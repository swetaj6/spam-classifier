#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Handle URLS.
   # Look for strings starting with http:// or https://.
   email_contents = re.sub('(http|https)://[^\s]*', 'httpaddr', email_contents)

