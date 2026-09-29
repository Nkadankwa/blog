+++
date = '2026-02-16T09:00:00+08:00'
image = '/images/database-planning-cover.png'
title = 'How I plan a small database schema before writing SQL'
categories = ['Journal']
tags = ['Databases', 'Software Design', 'Learning']
+++

When I need to create a database schema, I do not begin by opening an SQL editor. I begin with paper and a pen.

That first sketch gives me room to think about the problem before I become distracted by syntax. I write down the information the application needs to remember, group related fields into possible tables, and cross out ideas that do not belong. The page can be untidy because its job is to expose my assumptions.

## From a list to relationships

Once I have the main tables, I mark their primary keys and ask how one record connects to another. This is where I draw the foreign-key links. A line between two boxes forces me to decide whether the relationship is one-to-one, one-to-many, or something that needs a junction table.

I also look for duplicated information. If the same value would have to be corrected in several places, that is a sign that the design may need another table or a clearer relationship. I do not try to normalise everything just to satisfy a rule, but I want each table to have a purpose I can explain.

## Planning indexes before adding them

Indexes are part of the plan too. I think about the fields the application will search, filter, sort, or use in joins. A foreign key or a field used frequently in a lookup may deserve an index, but I do not want to add one to every column. Indexes can improve reads while adding storage and work to writes, so each one should answer a likely query.

Only when the drawing makes sense do I start writing SQL. The script may reveal problems that the paper missed, and the schema will still change as the application develops. Even so, starting on paper gives the first version a reason behind it. I am no longer creating tables because they feel right; I am translating a small model that I have already questioned.
