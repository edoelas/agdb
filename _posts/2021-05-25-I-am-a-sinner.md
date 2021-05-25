---
layout: post
title: I am a sinner
tags: ~WIP~ Presentation meta design blog
---

{% assign media = site.baseurl | append: "assets/media/" | append:  page.path | replace: ".md","" | replace: "_posts/",""  %}

![How did the blog look befor the redesign.]({{media}}/old_blog.png)
*How did the blog look befor the redesign.*

I have sinned. I said I wanted to keep this blog as minimal as possible. I bragged about the few lines I use. That I was using just 60 lines of CSS in total. What have I become? Now I use  around 200 lines of CSS. How many lines I will be using tomorrow? 1.000? 10.000? Nobody knows. I have became what I promissed to destroy. The bloat. I am a monster.

Okay, enough stupidity for today, now I am going to talk about what happened. Did I just woke up one morning and decided to spend my whole day fiddling with CSS? No, as I said I am not a web designer but as any human I like beautiful things. Two days ago, 23 May 2021, the day of the creation of this blog, at 22:08 I send the blog link to one of my friends and he replies:

> "It is as bad as beating a father."<br>- A. K.

That comeback opened my eyes. My response was not imediate but that comment fuelled the redesign. The harsh truth is that the default browser fonts are not the best ones.

When I did my first blog I loved its home page but two days ago, when I changed the layout of it, I discovered that my old home page was garbage. Two days ago I thought that the design of my blog was almost perfect. Now I think it was garbage. As we say here: "Who does not know god will pray to any saint." And that is exactly what happened. Now my question is: in a year or so, will I find that this blog is garbage and discover something way better? Is that even possible? I would think that it is not possible, but the recent events suggest the oposite.

### The changes

Originally I just thought of doing a few quality of life changes. Most of them are already done:

- **Adding RSS**. Yes, you can read my blog withot ever entering my blog. Without appreciating the beauty of it.

- **Hide useless links when printing**. If you want to print some article now you can do it withot printing the ugly [home]({{ site.baseurl }}) links. I don't know if anybody will do that but it is a problem that I have encountered when saving other webpages as PDF.

- **Google analytics**. Google knows what are you eating right now. Are you using [DuckDuckGo](https://duckduckgo.com/)? Useless in this page. I just want to know (for free) how many people is visiting my blog and where are the visitors from. Any alternatives are welcome, my email is at the end of the home screen. 

- **Improved the HTML code**. It was quite good, but there were still some problems because I did not understood how [Liquid](https://shopify.github.io/liquid/) works. Now it is even better.

There are still some things to do:

- Improve search
- Adapt design for smartphones
- [Solve hassle with image insertion](https://stackoverflow.com/questions/67660810/is-there-a-way-in-jekyll-to-set-a-base-path-for-images)
- [Alt text below images](https://stackoverflow.com/questions/19331362/using-an-image-caption-in-markdown-jekyll)

But while I was at it I thought: "Why not to take this oportunity to improove the design?". My plan was just to change the colours and fonts. In fact that is exactly what I did, but at a level I never believed I will be doing it.

### The redesign

First of all and the most important thing: **no HTML code has been harmed during the redesign of this blog**. The HTML code hasn't been changed at all. Everything is CSS work. That's nice.

Another important thing: **No useless CSS clases have been created to archive this purpose**. All the redesign has been done by modifying the CSS of the already existing classes and HTML elements. I have just created one class, `.dontprint`, which is used to hide the home links when printing.

How did I make it? By overwritting the classes used by Jekyll when converting my [Markdown](https://en.wikipedia.org/wiki/Markdown) to HTML. Most of the work has been done on the fonts. To get the fonts right (or what seems right to me) seamed really challenging but after reading some guides I think I made good decisions. At the end of the page I will leave some resources I find interesting but now I want to share with you the most influential one: [Choosing Web Fonts: A Beginner’s Guide](https://design.google/library/choosing-web-fonts-beginners-guide/). First, the content is interesting for begginers. Second, don't you see a similarity between that blog and my blog? No, I did not copy everything. When I found this blog post I already knew that I was going to use roboto, that I wanted black letters over white background and some other things. To decide the weight and size of the fonts I used another guide. So what did I took from this website? Two important things: the colours and the links.

#### Links

Lets start with the links. CSS allow you to modify the apperance of the links under four different circumstances: unvisited, visited, hovered and, pressed. First I thought about changing the color to a lighter gray when hovering and then to an enven lighter gray when pressing. I also was thinking to let the user know when a link has been already visited... probably using another gray? Four grays just for the links are too many grays. Using two different grays for text is fine. Three for some specific purposes can be interesting but Four for the same element? No. If you have a look to the [Google Design blog](https://design.google/library/racial-equity-everyday-products/) they use black for links and on hover they hide the underline. Just beautiful. It is not intrusive, does not require to use more colours, is easy to understand and to implement, gives exactly the right amount of information, it blends really well with the rest of the text etc. I like to use lots of links during the writting and this is a awesome solution. The CSS code looks like this:

```css
a{ color: var(--black);}
a:hover, a:active {text-decoration: none;}
```

#### Colours

Now we are going to talk about the colour. In lots of websites I have seen backgrounds and letters that are gray. Dark gray letters on top of light gray background. I believed in this since the contrast was reduced, making it les uncomfortable to look at, while the text could be read perfectly. But the designers in google are really brave. Black on top of white. I am following the path of the bravery with them. Either we win or we fall together, and I don't think google is going to fall any time soon. In the material design guide about [Text legibility](https://material.io/design/color/text-legibility.html#legibility-standards) they also suggest to use dark gray for less importante content. Finally I have added a light gray to use it as a box for special content, for exmaple, code blocks.

 Now I have 4 colours, `#fff`, `#eee`, `#333`, `#000`, each one with a specific purpose. That's all I need. It is still comfortable to read and the contrast is high enough that everybody can read it. The color palette is quite strightforward: four colours, two for the background and two for the text.

![Colours in order: #fff, #eee, #333, #000]({{ media }}/colours.png)
*Colours in order: #fff, #eee, #333, #000. First one invisible since it is the same colour as the background.*

Another question to think about is which color palette use for the code highlight. I think that is something I will take care of in the future. So far I have just choosen the [Tango](http://jwarby.github.io/jekyll-pygments-themes/languages/python.html) theme from [Pygments](https://pygments.org/) but I will modify it soon since I have been told that some colours might not have enough contrast.

#### Fonts

Fonts are really important for this blog. As you have seen there are not fancy graphics, menus, side boxes or anything. Everything is text. Not even buttons, I am using links. The only images you will find are the ones inside the posts and the favicon. I have made the concious decision of not putting an image as the header of each post, as almost any other blog does. The text oriented content is a barrier that once overcomed is very rewarding. I was taught that by a terminal.

I wanted to use Roboto as the font for my text. It is used by google so it must be a good choice. Google designers must know a couple of things about web design. I was planning to use a secondary font for some specific purposes but looking at the google design blog I found out that they were using only Roboto (that's not 100% true). Once again I believed in Google and used only Roboto. In fact, for the inline code and code blocks I am using Roboto on its mono variant. The usage of Roboto as my main and only font is not a fixed decision since I have read that for long text a serif font can be better suited. No one knows what the future holds.

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

I have done more changes than the ones explained here but this blog is not about web development. My reasoning when writting this blog is that it could help other developers who decide to create their own blog. At the end I am using just 100-150 extra CSS lines and importing 2 fonts. I am not a designer by any mean, in fact, as you may have discovered basically I just have merged some things that I found interesting, so do not take this as a guide. If you are curious about the CSS it is published on github under the path `/assets/css/BMFB.css`. The name stands for Better Mother Fu**ng Blog as a tribute to [bettermotherfuckingwebsite](http://bettermotherfuckingwebsite.com/), web that I used as my main inspiration when doing the first version of the Blog.

Here there are some markdown elements that I haven't shown yet. Those elements are latex-like math formulas, horizontal rules and tables:

$$mean = \frac{\displaystyle\sum_{i=1}^{n} x_{i}}{n}$$

---

| First name      |Last name| Number|
| :------------- | :----------: | -----------: |
|  Mario | Vargas   | 123123123    |
| Manuel   | Goterris | 13058375 |
| Pablo   | Albiol | 247674363 |

Probably there will be one last post about the blog itself, where I will talk about the supersimple search engine that I will implement and some minor changes. I promise that it will be the last one about web development.

Here there are some resources that I find interesting:


[Material design: Text legibility](https://material.io/design/color/text-legibility.html#legibility-standards)

[Material design: The type system](https://material.io/design/typography/the-type-system.html#applying-the-type-scale)