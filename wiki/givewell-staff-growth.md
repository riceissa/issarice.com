---
title: GiveWell staff growth
author: Issa Rice
date: 2016-07-27
---

I recently looked at GiveWell's staff growth over the years.
The data is from the [Our People](http://givewell.org/about/people) page, retrieved using the [Wayback Machine](https://archive.org/).
The page seems to have been created in mid-2010, so that's where the table starts (and before that, the number was presumably 2--4 anyway).
This is meant to be illustrative and not comprehensive.
Care was taken to detect the first point in time when an employee appeared or disappeared from a page, so the above table should be generally accurate but probably not completely so.
The Wayback Machine also had spotty coverage that lacked several months.

Date           Num          Diff
-----------  -----  ------------
2010-06-09   4
2011-06-04   4      $(-1, +1)$
2011-09-25   5      $(-0, +1)$
2012-01-02   4      $(-1, +0)$
2012-02-08   5      $(-0, +1)$
2012-07-19   8      $(-0, +3)$
2013-01-13   6      $(-2, +0)$
2013-04-30   7      $(-0, +1)$
2013-08-15   8      $(-1, +2)$
2013-09-28   10     $(-0, +2)$
2013-12-14   11     $(-0, +1)$
2014-07-13   12     $(-0, +1)$
2014-11-03   18     $(-0, +6)$
2015-02-01   18     $(-1, +1)$
2015-05-01   18     $(-1, +1)$
2015-06-16   23     $(-0, +5)$
2015-08-16   24     $(-0, +1)$
2015-10-01   30     $(-0, +6)$
2015-10-31   32     $(-0, +2)$
2015-11-22   31     $(-1, +0)$
2015-12-15   32     $(-1, +2)$
2016-03-10   31     $(-2, +1)$
2016-06-25   35     $(-2, +6)$
2016-07-23   37     $(-1, +3)$

Table: Growth of GiveWell. 'Num' is the number of full-time staff, 'Diff' is the
difference in 'Num' relative to the previous month and is given in the form
$(-x,y)$, where $x$ is the number full-time staff that left and $y$ is the
number of full-time staff that joined.

The following is a plot of the table above (which is better in some sense because it indicates the gaps when the employee count did not change):

![GiveWell employee plot through June 2016](givewell-employee.png)

The "cumulative number of employees" is just the number of people who have at one point worked for GiveWell, as of the indicated date; it is obtained by summing up the positive number in the diff column up to the date in question, and then adding the initial employee number.

However note that I think Holden in the October 2015 board meeting said GiveWell (excluding the Open Philanthropy Project) has around 12 full-time employees.
In other words, the table and plot don't distinguish between GiveWell and Open Philanthropy Project employees (as it is difficult to do so).
The numbers are also of full-time staff only, so does not include interns, conversation notes writers, etc.

Note also that *the gap between the two curves cannot decrease*.
It is for this reason that the survival ratio is good to look at in addition to the above graph:

![GiveWell employee survival ratio through June 2016](givewell-survival-ratio.png)

At each time $t$, the survival ratio is 'the number of employees at time $t$' divided by 'the number of cumulative employees at time $t$'.

# See also

- [GiveWell executive compensation]()

# External links

- [Vipul Naik shared this page](https://www.facebook.com/vipulnaik.r/posts/10208791654804628)
