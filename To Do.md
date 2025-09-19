# To Do List

This provides a short to-do list for next-stage updates/improvements.

## ✅ COMPLETED: Fix 'plot' button so that plotting can occur with any level of selection (including none).

* ✅ This now allows the user to click 'plot' at any stage - even if no subsets are selected
* ✅ Plots now have colours/shapes for different categories in each section. For example:
    * ✅ sites are coloured if no subsets are selected
    * ✅ systems are coloured if only a site is subsetted
    * ✅ phases are coloured if site and system act as subsets
* ✅ Implemented with dynamic plot titles, legends, and axis labels
* ✅ Full backward compatibility maintained

### Additional changes for plotting:
* ✅ Don't allow for plotting sites against each other for the scatterplot - this does not really make sense as the systems are different for each site. This means the checkboxes for sites should be removed from the dropdown select.
* ✅ Still allow for plotting all sites against each other.
* ✅ Move the 'variables' button to the top of the options box and highlight red when no variable is selected with a red message 'select a variable to view scatterplot'.

## Integrate boxplot and whisker charts when sites are compared
* ✅ Include a button on the options box that toggles between 'scatterplot' and 'compare'
* ✅ When 'scatterplot' is selected the current flow remains the same.
* ✅ When 'compare' is selected users MUST select one site (only) and select at least:
    * two or more systems (all phases in each) OR
    * one system and two or more phases
* ✅ Selection of comparisons systems/phases can be done using check boxes in the dropdown box currently used.
* ✅ The 'plot' button generates a box and whisker plot when 'compare' is selected
    * Box and whisker plots are aggregated at the top level as for scatterplots. This means that:
        * If two or more systems are selected for comparison then the plot comprises of two or more (equal to the number of systems selected) box and whisker plots side-by-side with all observations for each of those systems contained in those plots (respectively).
        * Same applies for phases selected - observations within each phase are plotted within the respective box and whisker plot for that phase.
* ✅ Integrate a button on the graph that allows the user to select 'cumulative by ID' or 'by plot site'.
    * The 'by crop' option means that all observations on that variable for the selected field plots are graphed as above
    * The 'cumulative by ID' option means that any duplicate observations are first summed then plotted to provide the cumulative result for each ID over time.
    * The latter is generally more meaningful for these results as we are concerned with cumulative results.

## Prepare the dashboard to allow for integration of more functions/analytics in a modular way

Aims: Re-organise the user interface to allow both for an intuitive UX and to modularise the components the users see in order to increase speed of development and an improved ability to allow for fee-based integrations for users (i.e. they simply pay a fee to access an additional dashboard component and, once paid, this is immediately available to them).

Layout concept:
* A fixed 'home' or 'options' column on the left hand side
* A viewing pane that includes tabs for different types of views or components for the selected option
* viewing pane changes based on the combined selection of options and tabs in the viewport selected
* Options (left column) should include:
    * Landing view^ (logo + map)
    * Options (select target site, system and phase)^
    * Costs by activity type
    * Yields and revenues
    * Gross margin comparisons^
    * Weather and other events
    * Measurements (e.g. soil moisture, soil nutrition, grain protein)
    * Price simulations and system comparisons
* Note: options with "^" at the end should be available. All others should be present in the options column but not clickable.
* For the 'options' page use the current options choices involving selection of a site and options to select one or more systems/phases for consideration
* For the gross margin comparisons use the current plots we are using and in the format we currently use.

Remember, our aim here is to improve the ability for the developer to add elements over time and enhance the data options presented within the dashboard without changing the overall UX/UI. So we are looking to develop this structure as one that is extendable over time.

One idea for how this should look is provided in the attachment.

## Integrate a prices simulation tool for comparisons and graph these as cumulative difference graphs to identify FSD and SSD outcomes
* Requirements:
    * Historical prices for target grains in real (current) prices as a (small) .csv
    * Distribution plotting functions - PDF and CDF - to allow for visual comparisons of the Gross Margin distributions for each system
    * A new screen on the dashboard that focuses on this approach
    * A set of functions to make FSD and SSD comparisons on distributions
    * A table to describe FSD/SSD relationships between comparisons (included in the screen)
### Method
* Take draws from historical prices with option to add in additional sensitivity (e.g. 5% variation added to allow for beyond-historic price outcomes)
* Undertake FSD and SSD tests
* Return gross margin distributions and CDFs along with binary indicators of FSD/SSD relationships

## 'What if' analysis
* Create a function that identifies under what price conditions one system will FSD/SSD another system
* Allow the user to specify price vectors for the crops and to analyse what that does to dominance/expected value rankings of systems (EV is from simulations and is average total value for a price simulation so in the case of a single vector of prices is just the total value)

## Anayltics
* Significant differences using bootstrap, MWU, Pearson, etc. tests
* Probability modelling of FSD/SSD outcomes based on commodity prices


## Integrate downloadable tables for means and SDs of variables as well as significant difference tests for chose comparisons
* Add another tab/page that allows the user to download tables of mean outcomes (with standard deviations) for selected variables and subsets. Also allow for a table of significant differences to be downloaded for selected comparisons - consider using a bootstrap to avoid assumptions of normality