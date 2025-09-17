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
* Don't allow for plotting sites against each other for the scatterplot - this does not really make sense as the systems are different for each site. This means the checkboxes for sites should be removed from the dropdown select.
* Still allow for plotting all sites against each other.
* Move the 'variables' button to the top of the options box and highlight red when no variable is selected with a red message 'select a variable to view scatterplot'.

## Integrate boxplot and whisker charts when sites are compared
* Include a button on the options box that toggles between 'scatterplot' and 'compare'
* When 'scatterplot' is selected the current flow remains the same.
* When 'compare' is selected users MUST select one site (only) and select at least:
    * two or more systems (all phases) OR
    * one system and two or more phases
* The 'plot' button generates a box and whisker plot when 'compare' is selected
* Integrate a button on the graph that allows the user to select 'by crop' or 'by plot site'.
    * The 'by crop' option means that all observations on that variable for the selected field plots are graphed
    * The 'by plot site' option means that the SUM of observations for each plot id are graphed.
    * The latter is generally more meaningful for these results as we are concerned with cumulative results.


## Integrate downloadable tables for means and SDs of variables as well as significant difference tests for chose comparisons
* Add another tab/page that allows the user to download tables of mean outcomes (with standard deviations) for selected variables and subsets. Also allow for a table of significant differences to be downloaded for selected comparisons - consider using a bootstrap to avoid assumptions of normality

## Integrate a prices simulation tool for comparisons and graph these as cumulative difference graphs to identify FSD and SSD outcomes
* TBD.