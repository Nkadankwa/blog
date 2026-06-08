+++
date = '2026-06-08T09:00:00+08:00'
image = '/images/clouderror.jpg'
title = 'What deploying a small web app taught me about row-level security'
categories = ['Journal']
tags = ['Deployment', 'Row-Level Security', 'Student Project']
+++

Building Eventally taught me how the parts of a web application fit together. Deploying it showed me how many important questions appear only when the application leaves the classroom environment.

The largest issue was row-level security. It was no longer enough for the application to connect to the database and return the expected records. I had to think about which user was making the request and which rows that user should be allowed to read, create, change, or delete.

## Working is not the same as being authorised

During development, broad permissions can make progress feel easy. The interface loads, inserts succeed, and the feature appears complete. In deployment, those same permissions can allow one user to see or modify another user's data.

Row-level security forced the access rule closer to the data. A policy needs a reliable identity and a clear relationship between that identity and each protected row. If ownership is not represented properly in the schema, the policy becomes difficult to express. If authentication context is missing, a rule that looked reasonable may reject everything—or protect nothing.

## Deployment turned hidden assumptions into work

This was one of the moments when I realised that the classroom had given us a foundation, not every step required to operate a real application. Configuration, environment variables, production permissions, error visibility, and recovery all became part of the software.

I do not see that as proof that the classroom work was useless. The deployment problem gave those earlier concepts a place to connect. Eventally made security concrete because the records represented actual users and actions rather than sample rows.

The lesson I am keeping is that access control cannot be a final switch added after the application works. Who may do what to which data belongs in the design of the schema, authentication flow, and tests from the beginning.
