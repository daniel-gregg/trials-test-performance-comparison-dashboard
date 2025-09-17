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

## Integrate comparisons
* Allow for the user to select a comparison set. For example:
    * If no subsets selected, user can compare one site to another
    * If site is selected, user can choose to compare one system to another for the given site
    * If site and system are selected, user can compare two or more phases for the given site-system combination

## Integrate boxplot and whisker charts for comparisons
* When implementing the comparisons, plot as a boxplot and whisker plots to better identify significant effects
* Consider doing this using a second tab on the dashboard (e.g. 'basic plots', 'comparisons')

## Integrate downloadable tables for means and SDs of variables as well as significant difference tests for chose comparisons
* Add another tab/page that allows the user to download tables of mean outcomes (with standard deviations) for selected variables and subsets. Also allow for a table of significant differences to be downloaded for selected comparisons - consider using a bootstrap to avoid assumptions of normality

## Integrate a prices simulation tool for comparisons and graph these as cumulative difference graphs to identify FSD and SSD outcomes
* TBD.