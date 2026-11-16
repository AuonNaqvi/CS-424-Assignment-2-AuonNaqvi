# Task 1

For Assignment 3, I decided to continue with my Car Mods visualization from Assignment 2, which consists of a sunburst diagram and the mod-rate matrix. The static visualization shows total counts of modified cars by range, while the matrix shows mod rates by class and year range. It displays all three car classes simultaneously, while the interactive version adds a dropdown menu that allows users to filter by Economy, Luxury, or Performance. Selecting a class updates both the sunburst and the matrix to display only cars belonging to that class.

The main reason I chose filtering was to make it easier to distinguish between the total number of modified cars and the percentage of cars modified within a particular category. This was something I noticed in Assignment 2, where a category having more modified cars didn't necessarily mean it had a higher mod rate. By filtering out the other classes, users can focus on one class and compare its mod rates across different year ranges without having to look through the entire matrix.

I expect this to reduce the time needed to identify these differences, although I'm not entirely sure it will. The static version already displays all the information at once, which could actually make comparisons between classes easier since users don't have to switch between filters. That's something I want to investigate during the evaluation.

# Task 2

Question: Does filtering the Car Mods visualization by car class help people compare mod counts and mod rates across car class and year range?

We hypothesis that users will more quickly identify differences between mod counts and mod rates across car class when using interactive visualizations.

| Analytical task | Condition 1 (Interactive) | Condition 2 (Static) |
| --- | --- | --- |
| Identify min/max percentages | For the luxury class, what percentage of cars are modded? (Q1) | In 2019 which class had the lowest percentage of modded cars? (Q2)|
| Identify min/max counts | Across all car classes, does any year range consistently have the highest count of modded cars? (Q3)| Across all car classes, which year range has the lowest total count of modded cars? (Q4)|

As seen in the table above we have 4 questions. Each question can be answered by either the static and interactive visualizations.
Each question forces users to examine different subsets of the data, Q1 forces people to look at just the luxury classes' data, Q2 forces people to compare the all the classes' 2019 data, Q3 forces people to compare specific year ranges to each other across all the car classes, Q4 forces forces users people to examine every year range within every car class.

Experimental procedure:
Participants are randomly selected from a pool of names. The first 10 names drawn will be the 10 particpants used for the evaluation. Participants will be informed the basics of what they'll be doing. Primarily, this means describing that they will be answering 4 questions, that they may answer however they choose, and that they will be timed.
Participants will be sat in a room and be presented with both the static and interactive visualizations but will not be able to interact with the interactive visualization until it must be used. There are 4 combinations for the conditions. I = interactive, s = static. Q1-I Q2-S Q3-I Q4-S, Q1-I Q2-S Q3-S Q4-I, Q1-S Q2-I Q3-I Q4-S, Q1-S Q2-I Q3-S Q4-I. Participants 1, 3, 5, 7 will use the first 2 combinations. Participants 2, 4, 6, 8 will use the last 2 combinations. Participants 9 and 10 will be randomly drawn (I used an online spin-the-wheel tool split up into 4ths.) Measurements taken are as follows:

- ID represents anonymized indexing of participants (in order they were selected) 
- Answer is the answer partipants gave
- Time is recorded in seconds, and starts from the moment the question is spoken to participant, and ends the moment they *finalize* their answer.
- Vis represents the vis type used to answer the question (I or S)
- Questions are represented as 1, 2, 3, 4, order listed in the table above. 
- Accuracy is represented as 1 for correct and 0 for incorrect. If a participant gives an answer that includes the right *and* a wrong answer, it is considered incorrect.

Results were recorded online. Participants were asked to download both html files that contained the vis, after things were explained as per the above procedure, they were asked to share the screen. After their combination type was determined, they were told to switch to the proper vis, then told the question. This was done until all answers were recorded digitally, then manually translated to a CSV file in Excel.

# Task 3

You should also document relevant observations that may help explain the results. For example, did participants struggle with particular visual encodings? Did they have difficulty finding or understanding the interaction controls? Were some tasks consistently harder than others?

Many participants seem to struggle with understanding the sunburst diagram. Interestingly enough I observed that most participants except 2 defaulted to using the matrix to answer as many questions as they could. Whether this is because culturally we emphasize raw numbers more, or because participants were less familiar with the sunburst in the first place, I'm unsure. My thinking is that the sunburst diagram looks similar to a pie chart (multiple participants compared it to that), so I had assumed familiarity wasn't an issue. This is data I neglected to collect though, and in hindsight would've made my analysis better. Interaction controls were exceedingly simple and everyone had similar levels of computer use. I had noticed that Q3 and Q4 took consistently longer to answer for most people, though this must be explored more upon in Task 4.

# Task 4

As we can see in my Assignment 3 notebook, task accuracy didnt vary significantly, between conditions, accuracy was 100% for Questions 1, 2, and 4 and Question 3's median and mean accuracy are the same, at 50%. This suggests that the visualization did not significantly impact the accuracy of participant's answers, so for the sake of this task, I won't be focusing on it as I dont think the results are very interesting. However, when we examine the descriptive statistics about time, we see some very interesting things. 

Overall, the total median time for the static visualization was 25 seconds, compared to the interactive visualization sitting at 19.5 This alone might *suggest* that the interactive visualization is better as it has a lower median time and the same accuracy as the static vis, however examining each Question's statistics reveals a much more nuanced perspective.

Question 1's median time for the static vis was 37.5 seconds, and the interactive vis was at 16 seconds, a very significant decrease in time, consistent with our overall statistics. 

Question 2's median time for the static vis was 20.5 seconds, interactive's was 13 seconds. Again a very significant decrease in time, however not as significant a decrease as Question 1's.

These results make sense considering the question asks for the mod percentage of a specific car class. The interactive visualization allows users to isolate Luxury cars, making the relevant information easier to find. In the static visualization, participants have to examine the overall matrix and work through the information themselves, doing math to figure out the solution.

Question 2 is also a question that has an answer relevant to each specific class' data. 

Question 3 and 4's interactive median times are significantly higher than the static vis' median times, with question 3's median interactive time being twice as long as its static counterpart. 

A possible explanation is that participants felt the need to examine all three classes to answer the question. In several instances of the interactive vis for the question, I found participants clinking through and observing each class' matrix one by one, before going back to the main visualization that displayed the necessary totals required for comparison. The static visualization already displays the classes together, whereas the interactive version encourages participants to filter between them. This, in my observations, made broader comparisons easier for the static participants to perform.

Question 4 follows a similar pattern to question 3, with the nature of the question concerning the overall dataset. I speculate that the reason the median time for the interactive participants is longer is the same as it is for question 3. Since this question concerns the entire dataset rather than a particular class, the class filter provides relatively little benefit.

Interestingly enough, half of participants, when their median times were observed across all 4 questions, answer questions faster with the interactive visualizations, whereas half of participants had better median times with the static visualizations.

All of this suggests to me that the beneficiality of the interactive vis is rather conditional. Yes, Questions 1 and 2 benefitted more from being able to filter between classes, but clearly questions 3 and 4 did not, and the same number of people who benefitted more from the interactive visualization also benefitted from the static visualization, showing, in my opinion, no greater overall utility. I would not be able to reasonably accept my hypothesis that users will more quickly identify differences between mod counts and mod rates across car class when using interactive visualizations. 

# Task 5

Question 3 was both the least accurate and one of the most time-consuming questions. This suggests its difficulty had a substantial effect on the overall results. It is likely that the wording was confusing, and in all honesty I tried rewording the question numerous times. It's all possible that comparing modification counts across multiple classes was simply harder than the other tasks. Static participants had to do mental math (one even used a calculator), and interactive participants needed to understand what the sunburst diagram was actually showing them in order to give a proper answer. Also because I was doing the evaluation online, I couldn't gauge participants concentration or perhaps initial confusion when looking at the questions or the visualizations.

However the insight revealed in Task 4 regarding question 3 was very interesting and completely outside my expectations. I expected everyone to just navigate to the Total's page and quickly discover that 15-19 was the correct answer. It highlights what I think is the greatest strength and weakness of my interactive design. Filtering made it easier to focus on individual categories, but it also removed information that might be useful for making broader comparisons *and promoted people to filter even when they didn't need to*. In hindsight, I think the interactive version would have benefited from allowing users to select multiple classes simultaneously, rather than only one at a time, so even though users might've compulsively filtered, they would've ended back up at the total view. Though in practice a good visualization wouldn't ever need this to be the case. Another possibility would be to keep a smaller overview of the entire dataset visible while filtering. This would allow users to focus on particular categories without completely losing the context of the other classes.

