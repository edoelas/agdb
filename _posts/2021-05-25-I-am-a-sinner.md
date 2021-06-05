---
layout: post
title: I am a sinner
tags: ~WIP~ Presentation meta design blog
---

{% assign media = site.baseurl | append: "assets/media/" | append:  page.path | replace: ".md","" | replace: "_posts/",""  %}

![How did the blog look before the redesign.]({{media}}/old_blog.png)
*How did the blog look before the redesign.*

I have sinned. I said I wanted to keep this blog as minimal as possible. I bragged about the few lines I use. That I was just using 60 CSS lines. What have I done? Now I use around 200 lines of CSS. How many lines I will be using tomorrow? 1.000? 10.000? Nobody knows. I have become what I promised to destroy. I am a monster. I am the father of the bloat.

Okay, enough stupidity for today, now I am going to talk about what happened. Did I just woke up one morning and decided to spend my whole day fiddling with CSS? No, as I said I am not a web designer but, like any human, I like beautiful things. Two days ago, 23 May 2021, the day of the creation of this blog, at 22:08 I sent the blog link to one of my friends and he replies:

> "Ugly as a toad."<br>- A. K.

That response opened my eyes. My reaction was not immediate but that comment started the redesign. The harsh truth is that the default browser fonts are not the best ones.

When I did my first blog I loved its home page but two days ago, when I changed the layout of it, I discovered that my old home page was garbage. Two days ago I thought that the design of my blog was almost perfect. Now I think it was garbage. As we say here: "Who does not know God will pray to any saint." And that is exactly what happened. Now my question is: in a year or so, will I find that this blog is garbage and discover something way better? Is that even possible? I would think that it is not possible, but the recent events suggest the opposite.

### The changes

Originally I just thought of doing a few quality of life changes. Most of them are already done:

- **Adding RSS**. Yes, you can read my blog without ever entering my blog. Without appreciating the beauty of it.

- **Hide useless links when printing**. If you want to print some article now you can do it without printing the ugly [home]({{ site.baseurl }}) links. I don't know if anybody will print them but it is a problem that I have encountered when saving other web pages as PDF.

- **Google analytics**. Google knows what are you eating right now. Are you using [DuckDuckGo](https://duckduckgo.com/)? Useless on this page. I just want to know (for free) how many people is visiting my blog and where are the visitors from. Any alternatives are welcome, my email is at the end of the home screen. 

- **Improved the HTML code**. It was quite good, but there were still some problems because I did not understand how [Liquid](https://shopify.github.io/liquid/) works. Now it is even better.

There are still some things to do:

- Improve search
- Adapt design for smartphones
- [Solve hassle with image insertion](https://stackoverflow.com/questions/67660810/is-there-a-way-in-jekyll-to-set-a-base-path-for-images)
- [Alt text below images](https://stackoverflow.com/questions/19331362/using-an-image-caption-in-markdown-jekyll)

But while I was at it I thought: "Why not take this opportunity to improve the design?". My plan was just to change the colours and fonts. In fact, that is exactly what I did, but with an attention to detail I never believed to be possible (for me).

### The redesign

First of all and the most important thing: **no HTML code has been harmed during the redesign of this blog**. The HTML code hasn't been changed at all. Everything is CSS work. That's nice.

Another important thing: **No useless CSS classes have been created to archive this purpose**. All the redesign has been done by modifying the CSS of already existing classes and HTML elements. I have just created one class, `.dontprint`, which is used to hide the home links when printing.

How did I make it? By overwriting the classes used by Jekyll when converting my [Markdown](https://en.wikipedia.org/wiki/Markdown) to HTML. It is not like I could do it any other way. Jekyll generates automagically the HTML code so I can't use classes or choose the HTML tags. 

Most of the work has been done on the fonts. To get the fonts right (or what seems right to me) seemed challenging but after reading some guides I think I made good decisions. At the end of the page I will leave some resources I find interesting, but now I want to share with you the most influential one: [Choosing Web Fonts: A Beginner’s Guide](https://design.google/library/choosing-web-fonts-beginners-guide/). First, the content is interesting for beginners. Second, don't you see a similarity between that blog and my blog? No, I did not copy everything. When I found this blog post I already knew that I was going to use Roboto, that I wanted dark letters over a light background and some other things. To decide the weight and size of the fonts I used another guide. So what did I took from this website? Two important things: the colours and the links.

#### Links

Let's start with the links. CSS allows you to modify the appearance of the links under four different circumstances: unvisited, visited, hovered and, pressed. First I thought about changing the colour to a lighter grey when hovering and then to an even lighter grey when pressing. I also was thinking to let the user know when a link has been already visited... probably using another grey? Four greys just for the links are too many greys. Using two different greys for text is fine. Three for some specific purposes can be interesting but Four for the same element? No. If you have a look at the [Google Design blog](https://design.google/library/racial-equity-everyday-products/) they use black for links and on hover they hide the underline. Just beautiful. It is not intrusive, does not require to use more colours, is easy to understand and to implement, gives exactly the right amount of information, blends well with the rest of the text etc. Markdown does not have an underline option so it cannot lead to confusion. I like to use lots of links during the writing and this is an awesome solution. The CSS code looks like this:

```css
a{ color: var(--black);}
a:hover, a:active {text-decoration: none;}
```

#### Colours

Now we are going to talk about colour. On lots of websites, I have seen backgrounds and letters that are grey. Dark grey letters on top of a light grey background. I believed in this since the contrast is reduced, making it less uncomfortable to look at, while the text could be read perfectly. But the designers in google are really brave. Black on top of white. I am following the path of the brave with them. Either we win or we fall together, and I don't think google is going to fall any time soon. In the material design guide about [Text legibility](https://material.io/design/color/text-legibility.html#legibility-standards) they also suggest using dark grey for less important content, so I did. Finally, I have added a light grey to use as a box for special content, for example, code blocks.

 Now I have 4 colours, `#fff`, `#eee`, `#333`, `#000`, each one with a specific purpose. That's all I need. It is still comfortable to read and the contrast is high enough that everybody can read it. The colour palette is quite straightforward: four colours, two for the background and two for the text.

![Colours in order: #fff, #eee, #333, #000]({{ media }}/colours.png)
*Colours in order: #fff, #eee, #333, #000. First one invisible since it is the same colour as the background.*

Another question to think about is which colour palette to use for the code highlight. I think that is something I will take care of in the future. So far I have just chosen the [Tango](http://jwarby.github.io/jekyll-pygments-themes/languages/python.html) theme from [Pygments](https://pygments.org/) but I will modify it soon since I have been told that some colours might not have enough contrast.

#### Fonts

Fonts are really important for this blog. As you have seen there are no fancy graphics, menus, side boxes or anything. Everything is text. Not even buttons, I am using links. The only images you will find are the ones inside the posts and the favicon. I have made the conscious decision of not putting an image as the header of each post, as almost any other blog does. The fear of text-oriented content is a barrier that once overcome is very rewarding. I was taught that by a terminal.

I wanted to use Roboto as the font for my text. It is used by Google so it must be a good choice. Google designers must know a couple of things about web design. I was planning to use a secondary font for some specific purposes but looking at the google design blog I found out that they were using only Roboto (that's not 100% true). Once again I believed in Google and used only Roboto. In fact, for the inline code and code blocks I am using Roboto on its mono variant. The usage of Roboto as my main and only font is not a fixed decision since I have read that for long text a serif font can be better suited. No one knows what the future holds.

In the guide about [the type system](https://material.io/design/typography/the-type-system.html#applying-the-type-scale) I discovered that it was not just about using one font and call it a day. It was about choosing the right size, weight, colour and spacing. This is the CSS that takes care of the important things related to the `<h1>` tag:

```css
h1{
  color: var(--black);
  font-size: 3.5rem;
  font-weight: 500;
  letter-spacing: -.01875rem;
  word-spacing: normal;
  line-height: 4.125rem;
  margin-top: 100px ;  
  margin-bottom: 50px ;  
  text-rendering: optimizeLegibility;
}
```

I am happy with how the fonts are looking now but there is room for improvement. I have barely touched the spacing between lines, words and characters. I hope you agree that choosing the right font is more complicated than it seems.

### Conclusion

I have done more changes than the ones explained here but this blog is not about web development. My reasoning when writing this blog is that it could help other developers who decide to create their own blog. In the end, I am using just 100-150 extra CSS lines and importing 2 fonts. I am not a designer by any mean as you may have discovered I just have merged some things that I found interesting, so do not take this as a guide. If you are curious about the CSS it is published on GitHub under the path `/assets/css/BMFB.css`. The name stands for Better Mother Fu**ng Blog as a tribute to [bettermotherfuckingwebsite](http://bettermotherfuckingwebsite.com/), the web that I used as my main inspiration when doing the first version of the Blog.

Here there are some markdown elements that I haven't shown yet. Those elements are latex-like math formulas, horizontal rules and tables:

$$mean = \frac{\displaystyle\sum_{i=1}^{n} x_{i}}{n}$$

---

| First name      |Last name| Number|
| :------------- | :----------: | -----------: |
|  Mario | Vargas   | 123123123    |
| Manuel   | Goterris | 13058375 |
| Pablo   | Albiol | 247674363 |

Probably there will be one last post about the blog itself where I will talk about the super simple search engine that I will implement and some minor changes. I promise that it will be the last one about web development.

Here there are some resources that I find interesting:


[Material design: Text legibility](https://material.io/design/color/text-legibility.html#legibility-standards)

[Material design: The type system](https://material.io/design/typography/the-type-system.html#applying-the-type-scale)
