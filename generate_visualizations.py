
    
  
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

cars = pd.read_csv("C:\\Users\\auon1\\Documents\\CS424Assignment2\\CS-424-Assignment-2-AuonNaqvi\\Assignment2\\CarsCleaned.csv")
print(cars["Modified"].value_counts())

# I'm keeping the same year groups I used in assignment 2.
year_ranges = ["Pre 05", "05-09", "10-14", "15-19", "20-26"]
car_classes = ["Economy", "Luxury", "Performance"]

carMods = make_subplots(rows=1, cols=2,
                        specs=[[{"type": "domain"}, {"type": "xy"}]],
                        subplot_titles=["Mods by year range", "Modification rate by year and class"],
                        column_widths=[.48, .52], horizontal_spacing=.08)

# First time through is the full dataset. The other three passes are for the dropdown.
for selected_class in ["All cars", "Economy", "Luxury", "Performance"]:
    if selected_class == "All cars":
        theseCars = cars
        matrix_classes = car_classes
    else:
        theseCars = cars[cars["Class"] == selected_class]
        matrix_classes = [selected_class]

    sunburst = px.sunburst(theseCars, path=["Modified", "Year_Range"],
                           color="Modified",
                           color_discrete_map={"Yes": "forestgreen", "No": "darkblue"})
    sunburst.update_traces(textinfo="label", sort=False)
    carMods.add_trace(sunburst.data[0], row=1, col=1)

    # A large number of modified cars doesn't always mean a high modification rate.
    byYearAndClass = theseCars.groupby(["Year_Range", "Class"])["Is Modified"].agg(["sum", "count"])
    percentages = []
    matrixText = []
    hoverText = []

    for yr in year_ranges:
        oneRow = []
        oneTextRow = []
        oneHoverRow = []
        for car_class in matrix_classes:
            if (yr, car_class) not in byYearAndClass.index:
                oneRow.append(None)
                oneTextRow.append("No cars")
                oneHoverRow.append("No cars in this group")
                continue

            modified_count = int(byYearAndClass.loc[(yr, car_class), "sum"])
            total_cars = int(byYearAndClass.loc[(yr, car_class), "count"])
            percent = modified_count / total_cars * 100
            oneRow.append(percent)

            # The older/performance groups get VERY small, so I kept the counts visible.
            small_group = "*" if total_cars < 3 else ""
            oneTextRow.append(f"{percent:.1f}%{small_group}<br>{modified_count}/{total_cars}")
            oneHoverRow.append(f"{modified_count} modified out of {total_cars} cars")

        percentages.append(oneRow)
        matrixText.append(oneTextRow)
        hoverText.append(oneHoverRow)

    carMods.add_trace(go.Heatmap(x=matrix_classes, y=year_ranges, z=percentages,
        text=matrixText, customdata=hoverText,
        texttemplate="%{text}", textfont=dict(size=12),
        hovertemplate="%{x} / %{y}<br>%{customdata}<extra></extra>",
        colorscale=[[0, "#edf4fb"], [1, "#24558b"]],
        zmin=0, zmax=100, xgap=4, ygap=4,
        colorbar=dict(title="Modified %", len=.75, thickness=15)),
        row=1, col=2)

    if selected_class != "All cars":
        carMods.data[-2].visible = False
        carMods.data[-1].visible = False

carMods.update_layout(title="Car Mods (" + str(len(cars)) + " cars observed)",
                      width=1150, height=635,
                      margin=dict(t=115, b=110, l=60, r=60),
                      showlegend=False)

# Plotly was trying to read 05-09 and 10-14 as dates.
carMods.update_xaxes(type="category", title_text="Vehicle class",
                     categoryorder="array", categoryarray=car_classes,
                     range=[-.5, 2.5], fixedrange=True, row=1, col=2)
carMods.update_yaxes(type="category", title_text="Estimated year range",
                     categoryorder="array", categoryarray=year_ranges[::-1],
                     fixedrange=True, row=1, col=2)
carMods.add_annotation(text="Cells show percent modified and modified/total. * = fewer than 3 cars.",
                       x=.5, y=-.18, xref="paper", yref="paper", showarrow=False)

# This copy only shows the first two charts, without any clicking or hover.
static = go.Figure(carMods)
static.data = static.data[:2]
static.write_html("static.html", include_plotlyjs=True,
                  config={"staticPlot": True, "displayModeBar": False})

