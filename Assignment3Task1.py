import pandas as pd
from plotly.express import *
from plotly.graph_objects import Heatmap, Figure
from plotly.subplots import make_subplots

cars = pd.read_csv("C:\\Users\\auon1\\Documents\\CS424Assignment2\\CS-424-Assignment-2-AuonNaqvi\\Assignment2\\CarsCleaned.csv")
print(cars["Modified"].value_counts())

yearRange = ["Pre 05", "05-09", "10-14", "15-19", "20-26"]
carClassList = ["Economy", "Luxury", "Performance"]

carMods = make_subplots(rows=1, cols=2,
    specs=[[{"type": "domain"}, {"type": "xy"}]],
    subplot_titles=["Mods by year range", "Mod rate by year and class"],
    column_widths=[.48, .52], horizontal_spacing=.08)

# First loop for the whole dataset, one loop for each class. dunno if there's a better way to do this.
for selected_class in ["All cars", "Economy", "Luxury", "Performance"]:
    if selected_class == "All cars":
        theseCars = cars
        matrix_classes = carClassList
    else:
        theseCars = cars[cars["Class"] == selected_class]
        matrix_classes = [selected_class]

    sunburstDiagram = sunburst(theseCars, path=["Modified", "Year_Range"],
        color="Modified",
        color_discrete_map={"Yes": "forestgreen", "No": "darkblue"})

    sunburstDiagram.update_traces(textinfo="label", sort=False)
    carMods.add_trace(sunburstDiagram.data[0], row=1, col=1)

    YearByClass = theseCars.groupby(["Year_Range", "Class"])["Is Modified"].agg(["sum", "count"])
    percentages = []
    matrixText = []
    hoverText = []

    for yr in yearRange:
        singleRow = []
        oneTextRow = []
        oneHoverRow = []
        for carClass in matrix_classes:
            if (yr, carClass) not in YearByClass.index:
                singleRow.append(None)
                oneTextRow.append("No cars")
                oneHoverRow.append("No cars in this group")
                continue

            modCount = int(YearByClass.loc[(yr, carClass), "sum"])
            totalCount = int(YearByClass.loc[(yr, carClass), "count"])
            percent = modCount / totalCount * 100
            singleRow.append(percent)

            # The performance groups for the yearranges get very small so I kept the counts visible.
            small_group = "*" if totalCount < 3 else ""
            oneTextRow.append(f"{percent:.1f}%{small_group}<br>{modCount}/{totalCount}")
            oneHoverRow.append(f"{modCount} modded out of {totalCount} cars")

        percentages.append(singleRow)
        matrixText.append(oneTextRow)
        hoverText.append(oneHoverRow)

    carMods.add_trace(Heatmap(x=matrix_classes, y=yearRange, z=percentages,
                              text=matrixText, customdata=hoverText,
                              texttemplate="%{text}", textfont=dict(size=12),
                              hovertemplate="%{x} / %{y}<br>%{customdata}<extra></extra>",
                              colorscale=[[0, "#edf4fb"], [1, "#24558b"]],
                              zmin=0, zmax=100, xgap=4, ygap=4,
                              colorbar=dict(title="modded %", len=.75, thickness=15)),
                      row=1, col=2)

    if selected_class != "All cars":
        carMods.data[-2].visible = False
        carMods.data[-1].visible = False

carMods.update_layout(title="Car Mods (" + str(len(cars)) + " cars observed)",
                      width=1150, height=635,
                      margin=dict(t=115, b=110, l=60, r=60),
                      showlegend=False)

# Plotly was trying to read 05-09 and 10-14 as dates.
carMods.update_xaxes(type="category", title_text="Car class",
                     categoryorder="array", categoryarray=carClassList,
                     range=[-.5, 2.5], fixedrange=True, row=1, col=2)
carMods.update_yaxes(type="category", title_text="Estimated year range",
                     categoryorder="array", categoryarray=yearRange[::-1],
                     fixedrange=True, row=1, col=2)
carMods.add_annotation(text="Cells show percent modded and modded/total. * = fewer than 3 cars.",
                       x=.5, y=-.18, xref="paper", yref="paper", showarrow=False)

# This copy only shows the first two charts, without any clicking or hover.
staticVis = Figure(carMods)
staticVis.data = staticVis.data[:2]
staticVis.write_html("staticVis.html", include_plotlyjs=True,
                     config={"staticPlot": True, "displayModeBar": False})

buttons = []
options = ["All cars", "Economy", "Luxury", "Performance"]
for i, option in enumerate(options):
    canSee = [False] * len(carMods.data)
    canSee[i * 2] = True
    canSee[i * 2 + 1] = True

    if option == "All cars":
        xRange = [-.5, 2.5]
        columns = carClassList
    else:
        xRange = [-.5, .5]
        columns = [option]

    buttons.append(dict(label=option, method="update", args=[
        {"visible": canSee},
        {"title.text": "Car Mods - " + option,
         "xaxis.categoryarray": columns, "xaxis.range": xRange}
    ]))

carMods.update_layout(updatemenus=[dict(buttons=buttons, type="dropdown",
                                        x=.12, y=1.17, xanchor="left", yanchor="top")])
carMods.add_annotation(text="Car class:", x=0, y=1.15,
                       xref="paper", yref="paper", xanchor="left", showarrow=False)
carMods.write_html("interactiveVis.html", include_plotlyjs=True,
                   config={"displayModeBar": False, "scrollZoom": False})

print("Saved staticVis.html and interactiveVis.html")