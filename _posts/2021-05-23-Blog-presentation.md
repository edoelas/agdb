---
layout: post
title: Blog presentation
date: 2021-05-23 10
tags: Presentation meta first
---

{% assign media = site.baseurl | append: "assets/media/" | append:  page.path | replace: ".md","" | replace: "_posts/",""  %}

Hi, how are you doing? I am fine, thanks. Either I have sent you personally the link to this blog, or I have no idea why you are here. Anyway, in this post, I plan to explain why I am making this blog, so, without further ado...

I already had a similar blog and I found it useful: it was a good way to record all my progress and mistakes. Usually, there were more mistakes than progress, but it is really important to remember the embarrassing mistakes to avoid repeating them. So this time I am planning to do the same but better. It also could be useful for the people that want to discover how is developing an indie game by somebody who just finished his degree and has zero experience in game development. We are going to learn a lot together. I also would like to improve my English writing, and this could be a good way to do it. The reason why I am making a new blog instead of using the old one is that some points could be improved: it was too tedious to publish a new post, the design could be better and, the structure was too complex. We could think about this blog as a v2 of the old one.

So that was 'why' I am using this blog. Now let's talk about the blog itself. I am not a web developer. I did an internship on web development and, after that, I was sure that I did not want to be a web developer. Today I still think that web development is not my thing. I would prefer to be a carpenter. But I have to admit that web development can be useful, for example, to create webs. One of the things that I do not like about the modern web is that even the simplest of the webs is bloated with stuff that I do not need, at a software and design level. This blog is *simple*. The fanciest thing you will find here is the search bar, which is a JavaScript function with less than 20 lines, and I am thinking about removing it since everybody can use the search function in his browser (ctrl+F). I am using [Jekyll](https://jekyllrb.com/) with [Github pages](https://pages.github.com/) and [Visual Studio Code](https://code.visualstudio.com/) as a text editor. That's all I need. The posts are created in markdown and once I push it to [Github](https://github.com/), [Travis CI](https://travis-ci.org/) takes care of the rest of the work and it gets uploaded programagically. All the editing happens locally but I can edit it via the Github webpage. I have data redundancy (since it is on my computer and in Github) and I just need to press a few buttons (zero commands) to publish it.

If we talk about the design, it is around 60 lines of CSS (including the syntax highlighting) and the most basic HTML you can imagine. ~~Maybe (probably not) you ask yourself: "Why the home button is under the title of the post?". It is because this allows me to delete four lines of HTML~~. It just has two kinds of pages: the home page and the posts. My contact information (e-mail) is at the bottom of the home page, no need for a separate page for that.

That was a bit of a rant, but it is also a statement. That's what I think about software development: [KISS](https://en.wikipedia.org/wiki/KISS_principle). Now let's talk about how I am going to use it. I plan to write something almost every day, even if it is five lines. That way, I force myself to invest a bit of time in the development of the project every day. Sometimes it will be things like what I have learned, what I have discovered, what I like or dislike about it etc. Be prepared to hear me complaining about things that probably I did not fully understand. But there will also be posts about how to solve that problem, a different approach to do the same thing,  recommending resources, and, of course, showing the outcome of my effort. It will not be well organized, that is why I decided to go with a tag system: it is simple and allows me to have some organization while not having it at all. Maybe I improve the search bar to allow for wildcards and specific attributes search, but that is the most I can do about the organization.

I think that was enough for a first post, a lot of text. I will finish by sharing with you an artist whose pixel art I like due to the way she works with the shapes, most of the time making them pixel-perfect even in weird angles. Her name is [nostalgictree](https://www.instagram.com/nostalgictree/).


![Pixel art by nostalgictree]({{ media }}/nostalgictree_art.jpg)
*Pixel art by [nostalgictree](https://www.instagram.com/nostalgictree/).*

**EDIT:** I decided to change a few things about how does the blog look. For the latest news check this blog post: [I am a sinner]({% post_url 2021-05-25-I-am-a-sinner %}). I have also crossed out two lines because they no longer made sense