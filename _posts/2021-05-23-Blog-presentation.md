---
layout: post
title: Blog presentation
tags: just-chatting
---

![alt text]({{ site.baseurl }}/assets/img/{{ page.path | replace: ".md","" | split: "/" | slice: -1 | }}/nostalgictree_art.jpg)

```python
s = "Python syntax highlighting"
print s
```
<pre>
{{ page.path | replace: ".md","" | split: "/" | slice: -1 | }}
</pre>
<pre>
{{page | inspect}}
</pre>
