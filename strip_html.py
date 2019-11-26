#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Strip all HTML.
    # Look for any expression that starts with < and ends with > and
    # does not have any < or > in the tag and replace it with a space.
    email_contents = re.sub('<[^<>]+>', ' ', email_contents)

