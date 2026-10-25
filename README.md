# CS-424-Assignment-2-AuonNaqvi

## Task 1
Here are the domain questions from Assignment 1, with the related data questions.

Domain Questions:
- How does the age distribution of vehicles differ across locations?
- Which Makes(brands) are more associated with particular car types?
- Are modified cars concentrated within certain year ranges, classes, or locations?
- How does the distribution of vehicle class vary across locations?

Data Questions:
- What is the car year-range distribution at each of the four locations?
- What is the frequency of each car type within each vehicle make (brand)?
- What is the count of modded vehicles, by year range, vehicle class, or location?
- What is the distribution of Economy, Luxury, and Performance cars across all 4 locations?

In assignment 1 I had already performed basic clean-up of the dataset. This meant running it through spellchecks, missing value checks, and making sure all entrees had consistent attribute types (int or string, mainly). When it comes to uncertainty I had already clarified in Assignment 1 the difficulties inherently present with my data collection method, particularly when it came to year and type approximations. As it pertains to the year range, in order to make the data more compatible with different kinds of graphs and charts I'm considering turning the different year-ranges into their average year (except pre 05 cars, which I'll just label as 2004.) I'm wondering about the practicalities of this decision though, as within the year-range approximations there could be the chance of, say, 80% of cars in the 05-09 category are 08 or 09. This would make the average (07), a bad representation of this group of cars. For car types, I believe my tendency to identify more SUV-crossovers is actually consistent with the industry. The majority of crossovers are from 15-19. Since American car design philosphy started changing around 2018-2019, the latter end of the year-range group, I'd be far less likely to misclassify a hatchback as an SUV crossover. Pre-2018, the design approaches for these two car types was quite distinct.

In my opinion, my domain questions were answerable from the dataset and also provided very unique insights in regards to it. For that reason I'm going to go through Assignment 2 with the above domain questions. Any changes will be documented in later tasks.

## Task 2
In the new dataset, I decided to add observation IDs for each car, in case I chose to speak about specific observations. I also added Year Start, Year End, and Estimated Year in order to make it easier to create something like a time-series and/or make it easier to encode the year-range attributes in terms a temporal manner rather than a categorical manner. Is Modified is either 0 or 1, making it easier to obtain frequencies for certain graph types. For "Pre-05" I decided to set the year start and end to 2004, and therefore the average is also 2004. This is for greater graph and chart variety and I consider it a worthy trade-off for greater visualization flexibility.