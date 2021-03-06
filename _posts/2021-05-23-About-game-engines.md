---
layout: post
title: About game engines
date: 2021-05-23 20
tags: Engine programming-language tool framework
---

Second blog post, and on the same day. You can call me a workaholic. The truth is that I just wanted to write something more related to game development. There are lots of things I have already learned that I will be publishing during the next few days. Today we are talking about game engines. The title is a bit misleading since I will not talk just about game engines, I will also talk about frameworks and other tools, we could rewrite the title as: "About things that we use to do games". But it was not that catchy.

When we decide to develop a game the first important decision is what do we want to develop. And it is not until we have taken that decision (or at least, we have a slight idea of the answer) that we can move to the next big question: "Which tools should I use?". Most of the time we are referring to the [game engine](https://en.wikipedia.org/wiki/Game_engine). And that is a quite difficult question. First of all, I am not a game engine expert. As I wrote in the first post I barely know anything about game development, but  I know some things about computer science and I will say a few words that can be helpful for beginners.


1. **Avoid searching on google "Which is the best game engine?" or similar questions**.

    Most of the results of that search will be pages that rank game engines based on doubtful criteria. I am not going to talk about why probably those rankings are crap but I will say this: taking your decision based on those rankings makes no sense. 

    Each game has different requirements. If you are going to do a 2D roguelike why would you pick the fastest 3D rendering game engine? Or if you want to make a simple puzzle game, why would you choose the game engine with the best physics engine? I think that there is no need to further develop this point. My suggestion is to make a list with the requirements of your games, with at least two sections: mandatory features and nice to have ones. Once you have that list you can start your search.

2. **Game development frameworks also exist**.

    I feel that most of the people interested in game design come from two groups: people interested in art and people interested in computers. If you are an artist with no experience in programming, I would suggest you to pick a game engine, but if you are a computer engineer,  you probably want to have a look at some of the frameworks. For me, the main advantages of frameworks are that you have more freedom and the chance to automate everything. No more clicking buttons and selecting dropdowns.

    That being said, frameworks usually are better suited for some kinds of games over others. If you want to do a 3D shooter game, a game engine with a nice level editor and illumination will be better. I also have the feeling that game engines tend to give you pre-made solutions while game frameworks leave these problems to the user. For example, all the big game engines give you some kind of [ECS](https://en.wikipedia.org/wiki/Entity_component_system), but frameworks like [libGDX](https://libgdx.com/) or [raylib](https://www.raylib.com/index.html) do not include it. Game frameworks are more barebones.

3. **Community, documentation, and programming language**.

    The three most important things in a Linux distro for me are community, documentation and repositories. It is a good idea to follow the same approach with game engines/frameworks. Instead of repositories now we are talking about programming languages and libraries.

    Of course, first, you need to make sure that it has the features that you need but after that, I think this is the next obvious rule to follow. These three things won't make your game run faster or to be prettier, at least not directly, but they will allow you to have a smoother experience. This point is especially important for beginners, like me. When starting the complexity can be a huge barrier.

    Programing languages is a huge topic on its own but I would suggest you **not** to pick the engine based on the languages that you know but the other way around, pick the language based on the engine that you are going to use. Lots of frameworks allow you to use multiple programming languages. Raylib for example has bindings for a ton of programming languages and libGDX can be used with most of the languages that run under the [Java Virtual Machine](https://en.wikipedia.org/wiki/Java_virtual_machine). Game engines usually are more restrictive but for example, [Godot](https://godotengine.org/) allows you to use GDScript, Visual Scripting, C# and, C++. One of the most popular game engines for indie games, Unity, allows you to use C++ and C#. There are [workarounds](https://www.reddit.com/r/golang/comments/kqg7pl/unitygolang_using_golang_as_a_scripting_engine/) in order to use other languages, but I would suggest against them because usually, the communities around these are non-existent. 

4. **You do not need such a powerful game engine**.

    If you are a [AAA](https://en.wikipedia.org/wiki/AAA_(video_game_industry)) company or you are planning to start a revolution in real-time 3D graphics forget about this point. If you are an indie developer I think it makes a lot of sense. Believe me, I have been there, I have been obsessed with using the fastest tools and it was a big mistake that was just slowing me down. If you do not believe me make a list of all the indie games that are not 2d or low poly and use high-resolution textures and models. I think you will have a hard time. And there is a reason for that: these kind of assets are really expensive (in terms of time and money), so it is not suitable for indie games, where the budget is a big constraint. I am not saying that you shouldn't pay attention to how fast is a game engine when picking one, I am just saying that please do not become obsessed as I did. Computers nowadays are incredibly powerful and these kind of super-fast tools are harder to master. Try to do anything with C and OpenGL and you will understand why.

With this post, I was not trying to cover all the important points related to picking a game engine. I just wanted to talk about some that usually are overlooked by beginners. I hope that this has been useful or at least interesting. Now I am going to leave some resources that came to my mind while writing this.

- **[Gamefromscratch](https://www.youtube.com/user/gamefromscratch) YouTube channel**. Mostly reviews of tools and resources for game development.

- **[The Cherno](https://www.youtube.com/user/TheChernoProject) YouTube channel**. A madlad who is creating his own game engine. Advanced but interesting. Also incredibly long.

- **[Learn OpenGL](https://learnopengl.com/) website**. A really nice OpenGL guide for advanced beginners. 

- **[Why is every indie game made with Pixel Art?](https://www.youtube.com/watch?v=m48xthwkpI0) video from [Out of Sight](https://www.youtube.com/channel/UCcmTXZ3oJVe0EHoTE4wCXpA)**. A really interesting video about why pixel art is so popular in indie games.

- **[Unity DOTS vs Handbuilt: Sample Project](https://www.youtube.com/watch?v=tInaI3pU19Y) video from [Nick Caston](https://www.youtube.com/channel/UCWm66r5LauAXin-Asjgo8YQ)**. Video comparing how efficient is Unity compared to C++ and OpenGL.2