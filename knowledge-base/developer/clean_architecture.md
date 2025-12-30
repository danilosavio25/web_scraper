# Clean_architecture Knowledge

> Category: patterns_architecture


## Source: atom.xml.md

xml version="1.0" encoding="utf-8"?

The Clean Code Blog


2023-01-19T20:57:45+00:00
http://blog.cleancoder.com/

Uncle Bob Martin

Functional Classes in Clojure

2023-01-19T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2023/01/19/functional-classes-clojure
<p>My previous <a href="http://blog.cleancoder.com/uncle-bob/2023/01/18/functional-classes.html">blog</a> seemed only to continue the confusion regarding classes in Functional Programming. Indeed, many people got quite irate. So perhaps a bit of code will help.</p>
<p><strong>Trigger Warning</strong>:</p>
<ul>
<li>Object Oriented Terminology.</li>
<li>Dynamically Typed Language.</li>
<li>Mixed Metaphors.</li>
<li>Distracting Animations.</li>
</ul>
<blockquote>
<p>To all the adherents of the <em>Statically Typed</em> Functional Programming religion: I know that you believe that <em>Static Typing</em> is an essential aspect of Functional Programming and that no mere dynamically typed language could ever begin to approach the heights and glory of <em>The One True and Holy TYPED Functional Apotheotic Paradigm</em>. But we lowly programmers quivering down here at the base of <em>Orthanc</em> can only hope to meekly subsist on the dregs that fall from on high.</p>
</blockquote>
<iframe width="560" height="315" src="https://www.youtube.com/embed/1KRqeDEQcYk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen=""></iframe>
<p>(R.I.P. Kirstie Alley</p>
<p>OK, so, once again…</p>
<blockquote>
<p><em>A class is an intentionally named abstraction that consists of a set of narrowly cohesive functions that operate over an internally defined data structure.</em></p>
</blockquote>
<p>We do not need the <code class="language-plaintext highlighter-rouge">class</code> keyword. Nor do we need polymorphic dispatch. Nor do we need inheritance. A class is just a description, whether in full or in part, of an object.</p>
<p>For example – it’s time we talked about clouds (which I have looked at from both sides now; and do, in fact, understand pretty well).</p>
<p>So… Here come your father’s parentheses!</p>
<p><img src="https://i.pinimg.com/originals/4f/1e/26/4f1e261d1afa9d58fd1125db5a5a4a12.jpg" /></p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(ns spacewar.game-logic.clouds
(:require [clojure.spec.alpha :as s]
[spacewar.geometry :as geo]
[spacewar.game-logic.config :as glc]))
(s/def ::x number?)
(s/def ::y number?)
(s/def ::concentration number?)
(s/def ::cloud (s/keys :req-un [::x ::y ::concentration]))
(s/def ::clouds (s/coll-of ::cloud))
(defn valid-cloud? [cloud]
(let [valid (s/valid? ::cloud cloud)]
(when (not valid)
(println (s/explain-str ::cloud cloud)))
valid))
(defn make-cloud
([]
(make-cloud 0 0 0))
([x y concentration]
{:x x
:y y
:concentration concentration}))
(defn harvest-dilithium [ms ship cloud]
(let [ship-pos [(:x ship) (:y ship)]
cloud-pos [(:x cloud) (:y cloud)]]
(if (&lt; (geo/distance ship-pos cloud-pos) glc/dilithium-harvest-range)
(let [max-harvest (\* ms glc/dilithium-harvest-rate)
need (- glc/ship-dilithium (:dilithium ship))
cloud-content (:concentration cloud)
harvest (min max-harvest cloud-content need)
ship (update ship :dilithium + harvest)
cloud (update cloud :concentration - harvest)]
[ship cloud])
[ship cloud])))
(defn update-dilithium-harvest [ms world]
(let [{:keys [clouds ship]} world]
(loop [clouds clouds ship ship harvested-clouds []]
(if (empty? clouds)
(assoc world :ship ship :clouds harvested-clouds)
(let [[ship cloud] (harvest-dilithium ms ship (first clouds))]
(recur (rest clouds) ship (conj harvested-clouds cloud)))))))
(defn update-clouds-age [ms world]
(let [clouds (:clouds world)
decay (Math/pow glc/cloud-decay-rate ms)
clouds (map #(update % :concentration \* decay) clouds)
clouds (filter #(&gt; (:concentration %) 1) clouds)
clouds (doall clouds)]
(assoc world :clouds clouds)))
(defn update-clouds [ms world]
(-&gt;&gt; world
(update-clouds-age ms)
(update-dilithium-harvest ms)))
</code></pre></div></div>
<p>Some years back I wrote a nice little <a href="http://blog.cleancoder.com/uncle-bob/2021/11/28/Spacewar.html">spacewar game</a> in Clojure. You can play it <a href="http://spacewar.fikesfarm.com/spacewar.html">here</a>. While playing, if you manage to blow up a Klingon, a sparkling cloud of <em>Dilithium Crystals</em> will remain behind, quickly dissipating. If you can guide your ship into the midst of that cloud, you will harvest some of that <em>Dilithium</em> and replenish your stores.</p>
<p>The code you see above is the <em>class</em> that represents the <em>Dilithium Cloud</em>.</p>
<p>The first thing to notice is that I defined the <em>TYPE</em> of the <code class="language-plaintext highlighter-rouge">cloud</code> <em>class</em> – <em>dynamically</em>.<br />
<img src="https://yt3.ggpht.com/a/AATXAJxJ07NzOxzlMLuiV6SGv808JXSCrALLJMXJ1w=s900-c-k-c0xffffffff-no-rj-mo" width="150" /></p>
<p>A <code class="language-plaintext highlighter-rouge">cloud</code> is an object with an <code class="language-plaintext highlighter-rouge">x</code> and <code class="language-plaintext highlighter-rouge">y</code> coordinate, and a <code class="language-plaintext highlighter-rouge">concentration</code>; all of which must be numbers. I also created a little type checking function named <code class="language-plaintext highlighter-rouge">valid-cloud?</code> that is used by my unit tests (not shown) to make sure the <em>TYPE</em> is not violated by any of the <em>methods</em>.</p>
<p>Next comes <code class="language-plaintext highlighter-rouge">make-cloud</code> the <em>constructor</em> of the <code class="language-plaintext highlighter-rouge">cloud</code> <em>class</em>.</p>
<iframe src="https://giphy.com/embed/vyTnNTrs3wqQ0UIvwE" width="480" height="400" frameborder="0" class="giphy-embed" allowfullscreen=""></iframe>
<p><a href="https://giphy.com/gifs/theoffice-the-office-tv-frame-toby-vyTnNTrs3wqQ0UIvwE">via GIPHY</a></p>
<p>There are two overloads of the <em>constructor</em>. The first takes no arguments and simply creates a <code class="language-plaintext highlighter-rouge">cloud</code> at (0,0) with no <em>Dilithium</em> in it. The second takes three arguments and loads the <em>instance variables</em> of the <em>class</em>.</p>
<iframe src="https://giphy.com/embed/2yP1jNgjNAkvu" width="480" height="480" frameborder="0" class="giphy-embed" allowfullscreen=""></iframe>
<p><a href="https://giphy.com/gifs/monty-python-2yP1jNgjNAkvu">via GIPHY</a></p>
<p>There are two primary <em>methods</em> of the <code class="language-plaintext highlighter-rouge">cloud</code> <em>class</em>: <code class="language-plaintext highlighter-rouge">update-clouds-age</code> and <code class="language-plaintext highlighter-rouge">update-dilithium-harvest</code>. The <code class="language-plaintext highlighter-rouge">update-clouds-age</code> <em>method</em> finds all the <code class="language-plaintext highlighter-rouge">cloud</code> <em>instances</em> in the <code class="language-plaintext highlighter-rouge">world</code> <em>object</em> and decreases their concentration by the <code class="language-plaintext highlighter-rouge">decay</code> factor – which is a function of the number of milliseconds (<code class="language-plaintext highlighter-rouge">ms</code>) since the last time they were updated. The <code class="language-plaintext highlighter-rouge">update-dilithium-harvest</code> <em>method</em> finds all the <code class="language-plaintext highlighter-rouge">cloud</code> <em>objects</em> that are within the <code class="language-plaintext highlighter-rouge">ship</code> <em>object</em>’s harvesting range and transfers <em>Dilithium</em> from those <code class="language-plaintext highlighter-rouge">cloud</code> <em>objects</em> to the <code class="language-plaintext highlighter-rouge">ship</code> <em>object</em>.</p>
<p>Now, you might notice that these <em>methods</em> are not the traditional style of method you would find in a Java program. For one thing, they deal with a list of <code class="language-plaintext highlighter-rouge">cloud</code> <em>objects</em> rather than an individual <code class="language-plaintext highlighter-rouge">cloud</code> <em>object</em>. Secondly, there’s nothing polymorphic about them. Third, they are <em>functional</em>, because they return a new <code class="language-plaintext highlighter-rouge">world</code> <em>object</em> with new <code class="language-plaintext highlighter-rouge">cloud</code> <em>objects</em> and, in the case of <code class="language-plaintext highlighter-rouge">update-dilithium-harvest</code>, a new <code class="language-plaintext highlighter-rouge">ship</code> <em>object</em>.</p>
<p>So are these really <em>methods</em> of the <code class="language-plaintext highlighter-rouge">cloud</code> <em>class</em>? Sure! Why not? They are a set of narrowly cohesive functions that manipulate an internal data structure within an intentionally named abstraction.</p>
<p>For all intents and purposes <code class="language-plaintext highlighter-rouge">cloud</code> is a °°°°°° °°°°°°° <em>class</em>.</p>
<iframe src="https://giphy.com/embed/TcdpZwYDPlWXC" width="480" height="240" frameborder="0" class="giphy-embed" allowfullscreen=""></iframe>
<p><a href="https://giphy.com/gifs/reaction-laughing-lotr-TcdpZwYDPlWXC">via GIPHY</a></p>
<p>So there.</p>

Functional Classes

2023-01-18T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2023/01/18/functional-classes
<p>I recently tweeted the following:</p>
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="en" dir="ltr">Should you subdivide a functional program into classes the way you would an object oriented program?<br /><br />Yes. You should. Because the rules don’t change just because you’ve chosen to use immutable data structures.</p>&mdash; Uncle Bob Martin (@unclebobmartin) <a href="https://twitter.com/unclebobmartin/status/1615436628385824769?ref\_src=twsrc%5Etfw">January 17, 2023</a></blockquote>
<script async="" src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
<p>This led to a bevy of interesting responses about the difference between classes and modules. In answer to those responses I tweeted this:</p>
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="en" dir="ltr">A class is a group of cohesive and narrowly defined functions that operate on an encapsulated data structure. The functions may, or may not, be polymorphically deployed.</p>&mdash; Uncle Bob Martin (@unclebobmartin) <a href="https://twitter.com/unclebobmartin/status/1615438162746134528?ref\_src=twsrc%5Etfw">January 17, 2023</a></blockquote>
<script async="" src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
<p>Of course that only led to an increased number of interesting responses. And so I thought that it might be wise to blog about my reasoning rather than to continue trying to cram that reasoning into tweets.</p>
<p>If you are in doubt about what FP is, and about what OO is, and about whether the two are compatible, then I recommend <a href="http://blog.cleancoder.com/uncle-bob/2018/04/13/FPvsOO.html">this</a> old blog of mine.</p>
<p>What is a class? According to the dictionary a class is:</p>
<blockquote>
<p><em>A set, collection, group, or configuration containing members regarded as having certain attributes or traits in common; a kind or category.</em></p>
</blockquote>
<p>Now consider that definition when reading the next paragraph.</p>
<p>In OO languages we organize our programs into classes of objects that share similar traits. We describe those objects in terms of the attributes and behaviors that they have in common. We strive to create hierarchies of classification that those objects can fit within. We consider the higher level classifications to be abstractions that allow the expression of general truths that are independent of irrelevant details. (Indeed, I once defined abstraction as: <em>The Amplification of the essential, and the elimination of the irrelevant.</em><a href="https://www.amazon.com/Designing-Object-Oriented-Applications-Method/dp/0132038374">[1]</a>)</p>
<p>In 1966 the power of abstraction by classification led the authors of Simula to create the keyword <code class="language-plaintext highlighter-rouge">class</code>. In 1980, Bjarne Stroustrup continued that convention and used the <code class="language-plaintext highlighter-rouge">class</code> keyword in C++. This was actually somewhat strange because C already had the keyword <code class="language-plaintext highlighter-rouge">struct</code> which had a virtually identical meaning. But the power of the word <code class="language-plaintext highlighter-rouge">class</code> held sway.</p>
<p>In the mid 90s the power of that word led the authors of Java (and then C#) to declare <em>and enforce</em> that <em>everything</em> in a program must be part of a class. This was a dramatic overreach. It seems to me that some of the things that Java forces into classes ought not to be in classes at all. For example, the class <code class="language-plaintext highlighter-rouge">java.lang.Math</code> is really just a namespace for a batch of functions and is not, in any sense, a classification of objects.</p>
<p>This conflation of object classification and namespaces is confusing and unnecessary; and is probably part of the reason my initial tweet generated the responses that it did.</p>
<p>Another overreach in Java (and by extension C#) is that methods are polymorphic by default. Polymorphism is a tool, not a rule. Many, if not most, function calls do not require dynamic dispatch.</p>
<p>These kinds of overreach lead to confusion about what a class really is. I believe that most of the responses to my tweet were the result of that confusion.</p>
<p>So let’s cut to the chase.</p>
<p>One of the oldest rules of software design is that we should partition the elements of the system into loosely coupled and internally cohesive elements. Those elements become well named places where we can put data and behavior. This follows the old proverb: <em>A place for everything, and everything in its place.</em></p>
<p>What are those elements? It seems obvious that the classification structures of objects ought to be high on the list. Namespaced function libraries like <code class="language-plaintext highlighter-rouge">java.lang.Math</code> are another obvious choice. In the one case we have a batch of functions that manipulate an internal data structure. In the other case we have a batch of functions that manipulate an external data structure.</p>
<p>The essential charachteristic of these elements, these batches of functions, is that they are internally cohesive. That means that all the functions in the batch are strongly related to each other because they manipulate the same data structures, whether internal or external. It is that cohesion that drives the partitioning of a software design.</p>
<p>###Example</p>
<p>Recently I have been writing an application called <a href="http://github.com/unclebob/more-speech"><code class="language-plaintext highlighter-rouge">more-speech</code></a> which is a client that browses messages on the <a href="https://nostr.com"><code class="language-plaintext highlighter-rouge">nostr</code></a> network. This nework is composed of relays that use a simple websocket protocol to transmit messages to clients. The <code class="language-plaintext highlighter-rouge">more-speech</code> client is written in Clojure, which is a Functional Programming language.</p>
<p>Early on I created a module named <code class="language-plaintext highlighter-rouge">protocol</code> to house the code that implemented the <code class="language-plaintext highlighter-rouge">nostr</code> protocol. I began this module by managing the websockets over which the messages travelled, and then decoding those messages and manipulating them according to the rules of the protocol.</p>
<p>Clojure is not a traditional OOPL, there is no <code class="language-plaintext highlighter-rouge">class</code> keyword that is used to declare and define objects and the methods that manipulate them. Rather, a module in Clojure is just a batch of functions that are not syntactically bound to any particular data. Thus my <code class="language-plaintext highlighter-rouge">protocol</code> module had functions that dealt with <code class="language-plaintext highlighter-rouge">WebSocket</code>s and functions that dealth with messages and functions that dealth with protocol elements. They were cohesive in the sense that they were all related to the <code class="language-plaintext highlighter-rouge">nostr</code> protocol; but there was no central data structure that unified them.</p>
<p>The other day I realized that I was missing an abstraction. The <code class="language-plaintext highlighter-rouge">nostr</code> protocol may be transmitted over websockets but the protocol rules have nothing to do with websockets. Those rules deal with the data that comes through the websockets, but not the websockets themselves. Yet my <code class="language-plaintext highlighter-rouge">protocol</code> module was littered with websocket code.</p>
<p>So I separated the websocket code from the <code class="language-plaintext highlighter-rouge">protocol</code> code by creating an abstraction that I called <code class="language-plaintext highlighter-rouge">relay</code>. A <code class="language-plaintext highlighter-rouge">relay</code> is a data structure that contains the <code class="language-plaintext highlighter-rouge">url</code> of a websocket, the websocket itself, and a function to call when messages are received. The <code class="language-plaintext highlighter-rouge">relay</code> data structure is manipulated by functions such as <code class="language-plaintext highlighter-rouge">make</code>, <code class="language-plaintext highlighter-rouge">open</code>, <code class="language-plaintext highlighter-rouge">close</code>, and <code class="language-plaintext highlighter-rouge">send</code>.</p>
<p>This <code class="language-plaintext highlighter-rouge">relay</code> module very clearly defines a class of objects. The <code class="language-plaintext highlighter-rouge">protocol</code> constructs a <code class="language-plaintext highlighter-rouge">relay</code> object for each of the urls in a list of active relays. It <code class="language-plaintext highlighter-rouge">open</code>s those <code class="language-plaintext highlighter-rouge">relay</code>s and <code class="language-plaintext highlighter-rouge">send</code>s messages to them. Messages that are received are sent to <code class="language-plaintext highlighter-rouge">protocol</code> through the callback functions that are passed into the function that constructs the <code class="language-plaintext highlighter-rouge">relay</code> object. In order to maintain the immutability and referential transparency constraints of Functional Programming, the functions that update the state of a <code class="language-plaintext highlighter-rouge">relay</code> return a new instance of that <code class="language-plaintext highlighter-rouge">relay</code>.</p>
<p>###Lesson</p>
<p>Java, C#, Ruby, and C++ all either enforce, or stronly encourage, the partitioning of systems into classes. Clojure does not; it is entirely agnostic about classes. The lesson that I learned from <code class="language-plaintext highlighter-rouge">protocol</code> and <code class="language-plaintext highlighter-rouge">relay</code> is that I had not been paying enough attention to class structure when writing complex Clojure programs. Instead, I had been allowing functions to accumulate in modules in a, more or less, ad hoc fashion – similar to the way one might program in C, Fortran, Basic, or even Assembler. But that was lazy. Objects exist in programs, and they can, and should, be classified. So, from now on, I will be paying much more attention to the classification structure of the objects my systems.</p>
<blockquote>
<p><em>A place for everything, and everything in its place.</em></p>
</blockquote>

Space War

2021-11-28T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2021/11/28/Spacewar
<p>For the last month I've been spending a lot of time working on <a href="https://github.com/unclebob/spacewar">Space War</a>. I know, I know, I should have been working on <a href="https://cleancoders.com"><em>Clean Code Episode 67: Legacy Code</em></a>, and <a href="https://www.youtube.com/playlist?list=PLmsuNLXeDr6Y1-a9ASu4mfxqDIgr-oaU6"><em>Euler 5</em></a>, and <a href="https://www.youtube.com/channel/UCThitpd5RCB2J5b\_HlcseMw"><em>Countest and Curmugeon 3</em></a>. I should have been working on a blog, or a new book, or... But I couldn't let go of Space War. It kept calling me.</p>
<p>The first time I wrote Space War was in 1978. I wrote it in <em>Alcom</em>, which was a simple derivative of <a href="https://en.wikipedia.org/wiki/FOCAL\_(programming\_language)"><em>Focal</em></a>, which was an analog of <em>Basic</em> for the <a href="https://en.wikipedia.org/wiki/PDP-8">PDP-8</a>. The computer was an <em>M365</em> which was an augmented version of a PDP-8 and was proprietery to Teradyne, my employer at the time.</p>
<p>The UI was screen based, using character graphics, similar to <em>curses</em>. Screen updates took on the order of a second. All input was through the keyboard.</p>
<p>We used to play it on one machine while waiting for a compile on another.</p>
<p>Forty years later, in September of 2018, I started working on <em>this</em> version of Space War. It's an animated GUI driven system with a frame rate of 30fps. It is written entirely in Clojure and uses the <a href="http://www.quil.info">Quil</a> shim for the <a href="https://processing.org">Processing</a> GUI framework.</p>
<p>My justification for writing it was so that I could use it as the case study for my cleancoders.com videos on <em>Functional Programming</em>. Once that series of videos was complete, I set Space War aside and started working on other things.</p>
<p>Then, a month ago, the program called to me. I don't know why. Perhaps it was because I'd left it in a partially completed state. Perhaps it was because I had just finished <a href="https://www.amazon.com/Clean-Craftsmanship-Disciplines-Standards-Ethics/dp/013691571X"><em>Clean Craftsmanship</em></a> and I needed a way to decompress. Or, perhaps it was just because I felt like it. Whatever the reason, I loaded up the project and started goofing around with it.</p>
<p>Now I'm sure you've had that feeling of trepidation when you pick up a code base that you haven't seen in three years. I certainly felt it. I mean, what was I going to find in there? Would I be able to get my bearings and understand the code? Or would I flail around aimlessly for weeks?</p>
<p>I needn't have worried. The code base was nicely organized. There was a very nice suite of tests that covered the vast majority of the game logic. The GUI code, though not tested, was simple enough to understand at a glance.</p>
<p>But, perhaps most importantly, this code was written to be 100% functional. No variables were mutated, anywhere in the code. This meant that every function did exactly what it said it did; and left no detritus around to confound other functions. No function could be impacted by the state of the system because the system did not have "a state".</p>
<p>Now maybe you are rolling your eyes at that last paragraph. Several years ago I might have rolled my eyes too. But the relief I experienced coming back into this code base after three years of not touching it, and knowing it was functional, was palpable.</p>
<p>Another thing that gave me a significant amount of help was that all the critical data structures in the system were described and tested using <code class="language-plaintext highlighter-rouge">clojure/spec</code>. This was profoundly helpful because it gave me the kind of declarative help that is usually reserved for statically typed languages.</p>
<p>For example, This is a Klingon:</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(s/def ::x number?)
(s/def ::y number?)
(s/def ::shields number?)
(s/def ::antimatter number?)
(s/def ::kinetics number?)
(s/def ::torpedos number?)
(s/def ::weapon-charge number?)
(s/def ::velocity (s/tuple number? number?))
(s/def ::thrust (s/tuple number? number?))
(s/def ::battle-state-age number?)
(s/def ::battle-state #{:no-battle :flank-right :flank-left :retreating :advancing})
(s/def ::cruise-state #{:patrol :guard :refuel :mission})
(s/def ::mission #{:blockade :seek-and-destroy :escape-corbomite})
(s/def ::klingon (s/keys :req-un [::x ::y ::shields ::antimatter
::kinetics ::torpedos ::weapon-charge
::velocity ::thrust
::battle-state-age ::battle-state
::cruise-state
::mission]
:opt-un [::hit/hit]))
</code></pre></div></div>
<p>These kinds of <code class="language-plaintext highlighter-rouge">clojure/spec</code> descriptions gave me the documentation I needed to reaquaint myself with the critical data structures of the system. They also gave me the ability to check that any functions I wrote kept those data structures conformant to the spec.</p>
<p>All of this means that I was able to make progress in this code base quickly, and with a high degree of confidence. <em>I never had that feeling of wading through bogs of legacy code.</em></p>
<p>Anyway, I'm done now, for the time being. I've given the player a mission to complete, and made it challenging, but possible, to complete that mission. A game requires 2-3 hours of intense play, is tactially and strategically challenging, and is often punctuated by moments of sheer panic.</p>
<p>I hope you enjoy downloading it, firing up Clojure, and playing it. Consider it my Christmas present to you.</p>
<p>One last thing. Three years ago <a href="https://github.com/mfikes">Mike Fikes</a> saw my Space War program and converted it from Clojure to <a href="https://clojurescript.org">ClojureScript</a>. The change was so miniscule that the two are now a single code base with a tiny smattering of conditional compilation for the very few differences. So if you want to play the game on-line you can just click on <a href="http://spacewar.fikesfarm.com/spacewar.html">http://spacewar.fikesfarm.com/spacewar.html</a>. Mike has kindly kept this version up to date so -- have at it!</p>

Functional Duplications

2021-10-28T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2021/10/28/functional-duplication
<p>I broke out my old <a href="https://github.com/unclebob/spacewar">Space War</a> game a few days ago and decided to make a few changes to speed the game up and make it more fun to play. In so doing I discovered a very interesting bug.</p>
<p>One of the changes I made was to populate the initial space with a few random bases scattered here and there. This would allow the player some extra resources with which to battle the Klingons while building up a network of more bases.</p>
<p>While I was playing the modified game, it crashed. Hard.</p>
<p>Now I wrote this with TDD, and I was very disciplined about the cleanliness of the code, and the test coverage. So this was unexpected. So I dug up all my old debugging skills from the pit in which I had buried them, and started to work out what was going on.</p>
<p>It wasn't long before I realized that crash was occuring because a transport was being launched between two bases, but the angle of the velocity vector of the transport was <code class="language-plaintext highlighter-rouge">:bad-angle</code>. This can only happen if the two bases exist at the exact same location.</p>
<p>Bases don't move around in this game, so there's no chance that two bases will accidentally slide on top of each other. There is a very (very) minor chance that the random number generator will put two bases on top of each other at the start of the game; but the odds are so miniscule that didn't worry about it. In any case, this crash happened well into the game I was playing, so initial values could not have been the cause.</p>
<p>Fortunately it's pretty easy to hunt and peck around in the game, so I was quickly able to discover that the two bases in question were duplicates of each other. Something in my code was duplicating bases!</p>
<p>Well now that should't be too hard to find. So I wrote a litte function that would examine the world and halt with a message if the world contained two bases at the same location. I called this function in the main update loop, and sure enough after 20 minutes of play the program halted with my message.</p>
<p>Unfortunately being able to detect <em>that</em> the duplication occurred did not tell me <em>where</em> it occurred. So I laced the code with calls to my <code class="language-plaintext highlighter-rouge">check-for-duplicate-base</code> function.</p>
<p>It took me a few tries because the problem was not in any of the obvious places. So over a few hours I added more and more calls to <code class="language-plaintext highlighter-rouge">check-for-duplicate-base</code>.</p>
<p>Eventually I found the culprit in a low frequency function named <code class="language-plaintext highlighter-rouge">klingons-steal-antimatter</code>.</p>
<p>This function is called once per second. It checks to see if any klingons are within <code class="language-plaintext highlighter-rouge">docking-distance</code> of a base, and if so it steals antimatter from that base.</p>
<p>This explained why the crash took so long to create. Most of the time it takes 20 minutes or so for a Klingon to move close enough to a base to start stealing.</p>
<p>Anyway, I looked at the code and didn't see any obvious duplication. So I wrote a unit test to check whether that function duplicated bases. My test positioned a klingon near a base, called the <code class="language-plaintext highlighter-rouge">klingons-steal-antimatter</code> function, and then checked the number of bases in the world. The result: No duplication.</p>
<p>Now, before I continue, let me describe the process I used in the <code class="language-plaintext highlighter-rouge">klingons-steal-antimatter</code> function.</p>
<p>The function created a list of <em>thefts</em>. A theft is a <code class="language-plaintext highlighter-rouge">[thief victim]</code> pair. It used those pairs to create lists of all the thieves and victims, and separate lists of all the innocent klingons and all the unvictimized bases.</p>
<p>Why? Because this is a purely functional program. In a purely functional program you cannot update the status of an object. Instead you transformm old objects into new objects. So when stealing antimatter from a base you must create a new base with less antimatter, and you must create a new klingon with more antimatter. When you are done processing all the thefts you are left with a list of all the updated klingons, and a list of all the updated bases.</p>
<p>The <code class="language-plaintext highlighter-rouge">world</code> contains a list of all the klingons and a list of all the bases. In order to update the <code class="language-plaintext highlighter-rouge">world</code> after processing the thefts you have to concatenate the updated bases with the unvictimized bases, and you have to concatenate the updated klingons with the innocent klingons.</p>
<p>Got it? Understand? Good.</p>
<p>As I pondered the code I realized that a base could be robbed by more than one klingon. Klingons tend to slowly migrate towards bases and then steal from them. Two or three or more could eventually manage to slide over to a base, like a pack of coyotes squabbling over a carcass.</p>
<p>Now I already had a unit test that checked for this condition. It created two klingons near one base and made sure that each klingon was able to steal from that base. What that test did not do, however, was count the number of bases in the world when it was done.</p>
<p>So I added a check. <code class="language-plaintext highlighter-rouge">base-count =&gt; 1</code>. Whoops, it came back with <code class="language-plaintext highlighter-rouge">2</code>.</p>
<p>Now maybe you've already figured out why this happened. But let me walk you through it. My function identified two thefts: <code class="language-plaintext highlighter-rouge">[[k1 b] [k2 b]]</code> It returned with the results of each theft. Let's say that <code class="language-plaintext highlighter-rouge">k1</code> stole <code class="language-plaintext highlighter-rouge">a1</code> antimatter from <code class="language-plaintext highlighter-rouge">b</code>, and <code class="language-plaintext highlighter-rouge">k2</code> stole <code class="language-plaintext highlighter-rouge">a2</code> from <code class="language-plaintext highlighter-rouge">b</code>. What the function returned was <code class="language-plaintext highlighter-rouge">[[k1+a1 b-a1] [k1+a2 b-a2]]</code>. Note that the second theft in the list was <em>not</em> <code class="language-plaintext highlighter-rouge">[k2+a2 b-a1-a2]</code>.</p>
<p>You've probably guessed the rest. When I reassembled the world, I added all the bases that had been victims; and -- of course -- I added <code class="language-plaintext highlighter-rouge">b-a1</code> <em>and</em> <code class="language-plaintext highlighter-rouge">b-a2</code>.</p>
<p>Fortunately I had lots of unit tests to fall back on. Changing the algorithm was actually quite challenging, and required me to put all the klingons and bases into hashmaps keyed by their positions. I won't bore you with the details.</p>
<p>So I added unit tests to check for the duplications, saw them fail, and then gradually made them pass. The unit tests allowed me to be sure that I was not breaking something else along the way.</p>
<p>Now you might think this is just an esoteric little problem that you'll never encounter. However, if you are writing functional programs, you <em>will</em> face this issue, and you'll likely face it a lot. Dealing with immutable lists of objects means that when you update such a list you must recreate it. If you are only updating <code class="language-plaintext highlighter-rouge">m</code> out of <code class="language-plaintext highlighter-rouge">n</code> elements of the list, you have to partition the original list into the <code class="language-plaintext highlighter-rouge">m</code> elements you are changing and the <code class="language-plaintext highlighter-rouge">n-m</code> elements you are not changing; and then you have to concatenate the <code class="language-plaintext highlighter-rouge">m</code> changed elements with the <code class="language-plaintext highlighter-rouge">n-m</code> unchanged elements in order to create the updated list.</p>
<p>Anyway, I thought you might find that interesting.</p>

Roots

2021-09-25T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2021/09/25/roots
<p>When I was 15 or so, my father would drive me, and my best friend, Tim Conrad, to the Digital Equipment Corporation (DEC) sales office each Saturday. This was a 30 min drive. My father would drop us off in the morning and pick us up in the late afternoon. He spend two hours in his car each Saturday hauling us around.</p>
<blockquote>
<p><em>Thanks Dad!</em></p>
</blockquote>
<p>Tim and I would spend our day "playing" with the floor model of the PDP-8 they had at the office. The office staff were very accommodating and accepting of our presence, and they helped us out if we needed any fresh rolls of teleprinter paper, or paper tape.</p>
<p>Several years later, at the age of 20, I found myself working at Teradyne Applied Systems in Chicago. The computer we used there was called an M365; but it was really just an upgraded PDP-8. We used it to control lasers in order to trim electronic components to very precise values.</p>
<p>Forty four years later, in May of 2015, I started playing with a cute little Lua environment on my iPad called <a href="https://codea.io/">Codea</a>. I wrote several fun little programs, like lunar lander, etc. But then I thought: "Wouldn't it be fun to write a PDP-8 Emulator?"</p>
<p>A few days/weeks later I had a nice little PDP-8 emulator running on my iPad. I found some archived binary images of ancient paper tapes and managed to load them into my emulator. This allowed me to run the suite of development tools that I had used back in those early days.</p>
<p>Then Apple decided it didn't want people writing code on the Ipad that was not distributed through the App store, so they blocked the means by which Codea users could share source code. Indeed, I couldn't even move Lua source code to my new iPads. So the emulator was lost.</p>
<p>Fortunately I had put the last working version up on GitHub.</p>
<p>At some point, Apple reopened the channel, perhaps due to a court case. I discovered this a few weeks back, and loaded that old source code back into my iPad. It worked like a champ.</p>
<p>I made a few changes to deal with the bigger screen, and the faster processor, and then announced it on twitter. I think many people have played with it since.</p>
<blockquote>
<p><strong>You can get the emulator <a href="https://github.com/unclebob/PDP8EmulatorIpad">here</a>.</strong> You'll find a lot of good tutorial information, and several demonstration videos in that repository.</p>
</blockquote>
<h3 id="euler-4">Euler 4</h3>
<p>As you may know I have a <a href="https://www.youtube.com/playlist?list=PLmsuNLXeDr6Y1-a9ASu4mfxqDIgr-oaU6">youtube series</a> on the <a href="https://www.youtube.com/c/Cleancoders/playlists">cleancoders.com channel</a>, in which I walk through the problems in the <a href="https://projecteuler.net/">Euler project</a> solving them in Clojure and then taking them to the max, Myth-buster style.</p>
<p>Euler 4 is a simple little problem of finding the factors of palindromic numbers. I quickly solved it in Clojure, and then I thought it would be fun to write a PDP-8 program to solve it.</p>
<blockquote>
<p><em>Down the rathole I went.</em></p>
</blockquote>
<p>I used TDD to get the individual subroutines working. Among the subroutines I wrote were single and double precision multiply and divide routines. (We didn't use the word "functions" back then.) The poor PDP-8 could only add. It couldn't even subtract. Subtraction was accomplished by using twos-complement addition (let the reader understand;-)</p>
<p>Was this fun? Yes, at first it was kinda cool to reminisce, and to feel all the old knowledge and instincts come flooding back into my brain. But once the "novelty" wore off, it stopped being fun, and just turned into work -- grinding, tedious, work.</p>
<p>It took me several hours, over a period of a few days, but I got the blasted thing working. It's not an experience I'd like to repeat. Working on a PDP-8 is a <strong>PITA</strong>, even when with all the cheats I supply in my Emulator.</p>
<p>Here, for your edification, is my solution to Euler 4 on a PDP-8. This code solves the problem; but I'm quite sure it has some really nasty bugs anyway. I am in no way proud of this code. I'm just not willing to improve it. If you study it you'll see just how awful it is. I mean, among other sins I used truly naive algorithms for multiplying and dividing numbers.</p>
<p>Anyway, be careful. The lure of the rathole is very compelling.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>/EULER 4 SOLUTION
PZERO=20
\*200
MAIN, CLA
TLS
TAD SEED
ISZ SEED
CIA
JMS CALL
MKPAL
JMS CALL
PRDOT
CLA
TAD MAXFAC
DCA FAC
FACLUP,
CLA
TAD FAC
TAD K100
SMA CLA
JMP MAIN
JMS CALL
DLOAD
DPAL
TAD FAC
CIA
JMS CALL
ISFAC
SKP
JMP GOTFAC
CLA
TAD I OFP /OTHER FAC &gt; 999 TRY NEXT PAL.
TAD MAXFAC
SMA CLA
JMP MAIN
ISZ FAC
JMP FACLUP
GOTFAC,
CLA
TAD I OFP
TAD MAXFAC
SMA CLA
JMP MAIN
JMS CRLF
CLA
TAD FAC
CIA
JMS CALL
PRAC
JMS CALL
PRDOT
CLA
TAD I OFP
JMS CALL
PRAC
JMS CRLF
JMS CALL
DLOAD
DPAL
JMS CALL
PRDACC
JMS CRLF
HLT
DECIMAL
SEED, -999
MAXFAC, -999
OCTAL
FAC, 0
OFP, OTHFAC+1
\*400
/MAKE A PALINDROMIC NUMBER FROM A SEED.
/ABC-&gt;ABCCBA IN DECIMAL IN DACC AND STORED IN DPAL
MKPAL, 0
DCA DPAL+1
DCA DPAL
TAD DPAL+1
JMS CALL
DIV
K10
DCA WRK
TAD REM
DCA DIGS
TAD WRK
JMS CALL
DIV
K10
DCA DIGS+2
TAD REM
DCA DIGS+1
JMS CALL
DLOAD
DPAL
TAD K1000
JMS CALL
DMUL
JMS CALL
DSTORE
DPAL
CLA
TAD DIGS
JMS CALL
MUL
K10
TAD DIGS+1
JMS CALL
MUL
K10
TAD DIGS+2
DCA DWRK+1
DCA DWRK
JMS CALL
DLOAD
DPAL
JMS CALL
DADD
DWRK
JMS CALL
DSTORE
DPAL
JMP I MKPAL
/SKIP IF AC IS A FACTOR OF DACC. AC=0
ISFAC, 0
DCA DFAC+1
DCA DFAC
JMS CALL
DDIV
DFAC
JMS CALL
DSTORE
OTHFAC
JMS CALL
DLOAD
DREM
JMS CALL
DSKEQ
D0
SKP
ISZ ISFAC
JMP I ISFAC
DFAC, 0
0
OTHFAC, 0
0
OCTAL
DPAL, 0
0
DIGS, 0
0
0
WRK, 0
DWRK, 0
0
// PZERO FOR EULER
\*PZERO
DECIMAL
K100, 100
K1000, 1000
K10, 10
OCTAL
PZERO = .
~
\*1000
/DMATHLIB
/DLOAD - LOAD ARG INTO DACC, AC=0
DLOAD, 0
CLA
TAD I DLOAD
ISZ DLOAD
DCA DARGP
TAD I DARGP
DCA DACC
ISZ DARGP
TAD I DARGP
DCA DACC+1
JMP I DLOAD
/DOUBLE PRECISION STORE ACCUMULATOR POINTED TO BY ARG
DSTORE, 0
CLA
TAD I DSTORE
DCA DARGP
ISZ DSTORE
TAD DACC
DCA I DARGP
ISZ DARGP
TAD DACC+1
DCA I DARGP
JMP I DSTORE
/SKIP IF DOUBLE PRECISION ARGUMENT IS EQUAL TO DACC. AC=0
DSKEQ, 0
CLA
TAD I DSKEQ
DCA DARGP
ISZ DSKEQ
TAD DACC
CIA
TAD I DARGP
SZA CLA
JMP I DSKEQ
ISZ DARGP
TAD DACC+1
CIA
TAD I DARGP
SNA CLA
ISZ DSKEQ
JMP I DSKEQ
/DOUBLE PRECISION ADD ARGUMENT TO DACC. AC=0
DADD, 0
CLA CLL
TAD I DADD
ISZ DADD
DCA DARGP
TAD DARGP
IAC
DCA DARGP2
TAD I DARGP2
TAD DACC+1
DCA DACC+1
RAL
TAD I DARGP
TAD DACC
DCA DACC
JMP I DADD
/COMPLEMENT AND INCREMENT DACC
DCIA, 0
CLA CLL
TAD DACC+1
CMA IAC
DCA DACC+1
TAD DACC
CMA
SZL
IAC
DCA DACC
JMP I DCIA
/MULTIPY DACC BY AC
DMUL, 0
CIA
DCA PLIERD
JMS DSTORE
DCAND
JMS DLOAD
D0
TAD PLIERD
SNA CLA
JMP I DMUL
DMUL1, JMS DADD
DCAND
ISZ PLIERD
JMP DMUL1
JMP I DMUL
PLIERD, 0
DCAND, 0
0
/DIV DACC BY DARG (AWFUL) R IN DREM AC=0
DDIV, 0
CLA
TAD I DDIV
ISZ DDIV
DCA .+4
JMS DSTORE
DVDEND
JMS DLOAD
0
JMS DCIA /NEGATE DIVISOR
JMS DSTORE
DVSOR
JMS DLOAD
DVDEND
DCA DQUOT
DCA DQUOT+1
JMP DDIV1
DDIV2, ISZ DQUOT+1 // INCREMENT DQUOT
SKP
ISZ DQUOT
DDIV1, JMS DSTORE
DREM
JMS DADD
DVSOR
TAD DACC
SMA CLA
JMP DDIV2
JMS DLOAD
DQUOT
JMP I DDIV
DARGP, 0
DARGP2, 0
DVSOR, 0
0
DVDEND, 0
0
DQUOT, 0
0
/PAGE ZERO DATA FOR DMATHLIB
\*PZERO
DACC, 0
0
D0, 0
0
DREM, 0
0
PZERO=.
~
/SINGLE PRECISION MATH LIBRARY
\*2000
/DIVIDE AC BY ARGP (SLOW AND NAIVE)
/Q IN AC, R IN REM
DIV, 0
DCA REM
TAD I DIV
ISZ DIV
DCA ARGP
TAD I ARGP
CIA
DCA MDVSOR
DCA QUOTNT
TAD REM
DIVLUP, TAD MDVSOR
SPA
JMP DIVDUN
ISZ QUOTNT
JMP DIVLUP
DIVDUN, CIA
TAD MDVSOR
CIA
DCA REM
TAD QUOTNT
JMP I DIV
MDVSOR, 0
QUOTNT, 0
ARGP, 0
/MULTIPLY AC BY ARGP (SLOW AND NAIVE)
/GIVING SINGLE PRECISION PRODUCT IN AC
MUL, 0
DCA CAND
TAD I MUL
ISZ MUL
DCA ARGP
TAD I ARGP
SNA
JMP I MUL
CIA
DCA PLIER
TAD CAND
ISZ PLIER
JMP .-2
JMP I MUL
CAND, 0
PLIER, 0
/PZERO FOR SMATHLIB
\*PZERO
REM, 0
PZERO=.
~
/TTY UTILS
\*3000
/PRINT ONE CHAR IN AC. IF CR THEN PRINT LF.
PRTCHAR,0
TSF
JMP .-1
TLS
DCA CH
TAD CH
TAD MCR
SZA
JMP RETCHR
TAD KLF
TSF
JMP .-1
TLS
RETCHR, CLA
TAD CH
JMP I PRTCHAR
CH, 0
MCR, -215
/PRINT AC AS ONE DECIMAL DIGIT AC=0
PRDIG, 0
TAD K260
TSF
JMP .-1
TLS
CLA
JMP I PRDIG
K260, 260
/PRINT THE DACC IN DECIMAL
PRDACC, 0
JMS CALL
DSTORE
DACSV
JMS CALL
DDIV
D1E6
TAD DACC+1
JMS PRDIG
JMS CALL
DLOAD
DREM
JMS CALL
DDIV
D1E5
TAD DACC+1
JMS PRDIG
JMS CALL
DLOAD
DREM
JMS CALL
DDIV
D1E4
TAD DACC+1
JMS PRDIG
JMS CALL
DLOAD
DREM
JMS CALL
DDIV
D1E3
TAD DACC+1
JMS PRDIG
JMS CALL
DLOAD
DREM
JMS CALL
DDIV
D1E2
TAD DACC+1
JMS PRDIG
JMS CALL
DLOAD
DREM
JMS CALL
DDIV
D1E1
TAD DACC+1
JMS PRDIG
JMS CALL
DLOAD
DREM
TAD DACC+1
JMS PRDIG
JMS CALL
DLOAD
DACSV
JMP I PRDACC
DACSV, 0
0
D1E6, 0364
1100
D1E5, 0030
3240
D1E4, 2
3420
D1E3, 0
1750
D1E2, 0
144
D1E1, 0
12
/PRINT AC, AC=AC
PRAC, 0
DCA SAC
TAD SAC
JMS CALL
DIV
D1E3+1
JMS PRDIG
TAD REM
JMS CALL
DIV
D1E2+1
JMS PRDIG
TAD REM
JMS CALL
DIV
D1E1+1
JMS PRDIG
TAD REM
JMS PRDIG
TAD SAC
JMP I PRAC
SAC, 0
/PRINT DOT AC=AC
PRDOT, 0
DCA SAC
TAD KDOT
JMS TYPE
TAD SAC
JMP I PRDOT
/----------------------
/PZERO TEST LIBRARY
\*PZERO
TYPE, 0 / AC=0
TSF
JMP .-1
TLS
CLA
JMP I TYPE
CRLF, 0 / AC=0
CLA
TAD KCR
JMS TYPE
TAD KLF
JMS TYPE
JMP I CRLF
/SOUND BELL AND HALT WITH ADDR OF BAD TEST IN AC
ERROR, 0
CLA
TAD KBELL
JMS TYPE
CLA CMA
TAD ERROR
HLT
/PRINT DOT, COUNT ERROR
PASS, 0
CLA
TAD KDOT
JMS TYPE
ISZ TESTS
JMP I PASS
/TESTS COMPLETE, PRINT ZERO AND HALT WITH # OF TESTS IN AC.
TSTDUN,
JMS CRLF
TAD KZERO
JMS TYPE
JMS CRLF
TAD TESTS
HLT
/CALL SUBROUTINE
CALL, 0
DCA AC
TAD I CALL
DCA CALLEE
TAD CALL
IAC
DCA I CALLEE
ISZ CALLEE
TAD AC
JMP I CALLEE
AC, 0
CALLEE, 0
TESTS, 0
KZERO, 260
KBELL, 207
KCR, 215
KLF, 212
KDOT, 256
PZERO=.
~
$
</code></pre></div></div>

More On Types

2021-06-29T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2021/06/29/MoreOnTypes
<p>Recently I wrote a cute little program for doing <em>Turtle Graphics</em>. For those of you who don't know, turtle graphics were originally added to the LOGO language by Seymour Papert in the late 1960s. He built a robot that he called a "turtle" that could hold a pen. The robot had wheels and could move forwards and backwards, and could rotate left and right. It could also raise and lower the pen. When placed on a sheet of paper, the turtle could be commanded to draw interesting designs.</p>
<p>Papert's goal was to teach children about programming. As the years went by the robot got replaced with screens, and the turtle became an icon that could draw lines. Children from the 70s until now have been enthralled by the simple commands for directing the turtle, and the elegant drawings they can make.</p>
<p>For example, this is how you might draw a square:</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>forward 100
right 90
forward 100
right 90
forward 100
right 90
forward 100
right 90.
</code></pre></div></div>
<p>Recently I had a need to explore some interesting geometrical designs. Turtle graphics would be perfect for my purposes. So I wrote a turtle graphics processor in Clojure. <a href="https://github.com/unclebob/Euler/tree/main/e2\_Fibonacci/Turtle">[code]</a></p>
<p>I used the <a href="http://quil.info/"><code class="language-plaintext highlighter-rouge">quil</code></a> framework which is based on the <a href="http://processing.org"><code class="language-plaintext highlighter-rouge">Processing</code></a> framework in Java. This framework makes it very easy to create simple GUIs in Clojure.</p>
<p>Now consider the problem of the Turtle. What is the type model for this object? What fields does it have, and what constraints must be placed on those fields?</p>
<p>Here was my solution to that problem, written in <code class="language-plaintext highlighter-rouge">clojure/spec</code>. As usual, in Clojure, you start at the bottom and read towards the top.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(s/def ::position (s/tuple number? number?))
(s/def ::heading (s/and number? #(&lt;= 0 % 360)))
(s/def ::velocity number?)
(s/def ::distance number?)
(s/def ::omega number?)
(s/def ::angle number?)
(s/def ::weight (s/and pos? number?))
(s/def ::state #{:idle :busy})
(s/def ::pen #{:up :down})
(s/def ::pen-start (s/or :nil nil?
:pos (s/tuple number? number?)))
(s/def ::line-start (s/tuple number? number?))
(s/def ::line-end (s/tuple number? number?))
(s/def ::line (s/keys :req-un [::line-start ::line-end]))
(s/def ::lines (s/coll-of ::line))
(s/def ::visible boolean?)
(s/def ::speed (s/and int? pos?))
(s/def ::turtle (s/keys :req-un [::position
::heading
::velocity
::distance
::omega
::angle
::pen
::weight
::speed
::lines
::visible
::state]
:opt-un [::pen-start]))
</code></pre></div></div>
<p>Now don't freak out at all the parentheses and colons. In fact, for the moment, just ignore them.</p>
<p>So, what is a turtle? A turtle is a map whose required keys are as follows:</p>
<ul>
<li>
<p><code class="language-plaintext highlighter-rouge">position</code> is the cartesian coordinate of the pen of the turtle. If you look up towards the top you will see that a position is defined as a tuple containing two numbers.</p>
</li>
<li>
<p><code class="language-plaintext highlighter-rouge">heading</code> is the direction that the turtle is pointing. It will move in that direction if told to move forward. Again, looking up towards the top you can see that a heading must be a number between 0 and 360.</p>
</li>
<li>
<p><code class="language-plaintext highlighter-rouge">velocity</code> is a number that represents the speed at which the turtle will move across the screen. This is used for animation, so that the user can actually watch the turtle travel across the screen.</p>
</li>
<li>
<p><code class="language-plaintext highlighter-rouge">distance</code> is a number that represents the remaining distance that the turtle must traverse before the current command (either a <code class="language-plaintext highlighter-rouge">forward</code> or <code class="language-plaintext highlighter-rouge">backwards</code> command) is complete.</p>
</li>
<li>
<p><code class="language-plaintext highlighter-rouge">omega</code> is a number that represents the angular velocity of the turtle. Again, this is for animation purposes, so that the user can watch the turtle rotate when given a <code class="language-plaintext highlighter-rouge">right</code> or <code class="language-plaintext highlighter-rouge">left</code> command.</p>
</li>
<li>
<p><code class="language-plaintext highlighter-rouge">angle</code> is a number that represents the number of degrees remaining to complete the current rotation command.</p>
</li>
<li>
<p><code class="language-plaintext highlighter-rouge">pen</code> is the state of the pen. Looking up you can see that the state of the pen can be either <code class="language-plaintext highlighter-rouge">up</code> or <code class="language-plaintext highlighter-rouge">down</code>.</p>
</li>
<li>
<p><code class="language-plaintext highlighter-rouge">weight</code> is a positive number that represents the thickness of the line drawn by the pen.</p>
</li>
<li>
<p><code class="language-plaintext highlighter-rouge">speed</code> is a positive integer that acts as a multiplier for both the <code class="language-plaintext highlighter-rouge">velocity</code> and <code class="language-plaintext highlighter-rouge">omega</code> parameters. This allows the user to speed up or slow down the animation.</p>
</li>
<li>
<p><code class="language-plaintext highlighter-rouge">lines</code> is a list of all the lines drawn by the turtle so far. Looking up you can see that it is a collection of lines, and that lines are maps whose required keys are <code class="language-plaintext highlighter-rouge">line-start</code> and <code class="language-plaintext highlighter-rouge">line-end</code>, both of which are tuples of two numbers. (Yes, I suppose I should have created a <code class="language-plaintext highlighter-rouge">point</code> type.)</p>
</li>
<li>
<p><code class="language-plaintext highlighter-rouge">visible</code> is a boolean that determines whether the turtle itself should be visible while it is being animated. If this is false, then all the user sees is the animated result of the turtle's movements.</p>
</li>
<li>
<p><code class="language-plaintext highlighter-rouge">state</code> is either <code class="language-plaintext highlighter-rouge">busy</code> or <code class="language-plaintext highlighter-rouge">idle</code>. This is used by the command processor. When the turtle goes from <code class="language-plaintext highlighter-rouge">busy</code> to <code class="language-plaintext highlighter-rouge">idle</code> the next command is pulled from the command queue and executed.</p>
</li>
</ul>
<p>It should be clear that this is a type model. Most statically typed languages would not be able to capture all the constraints within this type model; though there are perhaps some that could. However, this is not a static type model. Clojure is not a statically typed language. <code class="language-plaintext highlighter-rouge">clojure/spec</code> is a dynamic type definition language.</p>
<p>What does that mean? Probably the best way to explain that is to show you where that type model gets invoked. Here's a simple example.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(defn make []
{:post [(s/assert ::turtle %)]}
{:position [0.0 0.0]
:heading 0.0
:velocity 0.0
:distance 0.0
:omega 0.0
:angle 0.0
:pen :up
:weight 1
:speed 5
:visible true
:lines []
:state :idle})
</code></pre></div></div>
<p>This is the default constructor of the turtle. Notice that it just loads up all the required fields into a map. Notice also that there is a <em>post condition</em> that asserts that the result conforms the the <code class="language-plaintext highlighter-rouge">turtle</code> type.</p>
<p>This is nice. If I forget to initialize a field, or if I initialize a field to a value that conflicts with the type, I get an error.</p>
<p>Here's another, more complex example. Don't freak out, you don't have to understand this in detail.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(defn update-turtle [turtle]
{:post [(s/assert ::turtle %)]}
(if (= :idle (:state turtle))
turtle
(let [{:keys [distance
state
angle
lines
position
pen
pen-start] :as turtle}
(-&gt; turtle
(update-position)
(update-heading))
done? (and (zero? distance)
(zero? angle))
state (if done? :idle state)
lines (if (and done? (= pen :down))
(conj lines (make-line turtle))
lines)
pen-start (if (and done? (= pen :down))
position
pen-start)]
(assoc turtle :state state :lines lines :pen-start pen-start)))
)
</code></pre></div></div>
<p>This is the function that updates the turtle for each screen refresh. Again, notice the <em>post condition</em>. If anything is calculated incorrectly by the <code class="language-plaintext highlighter-rouge">update-turtle</code> function, I'll get an exception right away.</p>
<p>Now some of you might be worried that by checking types at runtime I could end up with runtime errors in production. You might therefore assert that static typing is better because the compiler checks the types long before the program ever executes.</p>
<p>However, I do not intend to have runtime errors in production, because I have a suite of tests that exercise all the behaviors of the system. Here's just one of those tests:</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(describe "Turtle Update"
(with turtle (-&gt; (t/make) (t/position [1.0 1.0]) (t/heading 1.0)))
(context "position update"
(it "holds position when there's no velocity"
(let [turtle (-&gt; @turtle (t/velocity 0.0) (t/state :idle))
new-turtle (t/update-turtle turtle)]
(should= turtle new-turtle)))
</code></pre></div></div>
<p>Again, you don't have to understand this in any detail. Just notice that the <code class="language-plaintext highlighter-rouge">make</code> and <code class="language-plaintext highlighter-rouge">update-turtle</code> functions are being invoked. Since those functions have <em>post conditions</em> that will check the types, and since my suite of tests is exhaustive, I am quite certain that there will be no runtime errors in production and that my dynamic type checking is as robust as any static type system.</p>
<p>The dynamic nature of the type checking allows me to assert type constraints that are very difficult, if not impossible, to assert at compile time. I can, for example, assert complex relationships between the values of the fields.</p>
<p>To expand on that example, imagine the type model of an accounting balance sheet. The sum of the assets, liabilities and equities on the balance sheet must be zero. This is easy to assert in <code class="language-plaintext highlighter-rouge">clojure/spec</code> but is difficult, if not impossible, to assert in most statically typed languages.</p>
<p>Moreover, <em>I</em> get to control when types are asserted. It is up to me to decide if and when a certain type should be checked. This gives me a lot of power and flexibility. It allows me to violate the type rules in the midst of computations, so long as the end result ends up conforming to the types.</p>
<p>One last point. In the late 90s and the 2000s, there was a lengthy and animated (and sometimes acrimonious) debate over TDD vs DBC (Design by Contract). What <code class="language-plaintext highlighter-rouge">clojure/spec</code> has taught me is that the two play very well together, and both should be in every programmer's toolkit.</p>

On Types

2021-06-25T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2021/06/25/OnTypes
<p>I wrote my first program in 1964. The name of the program was: <em>Mr Patternson's Computerized Gate</em>, and it was implemented on a little plastic computer named DIGICOMP-I, which was a cute little three bit finite state machine with 6 AND gates.</p>
<p>The first electronic computer I ever wrote a program for was an ECP-18 in 1966. This was a 15 bit wide machine with 1024 words of <em>drum</em> memory. The programs I wrote were all in binary machine language and were entered through the front-panel switches.</p>
<p>In the years between 1967 and 1969 my father would drive my friend, Tim Conrad, and I 25 miles to the Digital Equipment Corp sales office, where we would spend our Saturdays entering programs into the PDP-8 that they had on the floor. They were very gracious to allow us such access and freedom. The code we wrote was in PAL-D assembler (which was written by Ed Yourdon when he was 21 years old).</p>
<p>My very first job as a programmer was temporary. A matter of two weeks. I was 17, and the year was 1969. My father went to the CEO of a nearby insurance actuarial firm, ASC Tabulating, and in his inimitable fashion, told them that they would be hiring me for a summer job. He had a way of being <em>very</em> convincing.</p>
<p>The program I wrote for ASC was named IDSET. It was written in Honeywell H200 assembler (the language was called Easycoder and was based on IBM 1401 Autocoder). The purpose was to read student records from a magnetic tape and insert ID codes into those records, and then write them out onto a new tape. With some coaching, I was able to get that program to work.</p>
<p>Upon graduating High School, in 1971, I got a job at ASC again; but this time as a third-shift off-line printer operator. We were printing junk mail, which was a brand new thing back then.</p>
<p>A few months later I was hired as a full-time programmer analyst at ASC, and was assigned to work on huge re-write of a massive accounting and records system for Local 705 Trucker's union in Chicago. The existing system ran on a great big GE Datanet 30. ASC wanted to reimplement it on a Varian 620F mini-computer.</p>
<p>The 620F was a lovely little 16 bit computer with 32K of core memory and a 1us cycle time. The primary IO devices were a teletype, a slow card reader, two magnetic tape drives, and two 2314 20MB disks. The machine also had 16 (or was it 32) RS232 ports for talking to teletypes that were remotely connected through 300BPS modems.</p>
<p>Although the 620F came with a stand-alone assembler, there was no operating system. So every bit of that real time union accounting system was built from assembler code, with no frameworks, platforms, or operating systems to help.</p>
<p>In 1973 I took a job at Chicago Laser Systems, programming a PDP-8-like machine, in assembler, to control pulsed lasers, galvonometer driven mirrors, and step-and-repeat tables to trim electronic components to high degrees of tolerance.</p>
<p>In 1975 I took a job at Outboard Marine Corporation, programming a real time aluminum die cast system in IBM System 7 assembler.</p>
<p>In 1977 I took a job at Teradyne Central, programming a PDP-8-like machine, in assembler (again), to control a distributed system for testing and monitoring the quality of all the telephone lines in a telephone company service area. A year later we started using 8085 micro-computers and wrote all that code in assembler too.</p>
<p>Suffice it to say that I was steeped in assembler, and thought that all high-level languages were a joke. My forays into COBOL, Fortran, and PL/1 did not convince me otherwise. Real programmers programmed in assembler.</p>
<p>Between 1977 and 1980 I was introduced to Pascal. I rejected it as a viable language almost immediatly. I found the type system far too constraining, and didn't trust all the magic behind the scenes.</p>
<p>In 1980 I read a copy of Kernighan and Ritchie, and for the first time I began to see that a high-level language could possibly be an appropriate engineering language. I spent many years writing in that wonderful language which, by the way, was as untyped as assembler.</p>
<p>Oh, that's not to say that C didn't have declared types. It's just that the compiler didn't bother to check that you were using those types properly. This made the language untyped for all intents and purposes.</p>
<p>In 1986, after several nightmare scenarios having to do with the typlessness of C, I was an enthusiastic early adopter of C++. Unfortunately I could not get my hands on a C++ compiler until 1987. I became quite an expert in the languge, and engaged in many (many (many)) arguments on comp.lang.c++ and comp.object (in those heady days of USENET, a very early social networking platform).</p>
<p>C++ is a statically typed language. Many, today, would consider it to be relatively weakly typed; but from my point of view, after a decade and a half of untyped languages, I thought the type enforcement was very strong. I had overcome the feeling of being handcuffed by a strong type system and became quite adept at building type models.</p>
<p>In 1990 I took a contracting job at Rational, working in C++ on the first release of Rational Rose. This is where I met Grady Booch, and came up with the plan for my first book.</p>
<p>By 1991 I was a consultant, selling my services to companies, all over the US and Europe, who wanted to learn about object-oriented programming and C++. It was a lucrative affair for me, and I continued building that business for several years. Eventually I became the editor-in-chief of <em>The C++ Report</em> (does anybody remember print magazines?)</p>
<p>In 1999 I realized that C++ was a waning technolgy, and that the action was really happening in Java. Java was similar enough to C++ for me to make the transition with relative ease. The type system of Java was a bit weaker than C++, and I refused to use the stronger features (like <code class="language-plaintext highlighter-rouge">final</code> though I had been an avid consumer of <code class="language-plaintext highlighter-rouge">const</code> in C++).</p>
<p>By 2003 I had grown tired of Java's static type system and started playing around with Python. I found the language to be primitive and somewhat haphazard; so after a few excursions with the language I switched to Ruby.</p>
<p>In Ruby I found a home for several years. The dynamic type system was robust. The object-oriented facilities were well thought through and very easy to use. It was an elegant language with very few warts.</p>
<p>Then, in 2010 or so, I bumped into Clojure. I had just recently read <a href="https://mitpress.mit.edu/sites/default/files/sicp/index.html"><em>The Structure and Interpretation of Computer Programs</em></a> and so was interested in playing around with a LISP derivative.</p>
<p>It has been 11 years now, and I feel no urge to change languages. I reckon that Clojure may be my last programming language. Oh, not that I haven't looked around. I've had some daliances with Golang, Elixr, and Kotlin, and have looked with trepidation at Haskel. I've even played with Scala and F#. I keep looking as new languages arise; but have found nothing that calls me to switch away from Clojure.</p>
<p>Notice the pathway of my career. I went from untyped languages like assembler and C, to statically typed languages like C++ and Java, to dynamically typed languages like Python and Ruby, and now to Clojure.</p>
<p>The type system in Clojure is as dynamic as Python or Ruby, but there is a library in Clojure called <code class="language-plaintext highlighter-rouge">clojure/spec</code> that provides all the strong typing anyone would ever need. However, instead of that typing being controlled by the compiler, it is controlled by <em>me</em>. I can enforce simple types, or very complex data relationships. You might think of it as a kind of pre-condition/post-condition language. Eifel programmers would feel very much at home with it. It's an almost perfect way to engage in Design by Contract.</p>
<p>So what do I conclude from this? Not much other than that static typing is not for me. I prefer the flexibility of dynamic typing, and the ability to enforce types if, and when, I need such enforcement.</p>

if-else-switch

2021-03-06T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2021/03/06/ifElseSwitch
<p>A few days ago someone tweeted a question asking which of the following PHP snippets was better than the others, or whether there might be an even better approach.</p>
<p><img src="/assets/ifElseSwitch.jpg" /></p>
<p>I tweeted my answer in the following cryptic paragraph.</p>
<blockquote>
<p><em>Place the if/else cases in a factory object that creates a polymorphic object for each variant. Create the factory in ‘main’ and pass it into your app. That will ensure that the if/else chain occurs only once.</em></p>
</blockquote>
<p>Others have since asked me for an example. Twitter is not the best medium for that so…</p>
<p>Firstly, if the sole intent of the programmer is to translate:</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>0-&gt;'male',
1-&gt;'female'
otherwise -&gt; 'unknown'
</code></pre></div></div>
<p>…then his refactoring #2 would be my preference.</p>
<p>However, I have a hard time believing that the business rules of the system are not using that gender code for making policy decisions. My fear is that the <code class="language-plaintext highlighter-rouge">if/else/switch</code> chain that the author was asking about is replicated in many more places within the code. Some of those <code class="language-plaintext highlighter-rouge">if/else/switch</code> statements might switch on the integer, and others might switch on the string. It’s not inconceivable that you’d find a <code class="language-plaintext highlighter-rouge">if/else/switch</code> that used an integer in one case and a string in the next!</p>
<p>The proliferation of <code class="language-plaintext highlighter-rouge">if/else/switch</code> statements is a common problem in software systems. The fact that they are replicated in many places is problematic because when such statements are inevitably changed, it is easy to miss some. This leads to fragile systems.</p>
<p>But there is a worse problem with <code class="language-plaintext highlighter-rouge">if/else/switch</code> statements. It’s the dependency structure.</p>
<p><img src="/assets/ifElseSwitchStructure.jpg" /></p>
<p>Such statements tend to have cases that point outwards towards lower level modules. This often means that the module containing the <code class="language-plaintext highlighter-rouge">if/else/switch</code> will have source code dependencies upon those lower level modules.</p>
<p>That’s bad enough. We don’t like dependencies that run from high level modules to low level modules. They thwart our desire to create architectures that are made up of independently deployable components.</p>
<p>However, the above diagram shows that it’s worse than that. Other higher level modules tend to depend on the modules that contains those <code class="language-plaintext highlighter-rouge">if/else/switch</code> statements. Those higher level modules, therefore, have transitive dependencies upon the lower level modules. This turns the <code class="language-plaintext highlighter-rouge">if/else/switch</code> statements into <em>dependency magnets</em> that reach across large swathes of the system source code, binding the system into a tight monolithic architecture without a flexible component structure.</p>
<p>The solution to this problem is to break those outwards dependencies on the lower level modules. This can be done with simple polymorphism.</p>
<p><img src="/assets/ifElseSwitchPolymorphism.jpg" /></p>
<p>In the diagram above you can see the high level modules using a base class interface that polymorphically deploys to the low level details. With a little thought you should be able to see that this is behaviorally identical to the <code class="language-plaintext highlighter-rouge">if/else/switch</code> but with a twist. The decision about which case to follow must have been made before those high level policy modules invoked the base class interface.</p>
<p>We’ll come back to <em>when</em> that decision is made in a moment. For now, just look at the direction of the dependencies. There is no longer any transitive source code dependency from the high level modules to the low level modules. We could easily create a component boundary that separates them. We could even deploy the high level modules independently from the low level modules. This makes for a pleasantly flexible architecture.</p>
<p>Another point to consider is that the <code class="language-plaintext highlighter-rouge">if/else/switch</code> and the polymorphic implementations both use table lookups to do their work. In the case of an <code class="language-plaintext highlighter-rouge">if/else</code> the table lookup is procedural. In the case of a <code class="language-plaintext highlighter-rouge">switch</code> most compilers build a little lookup table. In the case of the polymorphic dispatch the vector table is built into the base class interface. So all three have very similar runtime and memory characteristics. One is not much faster than another.</p>
<p>So where does the decision get made? The decision is made when the instance of the base class is created. Hopefully that creation happens in a nice safe place like <code class="language-plaintext highlighter-rouge">main</code>. Usually we manage that with a simple factory class.</p>
<p><img src="/assets/ifElseSwitchFactory.jpg" /></p>
<p>In the diagram above you can see the high level module uses the base class to do its work. Every business rule that would once have depended on an <code class="language-plaintext highlighter-rouge">if/else/switch</code> statement now has its own particular method to call in the base class. When a business rule calls that method, it will deploy down to the proper low level module. The low level module is created by the <code class="language-plaintext highlighter-rouge">Factory</code>. The high level module invokes the <code class="language-plaintext highlighter-rouge">make(x)</code> method of the <code class="language-plaintext highlighter-rouge">Factory</code> passing some kind of token <code class="language-plaintext highlighter-rouge">x</code> that represents the decision. The <code class="language-plaintext highlighter-rouge">FactoryImpl</code> contains the sole <code class="language-plaintext highlighter-rouge">if/else/switch</code> statement, which creates the appropriate instance and passes it back to the high level module which then invokes it.</p>
<p>Note, again, the direction of the dependencies. See that red line? That’s a nice convenient component boundary. All dependencies cross it pointing towards the higher level modules.</p>
<p>Be careful with that token <code class="language-plaintext highlighter-rouge">x</code>. Don’t try to make it an <code class="language-plaintext highlighter-rouge">enum</code> or anything that requires a declaration above the red line. An integer, or a string is a better choice. It may not be type safe. Indeed, it <em>cannot</em> be type safe. But it will allow you to preserve the component structure of your architecture.</p>
<p>You may well be concerned about a different matter. That base class needs a method for every business rule that once depended upon the <code class="language-plaintext highlighter-rouge">if/else/switch</code> decision. As more of those business rules appear, you’ll have to add more methods to the base class. And since many business rules already depend upon the base class they’ll have to be recompiled/redeployed even though nothing they care about changed.</p>
<p>There are many ways to resolve that problem. I could keep this blog going for another 2,000 words or so describing them. To avoid that I suggest you look up <em>The Interface Segregation Principle</em> and the <em>Acyclic Visitor</em> pattern.</p>
<p>Anyway, isn’t it fascinating how interesting a discussion of a simple <code class="language-plaintext highlighter-rouge">if/else/switch</code> can be?</p>

Pairing Guidelines

2021-01-17T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2021/01/17/Pairing
<p>Everybody pairs from time to time. It is a rare programmer who has not sat down with another programmer to look something over or help find a bug.</p>
<p>Deep problems, that require much heavy thinking, do not often lend themselves to pairing. The interaction between the programmers tends to disrupt the necessary concentration.</p>
<p>On the other hand, it is not uncommon for programmers to get caught in a problem that they think is deep, but for which there is a much simpler solution that another programmer could quickly see. So it is wise to start deep problems with a pair, or even a mob, but then break it up when it becomes clear that the problem is irreducible.</p>
<p>On the other side of the spectrum, there is no good reason to pair on trivial matters. Fleshing out a list of error messages, or loading fifty fields into a form are relatively mindless activities that do not require the scrutiny afforded by pairing.</p>
<p>Then there is the vast middle. This is where pairing/mobbing are most valuable. These are problems that are non-trivial, but also not particularly deep. This is 90% of all programming. Pairing on this type of code keeps that code well tested, well structured, and as simple as possible.</p>
<p>Pairing should always be voluntary, never be forced, never be scheduled by a manager, and never tracked. It is an informal process that is entirely under the control of the individual programmers.</p>
<p>Some people can’t, or won’t do it. That’s ok; but it may require that their participation in certain projects be curtailed.</p>
<p>Pairing sessions should be short-ish. 20-40 minutes at a time. (<a href="https://en.wikipedia.org/wiki/Pomodoro\_Technique">Tomato</a> sized) With no more than three or four consecutive sessions of that length. This is not a rule, just an informal guideline.</p>
<p>Not all code that would benefit from pairing, should be written by pairs. A mature team might pair 50% of the time, or even less. During the pairing sessions, a large amount of code will be reviewed; far more than the pair is actively writing; and thus the benefits of pairing will be seen in very large swathes of non-paired code.</p>
<p>Bottom line: Don’t be a jerk. Pair sometimes, don’t pair other times. Pair enough so that you have a good grasp of the overall system, and know enough of what your teammates are doing that you could step into their roles if the need arose. Don’t pair so much that you hate your job, and your teammates.</p>

Solid Relevance

2020-10-18T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance
<p>Recently I received a letter from someone with a concern. It went like this:</p>
<hr />
<blockquote>
<p><em>For years the knowledge of the SOLID principle has been a standard part of our recruiting procedure. Candidates were expected to have a good working knowledge of these principles. Lately, however, one of our managers, who doesn’t code much anymore, has questioned whether that is wise. His points were that the Open-Closed principle isn’t very important anymore because most of the code we write isn’t contained in large monoliths and making changes to small microservices is safe and easy. The Liskov Substitution Principle is long out of date because we don’t focus on inheritance nearly as much as we did 20 years ago. I think we should consider <a href="https://speakerdeck.com/tastapod/why-every-element-of-solid-is-wrong">Dan North’s position on SOLID</a> – “Just write simple code.”</em></p>
</blockquote>
<hr />
<p>I wrote the following letter in response:</p>
<p>The SOLID principles remain as relevant to day as they were in the 90s (and indeed before that). This is because software hasn’t changed all that much in all those years — and <strong>that</strong> is because software hasn’t change all that much since 1945 when Turing wrote the first lines of code for an electronic computer. Software is still <code class="language-plaintext highlighter-rouge">if</code> statements, <code class="language-plaintext highlighter-rouge">while</code> loops, and assignment statements — <em>Sequence</em>, <em>Selection</em>, and <em>Iteration</em>.</p>
<p>Every new generation likes to think that their world is vastly different from the generation before. Every new generation is wrong about that; which is something that every new generation learns once the next new generation comes along to tell them how much everything has changed. <code class="language-plaintext highlighter-rouge">&lt;grin&gt;</code></p>
<p>So let’s walk through the principles, one by one.</p>
<p><strong>SRP</strong>) The Single Responsibility Principle.</p>
<blockquote>
<p><em>Gather together the things that change for the same reasons. Separate things that change for different reasons.</em></p>
</blockquote>
<p>It is hard to imagine that this principle is not relevant in software. We do not mix business rules with GUI code. We do not mix SQL queries with communications protocols. We keep code that is changed for different reasons separate so that changes to one part to not break other parts. We make sure that modules that change for different reasons do not have dependencies that tangle them.</p>
<p>Microservices do not solve this problem. You can create a tangled microservice, or a tangled set of microservices if you mix code that changes for different reasons.</p>
<p>Dan North’s slides completely miss the point on this, and convinces me that he did not understand the principle at all. (or that he was being ironic, which knowing Dan, is far more likely) His answer to the SRP is to “Write Simple Code”. I agree. The SRP is one of the ways we keep the code simple.</p>
<p><strong>OCP</strong>) The Open-Closed Principle.</p>
<blockquote>
<p><em>A Module should be open for extension but closed for modification.</em></p>
</blockquote>
<p>Of all the principles, the idea that anyone would question this one fills me full of dread for the future of our industry. Of course we want to create modules that can be extended without modifying them. Can you imagine working in a system that did not have device independence, where writing to a disk file was fundamentally different than writing to a printer, or a screen, or a pipe? Do we want to see <code class="language-plaintext highlighter-rouge">if</code> statement scattered through our code to deal with all the little details?</p>
<p>Or… Do we want to separate abstract concepts from detailed concepts. Do we want to keep business rules isolated from the nasty little details of the GUI, and the micro-service communications protocols, and the arbitrary behaviors of the database? Of course we do!</p>
<p>Again, Dan’s slide gets this completely wrong. When requirements change only <em>part</em> of the existing code is wrong. Much of the existing code is still right. And we want to make sure that we don’t have to change the right code just to make the wrong code work again. Dan’s answer is “write simple code”. Again, I agree. And, ironically, he is right. <em>Simple code is both open and closed</em>.</p>
<p><strong>LSP</strong>) The Liskov Substitution Principle.</p>
<blockquote>
<p><em>A program that uses an interface must not be confused by an implementation of that interface.</em></p>
</blockquote>
<p>People (including me) have made the mistake that this is about inheritance. It is not. It is about sub-typing. All implementations of interfaces are subtypes of an interface. All duck-types are subtypes of an implied interface. And, every user of the base interface, whether declared or implied, must agree on the meaning of that interface. If an implementation confuses the user of the base type, then <code class="language-plaintext highlighter-rouge">if/switch</code> statements will proliferate.</p>
<p>This principle is about keeping abstractions crisp and well-defined. It is impossible to believe that this is an outmoded concept.</p>
<p>Dan’s slides are entirely correct on this topic; he simply missed the point of the principle. Simple code is code that maintains crisp subtype relationships.</p>
<p><strong>ISP</strong>) The Interface Segregation Principle.</p>
<blockquote>
<p><em>Keep interfaces small so that users don’t end up depending on things they don’t need.</em></p>
</blockquote>
<p>We still work with compiled languages. We still depend upon modification dates to determine which modules should be recompiled and redeployed. So long as this is true we will have to face the problem that when module A depends on module B at <em>compile</em> time, but not at run time, then changes to module B will force recompilation and redeployment of module A.</p>
<p>This issue is especially acute in statically typed languages like Java, C#, C++, GO, Swift, etc. Dynamicaly typed languages are affected much less; but are still not immune. The existence of Maven and Leiningen are proof of that.</p>
<p>Dan’s slide on this topic is provably false. Clients <em>do</em> depend on methods they don’t call, if they have to be recompiled and redeployed when one of those methods is modified. Dan’s final point on this principle is fine, so far as it goes. Yes, if you can split a class with two interfaces into two separate classes, then it is a good idea to do so (SRP). But such separation is often not feasible, nor even desirable.</p>
<p><strong>DIP</strong>) The Dependency Inversion Principle.</p>
<blockquote>
<p><em>Depend in the direction of abstraction. High level modules should not depend upon low level details.</em></p>
</blockquote>
<p>It is hard to imagine an architecture that does not make significant use of this principle. We do not want our high level business rules depending upon low level details. I hope that is perfectly obvious. We do not want the computations that make money for us polluted with SQL, or low level validations, or formatting issues. We want isolation of the high level abstractions from the low level details. That separation is achieved by carefully managing the dependencies within the system so that all source code dependencies, especially those that cross architectural boundaries, point towards high level abstractions, not low level details.</p>
<p>In every case Dan’s slides end with: <em>Just write simple code</em>. This is good advice. However, if the years have taught us anything it is that simplicity requires disciplines guided by principles. It is those principles that define simplicity. It is those disciplines that constrain the programmers to produce code that leans towards simplicity.</p>
<p>The best way to make a complicated mess is to tell everyone to “just be simple” and give them no further guidance.</p>

Loopy

2020-09-30T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2020/09/30/loopy
<p>The following is a segment of a journey. It has no obvious beginning point, nor does it actually end up anywhere. The value, if any, is in the journey itself.</p>
<p>The code below is the standard solution to the <a href="http://butunclebob.com/ArticleS.UncleBob.ThePrimeFactorsKata">Prime Factors Kata</a>.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>public List&lt;Integer&gt; factorsOf(int n) {
ArrayList&lt;Integer&gt; factors = new ArrayList&lt;&gt;();
for (int d = 2; n &gt; 1; d++)
for (; n % d == 0; n /= d)
factors.add(d);
return factors;
}
</code></pre></div></div>
<p>However, I was doing this kata in Clojure the other day and I wound up with a different solution. It looked like this:</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(defn prime-factors [n]
(loop [n n d 2 factors []]
(if (&gt; n 1)
(if (zero? (mod n d))
(recur (/ n d) d (conj factors d))
(recur n (inc d) factors))
factors)))
</code></pre></div></div>
<p>The algorithm is pretty much the same. I mean if you tracked the value of <code class="language-plaintext highlighter-rouge">n</code>, <code class="language-plaintext highlighter-rouge">d</code>, and <code class="language-plaintext highlighter-rouge">factors</code> they would go through the same changes. On the other hand the code in Java is a doubly nested loop; but the code in Clojure is a single recursive loop with two recursion points. That’s interesting.</p>
<p>I could write the recursive algorithm in Java like this:</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code> private List&lt;Integer&gt; factorsOf(int n) {
return factorsOf(n, 2, new ArrayList&lt;Integer&gt;());
}
private List&lt;Integer&gt; factorsOf(int n, int d, List&lt;Integer&gt; factors) {
if (n&gt;1) {
if (n%d == 0) {
factors.add(d);
return factorsOf(n/d, d, factors);
} else {
return factorsOf(n, d+1, factors);
}
}
return factors;
}
</code></pre></div></div>
<p>And then, since this is tail recursive, I could rewrite it as a straight loop.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code> private List&lt;Integer&gt; factorsOf(int n, int d, List&lt;Integer&gt; factors) {
while (true) {
if (n &gt; 1) {
if (n % d == 0) {
factors.add(d);
n /= d;
} else {
d++;
}
} else
return factors;
}
}
</code></pre></div></div>
<p>For all intents and purposes this code executes the same algorithm as the standard solution; but it does not have a doubly nested loop. We have transformed the code from a doubly nested loop, to a single loop, without affecting the algorithm.</p>
<p>Is this always possible?</p>
<p>In other words: given a program with a nested loop, is there a way to write the same program with a single loop?</p>
<p>The answer to that is: <em>Yes.</em></p>
<p>The fact that a bit of code executes within an inner loop could be encoded into a state variable. The outer loop could then dispatch to that bit of code depending upon how that state variable is set.</p>
<p>We see that in the code above. The state condition for the inner loop is <code class="language-plaintext highlighter-rouge">n%d==0</code>. Indeed, I can extract that out as a <a href="https://moderatemisbehaviour.github.io/clean-code-smells-and-heuristics/general/g19-use-explanatory-variables.html">explanatory variable</a> to make my point clearer. I can also extract <code class="language-plaintext highlighter-rouge">n&gt;1</code>.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code> private List&lt;Integer&gt; factorsOf(int n, int d, List&lt;Integer&gt; factors) {
while (true) {
boolean factorsRemain = n &gt; 1;
boolean currentDivisorIsFactor = n % d == 0;
if (factorsRemain) {
if (currentDivisorIsFactor) {
factors.add(d);
n /= d;
} else {
d++;
}
} else
return factors;
}
}
</code></pre></div></div>
<p>Now all the looping decisions are made at the very top; and the <code class="language-plaintext highlighter-rouge">if</code> statements simply dispatch the flow of control to the right bits of code.</p>
<p>That nested <code class="language-plaintext highlighter-rouge">if</code> is a bit annoying. Let’s replace all that nesting with appropriate logic.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code> private List&lt;Integer&gt; factorsOf(int n, int d, List&lt;Integer&gt; factors) {
while (true) {
boolean factorsRemain = n &gt; 1;
boolean currentDivisorIsFactor = n % d == 0;
if (factorsRemain &amp;&amp; currentDivisorIsFactor) {
factors.add(d);
n /= d;
}
if (factorsRemain &amp;&amp; !currentDivisorIsFactor)
d++;
if (!factorsRemain)
return factors;
}
}
</code></pre></div></div>
<p>Now we have a nice outer loop that fully determines the execution path up front, and then selects the appropriate paths with a sequence of <code class="language-plaintext highlighter-rouge">if</code> statements with no <code class="language-plaintext highlighter-rouge">else</code> clauses.</p>
<p>Indeed, we can improve upon this just a little bit more by using more explanatory variables to explicitly name those paths.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code> private List&lt;Integer&gt; factorsOf(int n, int d, List&lt;Integer&gt; factors) {
while (true) {
boolean factorsRemain = n &gt; 1;
boolean currentDivisorIsFactor = n % d == 0;
boolean factorOutCurrentDivisor = factorsRemain &amp;&amp;
currentDivisorIsFactor;
boolean tryNextDivisor = factorsRemain &amp;&amp; !currentDivisorIsFactor;
boolean allDone = !factorsRemain;
if (factorOutCurrentDivisor) {
factors.add(d);
n /= d;
}
if (tryNextDivisor) {
d++;
}
if (allDone)
return factors;
}
}
</code></pre></div></div>
<p>I think I can make this more interesting by using an <code class="language-plaintext highlighter-rouge">enum</code> and a <code class="language-plaintext highlighter-rouge">switch</code>.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code> private enum State {Starting, Factoring, Searching, Done}
private List&lt;Integer&gt; factorsOf(int n, int d, List&lt;Integer&gt; factors) {
State state = State.Starting;
while (true) {
boolean factorsRemain = n &gt; 1;
boolean currentDivisorIsFactor = n % d == 0;
if (factorsRemain &amp;&amp; currentDivisorIsFactor)
state = State.Factoring;
if (factorsRemain &amp;&amp; !currentDivisorIsFactor)
state = State.Searching;
if (!factorsRemain)
state = State.Done;
switch (state) {
case Factoring:
factors.add(d);
n /= d;
break;
case Searching:
d++;
break;
case Done:
return factors;
}
}
}
</code></pre></div></div>
<p>Now let’s move the determination of the <em>next</em> state into each case.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code> private List&lt;Integer&gt; factorsOf(int n, int d, List&lt;Integer&gt; factors) {
State state = State.Starting;
while (true) {
switch (state) {
case Starting:
if (n == 1)
state = State.Done;
else if (n % d == 0)
state = State.Factoring;
else
state = State.Searching;
break;
case Factoring:
factors.add(d);
n /= d;
if (n == 1)
state = State.Done;
else if (n % d != 0)
state = State.Searching;
break;
case Searching:
d++;
if (n == 1)
state = State.Done;
else if (n % d == 0)
state = State.Factoring;
break;
case Done:
return factors;
}
}
}
</code></pre></div></div>
<p>Ugh. I think we can improve upon this by moving a few things around and gettting rid of those explanatory variables.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code> private List&lt;Integer&gt; factorsOf(int n, int d, List&lt;Integer&gt; factors) {
State state = State.Starting;
while (true) {
switch (state) {
case Starting:
break;
case Factoring:
factors.add(d);
n /= d;
break;
case Searching:
d++;
break;
case Done:
return factors;
}
if (n == 1)
state = State.Done;
else if (n % d == 0)
state = State.Factoring;
else
state = State.Searching;
}
}
</code></pre></div></div>
<p>OK, So now the whole thing has been changed into a <a href="https://en.wikipedia.org/wiki/Moore\_machine">Moore</a> model finite state machine. The state transition diagram looks like this.</p>
<p><img src="/assets/loopy/fsm.jpg" width="300" /></p>
<p>If you look closely you can see the nested loops in that diagram. They are the two transitions on the <code class="language-plaintext highlighter-rouge">Searching</code> and <code class="language-plaintext highlighter-rouge">Factoring</code> states that stay in the same state. You can also see the how the two loops interconnect through the transitions between the <code class="language-plaintext highlighter-rouge">Searching</code> and <code class="language-plaintext highlighter-rouge">Factoring</code> states. The <code class="language-plaintext highlighter-rouge">Starting</code> state simply accepts <code class="language-plaintext highlighter-rouge">n</code> from the outside world and initializes <code class="language-plaintext highlighter-rouge">d</code> and <code class="language-plaintext highlighter-rouge">factors</code>, and then dispatches to one of the other three states as appropriate. The <code class="language-plaintext highlighter-rouge">Done</code> state simply returns the <code class="language-plaintext highlighter-rouge">factors</code> list.</p>
<p>This is how Alan Turing envisioned computation in his <a href="https://www.cs.virginia.edu/~robins/Turing\_Paper\_1936.pdf">1936 paper</a>, which you can read about in Charles Petzold’s wonderful book: <a href="https://www.amazon.com/Annotated-Turing-Through-Historic-Computability/dp/0470229055">The Annotated Turing</a>.</p>
<p>So, we’ve gone from a nice doubly nested loop in Java to a Turing style finite state machine simply through a sequence of refactorings, each of which kept all the tests passing. This transformation from a standard procedure to a Turing style finite state machine could be done on any program at all.</p>
<p>Now let’s go back to the two bits of code that started all this. The Java version:</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>public List&lt;Integer&gt; factorsOf(int n) {
ArrayList&lt;Integer&gt; factors = new ArrayList&lt;&gt;();
for (int d = 2; n &gt; 1; d++)
for (; n % d == 0; n /= d)
factors.add(d);
return factors;
}
</code></pre></div></div>
<p>And the Clojure version:</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(defn prime-factors [n]
(loop [n n d 2 factors []]
(if (&gt; n 1)
(if (zero? (mod n d))
(recur (/ n d) d (conj factors d))
(recur n (inc d) factors))
factors)))
</code></pre></div></div>
<p>The finite state machine is entirely hidden in the Java version isn’t it. It’s very difficult to see it peaking out from those nested <code class="language-plaintext highlighter-rouge">for</code> loops. But that state machine is much more obvious in the Clojure program. The state is determined by the two <code class="language-plaintext highlighter-rouge">if</code> forms, and the appropriate code is executed for each state.</p>
<p>If you can’t see that FSM in the Clojure code, then consider this simple refactoring which makes it even more evident:</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(defn factors [n]
(loop [n n d 2 fs []]
(cond
(and (not= n 1) (zero? (mod n d))) (recur (/ n d) d (conj fs d))
(and (not= n 1) (not (zero? (mod n d)))) (recur n (inc d) fs)
(= n 1) fs)))
</code></pre></div></div>
<p>Why should this be? Why should the Clojure program look more like the FSM than the Java program? The answer is simple. The Java program can save some state information <em>within</em> the flow of control, because it can mutate variables while the loops are in progress. The Clojure program cannot save any state within the flow of control because no variables can be mutated at all. Those state changes are only noticed when the recursive <code class="language-plaintext highlighter-rouge">loop</code> is re-entered.</p>
<p>Thus, functional programs tend to look much more like Finite State Machines than programs that are free to manipulate variables.</p>
<p>One last thought. The Java program that implemented the Finite State Machine had only one loop; and that loop was: <code class="language-plaintext highlighter-rouge">while</code> <code class="language-plaintext highlighter-rouge">(true)</code>. That means the loop knew nothing at all about the algorithm it was looping. Thus we can abstract it away from the program itself and envision a language that has no loops at all. No <code class="language-plaintext highlighter-rouge">while</code> statements, no <code class="language-plaintext highlighter-rouge">for</code> loops, no <code class="language-plaintext highlighter-rouge">if</code> statements, and (of course) no <code class="language-plaintext highlighter-rouge">goto</code>s. Programs in this language would be written in the FSM style. They would be composed of switch statements that switched on boolean expressions that identified each state. The language system would then simply execute that program, over and over, until told to stop.</p>
<p>Such programs would be naturally functional. For although they could mutate the state of variables, the mutated state would be irrelevant to the flow of control within the program, and could only affect the next iteration of the program. In effect the program would look like a tail-call-optimized recursive function.</p>
<p>Wait… Did I miss the exit?</p>

Conference Conduct

2020-09-23T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2020/09/23/ConferenceConduct
<p>It was just a few years ago, at the height of the <em>Me Too</em> revelations, that codes of conduct began to prominently appear in Software Conferences. At the time I felt this was appropriate given the horror stories that had been circulating about sexual harassment and misbehavior at some of those conferences. I wrote a <a href="http://blog.cleancoder.com/uncle-bob/2016/01/15/Manhandled.html">blog</a> about it at the time.</p>
<p>Since then I have seen the other side of the coin. Codes of conduct have been used as weapons to exclude people on the basis of their political opinions, or on the basis of their associations, or just because someone didn’t like them. I have written blogs about this as well. <a href="http://blog.cleancoder.com/uncle-bob/2019/11/08/OpenLetterLinuxFoundation.html">(1)</a>, <a href="http://blog.cleancoder.com/uncle-bob/2017/09/26/SierraJulietFoxtrot.html">(2)</a></p>
<p>As much as I think that codes of conduct are a good idea, we must not allow them to be weaponized. If we are going to set up rules with consequences, then we also need to set up the the due processes by which those rules and consequences are adjudicated. Otherwise the people who police the codes of conduct will be free of the due checks and balances that protect conference attendees and speakers from unfair and malicious actions. As we have seen, such malicious and unfair actions have become all too common.</p>
<p>It seems to me that if a conference is going to publish a code of conduct, like the one below, they must also publish the process by which alleged violations will be adjudicated. That process must include provisions for the accused to be able to defend themselves against the allegation, and must also allow the accused to know the identity of the accuser(s). Otherwise all conference attendees and speakers will be exposed to malicious and falsified complaints with no recourse to defend themselves.</p>
<p>The conference I was <a href="http://blog.cleancoder.com/uncle-bob/2020/09/12/TheDisinvitation.html">disinvited</a> from is over. I was ejected because code of conduct complaints were registered against me by three relatively minor speakers in quick succession. I do not know if those speakers acted in concert. Nor am I certain of the identities of those speakers (though I have a good idea). What I <em>do</em> know is that three or four weeks before the conference was to begin those speakers threatened to withdraw from the conference if I were allowed to speak.</p>
<p>From what I have been able to discern, the conference organizers conducted an investigation. I was not a party to this investigation, indeed I was unaware that it was taking place. I was not notified about the complaints, nor was I given the opportunity to speak in my own defense. The conference organizers simply judged me based upon the complaints and whatever they could discover for themselves. I am quite certain that due diligence was not a requirement of the investigation.</p>
<p>Given that they were volunteers, and that losing three speakers one month before the conference is a considerable blow, it’s not hard to imagine that the conference organizers were under a fair bit of pressure to resolve the issue quickly and salvage as many speakers as possible. What’s more, the conference had already extracted as much value as it could from my image being emblazoned on their website and on the mailers they sent out two days before the start of the conference. So the decision to eject me must have been pretty easy.</p>
<p>What was the code of conduct violation? Apparently it related to something on twitter. I have read the code of conduct and the only potential violation I can see falls under the following rule.</p>
<blockquote>
<p><em>Any form of written, social media, or verbal communication that can be offensive or harassing to any attendee, speaker or staff is not allowed at Chicago Cloud Conference.</em></p>
</blockquote>
<p>That’s quite a standard. I don’t think any of us could withstand it. We’ve all said or written things that have offended, or could offend <em>someone</em>. I’ve had people get offended about my definition of monads. I’ve had people get upset with me about the SOLID principles, or my position on TDD, or my criticisms of statically typed languages. Some people may even have been offended by my infrequent comments about current politics.</p>
<p>As written, this rule means that anybody can complain about anything you might have said or written, at any time in the past. The only qualification for violation is that <em>someone</em> finds it offensive.</p>
<p>What’s more, since there is no published process of adjudication, you may well find that if a complaint is made against you, you will <em>not</em> be able to defend yourself, in any way. An individual, or a small group of people, whom you do not know, will vote in secret, without your knowledge, and without your input. If they decide against you, you will be ejected from the conference, without refund, and without recourse.</p>
<p>In short this means that if someone doesn’t like you, they can get you kicked out – and there’s nothing you can do about it. In my case three speakers apparently didn’t like something I said on twitter. So they extorted the conference organizers who bowed under the weight of that extortion and disinvited me without giving me the opportunity to address the complaints.</p>
<p>My solution to this is simple:</p>
<blockquote>
<p><em>From now on I will not agree to attend, nor will I agree to speak at, any conference that publishes a code of conduct but does not have a published process for adjudicating code of conduct complaints. That process must include a means for those accused of a violation to defend themselves from the malicious actions of others, and must allow them to know who their accusers are.</em></p>
</blockquote>
<p>I recommend that you all adopt the same policy.</p>
<hr />
<blockquote>
<p><strong>Code Of Conduct</strong></p>
</blockquote>
<blockquote>
<p>Chicago Cloud Conference is dedicated to providing a harassment-free conference experience for everyone, regardless of gender, sexual orientation, disability, physical appearance, body size, race, or religion. We have a zero-tolerance policy for any harassment of conference participants in any form. Sexual language and imagery is not appropriate for any conference venue, including talks. Conference participants violating these rules may be sanctioned or expelled from the conference without a refund at the discretion of the conference organizers.</p>
</blockquote>
<blockquote>
<p>Any form of written, social media, or verbal communication that can be offensive or harassing to any attendee, speaker or staff is not allowed at Chicago Cloud Conference. Please inform a Chicago Cloud Conference staff member if you feel a violation has taken place and the conference leadership team will address the situation.</p>
</blockquote>
<blockquote>
<p>Harassment includes offensive verbal comments related to gender, sexual orientation, disability, physical appearance, body size, race, religion; sexual images in public spaces; deliberate intimidation; stalking; following; harassing photography or recording; sustained disruption of talks or other events; inappropriate physical contact; and unwelcome sexual attention. Participants asked to stop any harassing behavior are expected to comply immediately.
Exhibitors in the expo hall, sponsor or vendor booths, or similar activities are also subject to the anti-harassment policy. In particular, exhibitors should not use sexualized images, activities, or other material. Booth staff (including volunteers) should not use sexualized clothing/uniforms/costumes, or otherwise create a sexualized environment.</p>
</blockquote>
<blockquote>
<p>If a participant engages in harassing behavior, the conference organizers may take any action they deem appropriate, including warning the offender or expulsion from the conference with no refund. If you are being harassed, notice that someone else is being harassed, or have any other concerns, please contact a member of conference staff immediately. Conference staff can be identified by t-shirts and special badges.
Conference staff will be happy to help participants contact hotel/venue security or local law enforcement, provide escorts, or otherwise assist those experiencing harassment to feel safe for the duration of the conference. We value your attendance.</p>
</blockquote>
<blockquote>
<p>We expect participants to follow these rules at all conference venues and conference-related social events.</p>
</blockquote>
<blockquote>
<p>Chicago Cloud Conference prioritizes marginalized people’s safety over privileged people’s comfort and therefore we will not act on complaints regarding:
‘Reverse’ -isms, including ‘reverse racism,’ ‘reverse sexism,’ and ‘cisphobia’.
Reasonable communication of boundaries, such as “leave me alone,” “go away,” or “I’m not discussing this with you”.
Communicating in a ‘tone’ you don’t find congenial.
Criticizing racist, sexist, cissexist, or otherwise oppressive behavior or assumptions.</p>
</blockquote>
<blockquote>
<p>What to do when you witness a Code of Conduct violation?</p>
</blockquote>
<blockquote>
<p>All reports of incidents are confidential! We will not publish the name of the reporter in any way.
Speak up</p>
</blockquote>
<blockquote>
<p>Of course we do not want you do get into a more uncomfortable position as you maybe already are. You do not need to interact with the person(s) who presumably violated the Code of Conduct. Please let someone of the organizing team know</p>
</blockquote>
<blockquote>
<p>In every session, you will find one track host (the person introducing the speakers) and at least one crew member (wearing a colorful shirt with the word “crew” on it). All people who are working on Chicago Cloud Conference are very aware of the Code of Conduct.
Approach them and let them know. In most cases they will bring you to one of the main organizers, so we can write an incident report.
Who What were the circumstances that led to the incident?
When?</p>
</blockquote>
<blockquote>
<p>Everyone working on Chicago Cloud Conference is informed on how to deal with an incident and how to further proceed with the situation.</p>
</blockquote>
<blockquote>
<p>The Purpose of the Code of Conduct:</p>
</blockquote>
<blockquote>
<p>By signaling inclusivity and diversity as values we expect the conference to uphold, the Code of Conduct helps guarantee that the event will indeed be inclusive and embrace diversity.</p>
</blockquote>

The Disinvitation

2020-09-12T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2020/09/12/TheDisinvitation
<p>I have a friend, in the Chicago area, who calls me up two or three times a year to ask me to give a talk at a User Group, or a conference he’s involved with, or something like that. If my schedule is free I always say yes. I don’t charge anything because I enjoy supporting the Chicago software community, and it’s never a bad thing to get my face out in front of new people. I am a consultant, after all, and giving pro-bono talks is one of the ways I promote myself.</p>
<p>Anyway, he wrote to me last October (That’s right, a full year ago!) and asked me to give a presentation at a Chicago conference this September 21st. I agreed, and he thanked me, and that was that. Then, in June, he wrote to tell me that the conference was going to be virtual due to Covid. I acknowledged and, once again, that was that.</p>
<p>Last Wednesday, September 9th, twelve days before the conference, he called me on the phone and said:</p>
<blockquote>
<p><em>“This is going to be the most uncomfortable phone call I have ever made.”</em></p>
</blockquote>
<p>He went on to say that the “Code of Conduct” people at the conference were concerened about some of my political opinions, and that some of the speakers of the conference refused to speak if I was going to speak.</p>
<p>Like I said, this guy is a friend of mine, and I don’t want to get him into any trouble, so I decided not to raise a fuss about it, and I promised him I would not mention his name or the name of the conference on line. He responded by telling me:</p>
<blockquote>
<p><em>I’m scared to death of these people.</em></p>
</blockquote>
<p>Over the last few days I’ve been mulling this situation over in my mind, and I’ve come to a few interesting conclusions.</p>
<ol>
<li><strong>The conference organizers are in breach of contract.</strong></li>
</ol>
<p>OK, we didn’t have a formal written contract, but we had emails. And we also had the fact that, for the better part of a year, the conference website had my picture on it, and advertised me as a speaker. I conclude that the conference organizers derived substantial benefit from those pictures and from promising my virtual presence to their audience. I, on the other hand, was denied the benefit of actually speaking to that audience. Therefore, I am the damaged party.</p>
<p>Could I sue them? Certainly, though I’d have a difficult time quantifying the damages. Had we agreed on a speaking fee, I could at least claim that fee as damages. Next time I do one of these pro-bono events I’ll have the organizers agree to paying a hefty cancellation fee.</p>
<ol>
<li><strong>The speakers who refused to speak if I spoke are guilty of <em>tortious interference</em>.</strong></li>
</ol>
<p>Those speakers would not have been harmed by speaking in a virtual conference that I also spoke in. Their intent was to damage me by forcing the conference organizers to breach their contract with me. That is the definition of tortious interference.</p>
<p>Could I sue them? Certainly. I won’t, for the same reason that I’m not going to sue the conference organizers. And, frankly, suing people for such small potatoes just isn’t worth the trouble. But, like I said, next time I do a pro-bono talk I’ll have the conference organizers agree to the value that I’m deriving in return for using my name and likeness on their website. Then I can sue them, and any tortious interferers, for that sum and punitive damages too.</p>
<p>Do I know who those tortiously interfering speakers are? I’ve got a pretty good idea. Myfear of course is that I do not wish to harm my friend. Nor do I wish to harm the conference organizers, nor the Chicago Software community. It seems to me that they are all victims of those revolting speakers.</p>
<p>So, this time, I’ll let the legal options rest. Instead, I’m offering a virtual <a href="https://us02web.zoom.us/webinar/register/WN\_Q5Fi-nWkRM6sdhNVY3r6VQ">free talk</a> at 10:00 AM CDT, on September 21st, the first day of the conference. Those who wanted to hear me speak, still can.</p>
<p>The last point I’d like to make is this:</p>
<blockquote>
<p><em>Disinviting someone from a virtual conference who can draw a potentially large audience away from that virtual conference is not a particularly intelligent tactic.</em></p>
</blockquote>

REPL Driven Design

2020-05-27T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2020/05/27/ReplDrivenDesign
<p>If you follow me on facebook you know that I’ve been publishing daily CoronaVirus statistics. I generate these statistics using the daily updates in the Johns Hopkins github <a href="https://github.com/CSSEGISandData/COVID-19">repository</a>.</p>
<p>At first I just hand copied the data into a spreadsheet. But that became tedious quite rapidly.</p>
<p>Then, in late March, I wrote a little Clojure program to extract and process the data. Every morning I pull the repo, and then run my little program. It reads the files, does the math, and prints the results.</p>
<p>Of course I used TDD to write this little program.</p>
<p>But over the last several weeks I’ve made quite a few small modifications to the program; and it has grown substantially. In making these adaptations I chose to use a different discipline: REPL Driven Design.</p>
<p>REPL Driven Design is quite popular in Clojure circles. It’s also quite seductive. The idea is that you try some experiments in the REPL to make sure you’ve got the right ideas. Then you write a function in your code using those idea. Finally, you test that function by invoking it at the REPL.</p>
<p>It turns out that this is a very satisfying way to work. The cycle time – the time between a code experiment and the test at the REPL – is nearly as small as TDD. This breeds lots of confidence in the solution. It also seems to save the time needed to mock, and create fake data because, at least in my case, I could use real production data in my REPL tests. So, overall, it felt like I was moving faster than I would have with TDD.</p>
<p>But then, in late April, I wanted to do something a little more complicated than usual. It required a design change to my basic structure. And suddenly I found myself full of fear. I had no way to ensure that those design changes wouldn’t leave the system broken in some way. If I made those changes, I’d have to examine every output to make sure that none of them had broken. So I postponed the change until I could muster the courage, and set aside the dedicated time it would require.</p>
<p>The change was not too painful. Clojure is an easy language to work with. But the verfication was not trivial, which led me to deploy the program with a small bug – a bug I caught 4 days later. That bug forced me to go back and correct the data and graphs that I generated.</p>
<p>Why did I need the design change? Because I was not mocking and creating fake data. My functions just read from the repo files directly. There was no way to pass them fake data. The design change I needed to make was precisely the same as the design change that I’d have needed for mocking and fake data.</p>
<p>Had I stuck with the TDD discipline I would have automatically made that design change, and I would not have faced the fear, the delay, and the error.</p>
<p>Is it ironic that the very design change that TDD would have forced upon me was the design change I eventually needed? Not at all. The decoupling that TDD forces upon us in order to pass isolated inputs and gather isolated outputs is almost always the design that fascilitates flexibility and promotes change.</p>
<p>So I’ve learned my lesson. REPL driven development feels easier and faster than TDD; but it is not. Next time, it’s back to TDD for me.</p>

A Little More Clojure

2020-04-09T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2020/04/09/ALittleMoreClojure
<p>So let’s learn just a little bit more of Clojure.</p>
<p>Here are a few common utility functions:</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>user=&gt; (inc 1) ; increments argument
2
user=&gt; (dec 3) ; decrements argument
2
user=&gt; (empty? []) ; tests for empty
true
user=&gt; (empty? [1 2])
false
</code></pre></div></div>
<p>If you know Java or C# you probably know what the <code class="language-plaintext highlighter-rouge">map</code> function does. Here’s an example: <code class="language-plaintext highlighter-rouge">(map inc [1 2 3])</code> evaluates to <code class="language-plaintext highlighter-rouge">(2 3 4)</code>.<br />
The first argument of map is a function. The second is a list. The <code class="language-plaintext highlighter-rouge">map</code> function returns a new list by applying the function to every element of the input list.</p>
<p>The <code class="language-plaintext highlighter-rouge">filter</code> function also takes a function and a list. <code class="language-plaintext highlighter-rouge">(filter odd? [1 2 3 4 5])</code> evaluates to <code class="language-plaintext highlighter-rouge">(1 3 5)</code>. From that I think you can tell what both the <code class="language-plaintext highlighter-rouge">filter</code> and the <code class="language-plaintext highlighter-rouge">odd?</code> functions do.</p>
<p>And so with that, let’s try a little challenge. Let’s find all the prime numbers between one and a thousand.</p>
<p>We’ll use a variant of TDD to do this. Our eyes will be the tests. The cycle will be the same size as normal TDD; but we’ll write a bit of code first and then test it.</p>
<blockquote>
<p><em>I know. Blashphemy! So sue me. ;-)</em></p>
</blockquote>
<p>We begin like this: <code class="language-plaintext highlighter-rouge">(defn primes [n] )</code> This returns <code class="language-plaintext highlighter-rouge">nil</code>.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>user=&gt; (primes 1000)
nil
</code></pre></div></div>
<p>Now let’s get all the numbers between 1 and <code class="language-plaintext highlighter-rouge">n</code>.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(defn primes [n]
(range 1 (inc n)))
user=&gt; (primes 10)
(1 2 3 4 5 6 7 8 9 10)
</code></pre></div></div>
<p>You’ve probably figured out what <code class="language-plaintext highlighter-rouge">range</code> does. It just returns a list of all the integers between it’s arguments.</p>
<p>OK, so now all we have to do is filter all the primes:</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(defn primes [n]
(let [candidates (range 1 (inc n))]
(filter prime? candidates)))
CompilerException java.lang.RuntimeException: Unable to resolve symbol: prime? in this context, compiling:(null:3:5)
</code></pre></div></div>
<p>Oh, oh. We need to implement <code class="language-plaintext highlighter-rouge">prime?</code></p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(defn prime? [n])
user=&gt; (primes 10)
()
</code></pre></div></div>
<p>OK, that makes sense. But I should explain the <code class="language-plaintext highlighter-rouge">let</code> function. It allows you to create names that are bound to expressions. The names exist only within the parentheses of the <code class="language-plaintext highlighter-rouge">let</code> expression. So it’s a way to create local variables – though the word “variable” is not quite right because they cannot be reassigned. They are immutable.</p>
<p>Now how do we tell if a given integer <code class="language-plaintext highlighter-rouge">n</code> is prime? Well, you all know how to do that, right? The simple and naive way is to divide the integer by every number between 2 and <code class="language-plaintext highlighter-rouge">n</code>. But, of course that’s wasteful. There’s a better upper limit to try which is the square root of <code class="language-plaintext highlighter-rouge">n</code>. I’m sure you can work out why that’s true.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(defn prime? [n]
(let [sqrt (Math/sqrt n)]
sqrt))
user=&gt; (prime? 100)
10.0
</code></pre></div></div>
<p>OK, that’s right. Notice that we called the Java <code class="language-plaintext highlighter-rouge">Math.sqrt</code> function. That’s a good example of how Clojure can call down into the Java libraries). Of course we don’t want <code class="language-plaintext highlighter-rouge">prime?</code> to return a number; we want it to return a boolean. But for now it’s good to see the intermediate values of our computation.</p>
<p>So, next we’d like to get all the integers between 2 and the square root. We already know how to do that.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(defn prime? [n]
(let [sqrt (Math/sqrt n)
divisors (range 2 (inc sqrt))]
divisors))
user=&gt; (prime? 100)
(2 3 4 5 6 7 8 9 10)
</code></pre></div></div>
<p>Now which of the <code class="language-plaintext highlighter-rouge">divisors</code> divide <code class="language-plaintext highlighter-rouge">n</code> evenly? We can find out by using the <code class="language-plaintext highlighter-rouge">map</code> function.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(defn prime? [n]
(let [sqrt (Math/sqrt n)
divisors (range 2 (inc sqrt))
remainders (map (fn [x] (rem n x)) divisors)]
remainders))
user=&gt; (prime? 100)
(0 1 0 0 4 2 4 1 0)
</code></pre></div></div>
<p>The <code class="language-plaintext highlighter-rouge">rem</code> function should be self-explanatory; it just returns the integer remainder of the division of <code class="language-plaintext highlighter-rouge">n</code> by <code class="language-plaintext highlighter-rouge">x</code>. The <code class="language-plaintext highlighter-rouge">(fn [x]...)</code> business needs a little explanation. Notice how similar it is to <code class="language-plaintext highlighter-rouge">defn f [x]</code>? This is how we create an anonymous function. If you know the syntax in Java or C# for anonymous functions, then this shouldn’t be too much of a surprise to you. Anyway, the remainders list is just the list of all the remainders that result from dividing <code class="language-plaintext highlighter-rouge">n</code> by the <code class="language-plaintext highlighter-rouge">divisors</code>.</p>
<p>Now some of those remainders were zero, and that means they divided <code class="language-plaintext highlighter-rouge">n</code> evenly. Therefore <code class="language-plaintext highlighter-rouge">n</code> (100 in this case) is not prime. Let’s try a few others.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>user=&gt; (prime? 17)
(1 2 1 2)
user=&gt; (prime? 1001)
(1 2 1 1 5 0 1 2 1 0 5 0 7 11 9 15 11 13 1 14 11 12 17 1 13 2 21 15 11 9 9)
user=&gt; (prime? 37)
(1 1 1 2 1 2)
</code></pre></div></div>
<p>OK, so if the remainders list has a zero in it, then <code class="language-plaintext highlighter-rouge">n</code> is not prime. Well, that should be easy, shouldn’t it?</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(defn prime? [n]
(let [sqrt (Math/sqrt n)
divisors (range 2 (inc sqrt))
remainders (map (fn [x] (rem n x)) divisors)
zeroes (filter zero? remainders)]
zeroes))
user=&gt; (prime? 100)
(0 0 0 0)
user=&gt; (prime? 17)
()
</code></pre></div></div>
<p>So now all we need to do is return <code class="language-plaintext highlighter-rouge">true</code> if the list is empty. Right?</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(defn prime? [n]
(let [sqrt (Math/sqrt n)
divisors (range 2 (inc sqrt))
remainders (map (fn [x] (rem n x)) divisors)
zeroes (filter zero? remainders)]
(empty? zeroes)))
user=&gt; (prime? 100)
false
user=&gt; (prime? 17)
true
user=&gt; (primes 100)
(1 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97)
</code></pre></div></div>
<p>Now I want you to think carefully about how we solved this problem. No <code class="language-plaintext highlighter-rouge">if</code> statements. No <code class="language-plaintext highlighter-rouge">while</code> loops. Instead we envisioned lists of data flowing through filters and mappers. The solution was almost more of a fluid dynamics problem than a software problem. (Ok, that’s a stretch, but you get my meaning.) Instead of imagining a procedural solution, we imagine a data-flow solution.</p>
<p>Think hard on this – it is one of the keys to functional programming.</p>
<p>(Special thanks to Stu Halloway @stuarthalloway for cluing me into the dataflow mindset way back in 2005)</p>
<p>Oh, and the primes between 1 and 1000?</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>user=&gt; (primes 1000)
(1 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587 593 599 601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701 709 719 727 733 739 743 751 757 761 769 773 787 797 809 811 821 823 827 829 839 853 857 859 863 877 881 883 887 907 911 919 929 937 941 947 953 967 971 977 983 991 997)
</code></pre></div></div>
<blockquote>
<p><em>And, yes, there is a bug. 1 is not prime. 2 is prime. Can you fix it?</em></p>
</blockquote>

A Little Clojure

2020-04-06T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2020/04/06/ALittleClojure
<p>So let’s learn just a little bit of clojure.</p>
<p>This expression: <code class="language-plaintext highlighter-rouge">(1 2)</code> represents the list containing the integers 1 and 2 in that order. If you want an empty list, that’s just <code class="language-plaintext highlighter-rouge">()</code>. And the list of the first five letters of the alphabet is just <code class="language-plaintext highlighter-rouge">(\a \b \c \d \e)</code>.</p>
<p>Now you know a lot about the syntax of clojure. Perhaps you think there’s a lot missing. Well, there are a <em>few</em> things missing; but far fewer than you’d think.</p>
<p>You might be wondering how you add two numbers. That’s easy, that’s just <code class="language-plaintext highlighter-rouge">(+ 1 2)</code>. As it happens that’s also just the list of the function named <code class="language-plaintext highlighter-rouge">+</code> followed by a 1 and a 2. You see, a function call is really just a list. The function is the first element of the list, and the arguments are just the other elements of that list. When you want to call a function, you simply invoke the list that represents that function call.</p>
<p>There are quite a few built-in functions in clojure. For example there’s <code class="language-plaintext highlighter-rouge">+, -, \*, and /</code>. They do precisely what you’d think. Well, perhaps not precisely. <code class="language-plaintext highlighter-rouge">(+ 1 2 3)</code> evaluations to <code class="language-plaintext highlighter-rouge">6</code>. <code class="language-plaintext highlighter-rouge">(- 3 2 1)</code> evaluates to zero. <code class="language-plaintext highlighter-rouge">(\* 2 3 4)</code> evaluates to <code class="language-plaintext highlighter-rouge">24</code>. And <code class="language-plaintext highlighter-rouge">(/ 20 2 5)</code> evaluates to 2. <code class="language-plaintext highlighter-rouge">(- 5)</code> evaluates to <code class="language-plaintext highlighter-rouge">-5</code>. <code class="language-plaintext highlighter-rouge">(\* 5)</code> evaluates to <code class="language-plaintext highlighter-rouge">5</code>. And, get ready for this, <code class="language-plaintext highlighter-rouge">(/ 3)</code> evaluates to <code class="language-plaintext highlighter-rouge">1/3</code>. That last is the clojure syntax for the rational number one-third.</p>
<p><code class="language-plaintext highlighter-rouge">(first 1 2 3)</code> evaluates to <code class="language-plaintext highlighter-rouge">1</code>, <code class="language-plaintext highlighter-rouge">(second 1 2 3)</code> evaluates to 2, and <code class="language-plaintext highlighter-rouge">(last 1 2 3)</code> evaluates to – you guessed it – <code class="language-plaintext highlighter-rouge">3</code>.</p>
<p>If you’d like to see this in action you’ll need to start up a clojure REPL. You can google how to do that. The word REPL stands for Read, Evaluate, Print Loop. It’s a very simple program that reads in an expression, evaluates that expression, prints the result of that expression, and then loops back to the read.</p>
<p>If you start a REPL you’ll get some kind of a prompt, perhaps like this <code class="language-plaintext highlighter-rouge">user=&gt;</code>. Then you can type an expression and see it evaluated. Here are a few from my REPL</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>user=&gt; (+ 1 2 3 4)
10
user=&gt; (- 5 6 7 8)
-16
user=&gt; (\* 6 7 8)
336
user=&gt; (/ 5 6 9)
5/54
</code></pre></div></div>
<p>If you try the expression at the very start of this article: <code class="language-plaintext highlighter-rouge">(1 2)</code> you’ll get a nasty surprise.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>user=&gt; (1 2)
ClassCastException java.lang.Long cannot be cast to clojure.lang.IFn user$eval1766.invokeStatic (:1)
</code></pre></div></div>
<p>That’s because the digit <code class="language-plaintext highlighter-rouge">1</code> is not a function; and the REPL believes that if it reads a list, that list ought to be evaluated as a function call. If you just want the list <code class="language-plaintext highlighter-rouge">(1 2)</code> at the REPL you can convince the REPL not to call the list as a function by quoting it as follows:</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>user=&gt; (quote (1 2))
(1 2)
user=&gt; '(1 2)
(1 2)
user=&gt; (list 1 2)
(1 2)
</code></pre></div></div>
<p>The first invokes the <code class="language-plaintext highlighter-rouge">quote</code> function which prevents its argument <code class="language-plaintext highlighter-rouge">(1 2)</code> from being evaluated and just returns it. The second is just a little syntax shortcut for calling the <code class="language-plaintext highlighter-rouge">quote</code> function. The third invokes the function that constructs lists.</p>
<p>Lists are implemented as linked lists. Each element contains a value and points to the next element. That makes it very fast to add an element to the front of the list, or to walk the list one element at a time. But it makes it slow to index into the list to find the Nth element. So, for that, clojure uses the <em>vector</em> data type. Here is a vector of the first three integers: <code class="language-plaintext highlighter-rouge">[1 2 3]</code>. That’s right, it’s the square brackets that do the trick.</p>
<p>A vector is a lot like a growable array. It’s easy to add to the end of it, and it’s easy to index into it. Lists make good stacks. Vectors make good queues.</p>
<p>Now let’s define a function. <code class="language-plaintext highlighter-rouge">(defn f [x] (+ (\* 3 x) 1))</code> this defines the function named <code class="language-plaintext highlighter-rouge">f</code>. It takes one argument named <code class="language-plaintext highlighter-rouge">x</code>. And it calculates the formula: <code class="language-plaintext highlighter-rouge">3x+1</code>.</p>
<p>Now let’s take this apart one token at a time. This looks like a call to the function <code class="language-plaintext highlighter-rouge">defn</code>. We’ll let that stand for the moment, but it’s not exactly right; <code class="language-plaintext highlighter-rouge">defn</code> is a bit more special than that. The next token is the name of the function: <code class="language-plaintext highlighter-rouge">f</code>. Names are alphanumeric with a few special characters allowed. For example <code class="language-plaintext highlighter-rouge">+++</code> is a valid name. Following the name is a vector that names the function arguments. Again, these are names. Those names will be bound to the argument values when the function is called. And following the argument vector is the expression that is evaluated by the function. That expression can use the argument names.</p>
<p>You now know the vast majority of Clojure syntax. There’s more, of course, but you already know enough to write significant programs.</p>
<p>So let’s write a simple one. Let’s write the factorial function.<br />
<code class="language-plaintext highlighter-rouge">(defn fac [x] (if (= x 1) 1 (\* x (fac (dec x)))))</code></p>
<p>Let’s walk through this. The function is named <code class="language-plaintext highlighter-rouge">fac</code> and it takes one argument named <code class="language-plaintext highlighter-rouge">x</code>. The <code class="language-plaintext highlighter-rouge">if</code> function takes three arguments. If the first evaluates to something <em>truthy</em> it returns the second, otherwise it returns the third. The <code class="language-plaintext highlighter-rouge">=</code> function does exactly what you’d think: it is a test for equality. If <code class="language-plaintext highlighter-rouge">x</code> is 1, then the <code class="language-plaintext highlighter-rouge">if</code> statement, and therefore the function, will return 1. Otherwise the <code class="language-plaintext highlighter-rouge">if</code> statement will return <code class="language-plaintext highlighter-rouge">x</code> times the factorial of the decrement of <code class="language-plaintext highlighter-rouge">x</code>.</p>
<p>Let’s try it:</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>user=&gt; (fac 3)
6
user=&gt; (fac 4)
24
user=&gt; (fac 10)
3628800
user=&gt; (fac 20)
2432902008176640000
user=&gt; (fac 30)
ArithmeticException integer overflow clojure.lang.Numbers.throwIntOverflow (Numbers.java:1501)
</code></pre></div></div>
<p>That works nicely, until we exceed 64 bits of precision. Clojure likes to use 64 bit integers for efficiency. But if you’d rather have unlimited precision you can use the <code class="language-plaintext highlighter-rouge">N</code> notation.</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>user=&gt; (fac 1000N)
402387260077093773543702433923003985719374864210714632543799910429938512398629020592044208486969404800479988610197196058631666872994808558901323829669944590997424504087073759918823627727188732519779505950995276120874975462497043601418278094646496291056393887437886487337119181045825783647849977012476632889835955735432513185323958463075557409114262417474349347553428646576611667797396668820291207379143853719588249808126867838374559731746136085379534524221586593201928090878297308431392844403281231558611036976801357304216168747609675871348312025478589320767169132448426236131412508780208000261683151027341827977704784635868170164365024153691398281264810213092761244896359928705114964975419909342221566832572080821333186116811553615836546984046708975602900950537616475847728421889679646244945160765353408198901385442487984959953319101723355556602139450399736280750137837615307127761926849034352625200015888535147331611702103968175921510907788019393178114194545257223865541461062892187960223838971476088506276862967146674697562911234082439208160153780889893964518263243671616762179168909779911903754031274622289988005195444414282012187361745992642956581746628302955570299024324153181617210465832036786906117260158783520751516284225540265170483304226143974286933061690897968482590125458327168226458066526769958652682272807075781391858178889652208164348344825993266043367660176999612831860788386150279465955131156552036093988180612138558600301435694527224206344631797460594682573103790084024432438465657245014402821885252470935190620929023136493273497565513958720559654228749774011413346962715422845862377387538230483865688976461927383814900140767310446640259899490222221765904339901886018566526485061799702356193897017860040811889729918311021171229845901641921068884387121855646124960798722908519296819372388642614839657382291123125024186649353143970137428531926649875337218940694281434118520158014123344828015051399694290153483077644569099073152433278288269864602789864321139083506217095002597389863554277196742822248757586765752344220207573630569498825087968928162753848863396909959826280956121450994871701244516461260379029309120889086942028510640182154399457156805941872748998094254742173582401063677404595741785160829230135358081840096996372524230560855903700624271243416909004153690105933983835777939410970027753472000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000N
</code></pre></div></div>
<p>OK, one last thing. Let’s add up all the numbers in a list. We want <code class="language-plaintext highlighter-rouge">(sum [1 2 3 4 5])</code> to evaluate to <code class="language-plaintext highlighter-rouge">15</code>. First we’ll do it the hard way:<br />
<code class="language-plaintext highlighter-rouge">(defn sum [l] (if (empty? l) 0 (+ (first l) (sum (rest l)))))</code></p>
<p>The <code class="language-plaintext highlighter-rouge">empty?</code> function does just what you’d think, it returns true if the list is empty. The <code class="language-plaintext highlighter-rouge">rest</code> function returns all but the first element of a list.</p>
<p>Of course we could have written <code class="language-plaintext highlighter-rouge">sum</code> like this: <code class="language-plaintext highlighter-rouge">(defn sum [l] (apply + l))</code>. The <code class="language-plaintext highlighter-rouge">apply</code> function – um – applies the function passed in it’s first argument to the list in its second.</p>
<p>We could also have written the function like this: <code class="language-plaintext highlighter-rouge">(defn sum [l] (reduce + l))</code>. But that takes us to the <code class="language-plaintext highlighter-rouge">reduce</code> function which (as George Carlin used to say) might go a bit too far. At least for this article.</p>

A New Hope

2020-04-05T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2020/04/05/ANewHope
<p><strong>…The Year is 2045…</strong></p>
<p>Dad, can you help me with my school report?</p>
<blockquote>
<p><em>Sure son. What’s it about?</em></p>
</blockquote>
<p>We have to do it on the great pandemic of 2020. You were there, right?</p>
<blockquote>
<p><em>I was just a little boy. But I know a lot about it. What is it you need to know?</em></p>
</blockquote>
<p>We’re supposed to write about the heroes.</p>
<blockquote>
<p><em>Ah, yes. A good topic. There were so many.</em></p>
</blockquote>
<p>OK, so… Who were they?</p>
<blockquote>
<p><em>Well, first of all there were the healthcare workers. Day after day, week after week, they kept on working in those hospitals full of very sick people. Many of them got sick too; and quite a few of them died.</em></p>
</blockquote>
<p>They must have been brave.</p>
<blockquote>
<p><em>They were. Very. They were as brave as any soldier going to war. Perhaps braver, because you couldn’t see the enemy, and in those days you couldn’t fight it.</em></p>
</blockquote>
<p>We can fight it now, can’t we Dad.</p>
<blockquote>
<p><em>Yes son. Now we can. We have vaccines and treatments. Nobody dies of COVID-19 anymore. But back then we didn’t have vaccines or treatments. We just had nurses and doctors who tried their very best to save as many people as possible.</em></p>
</blockquote>
<p>So they were the heroes?</p>
<blockquote>
<p><em>Yes. But there were many more. There were the people who worked in grocery stores.</em></p>
</blockquote>
<p>I thought everybody stayed home to work.</p>
<blockquote>
<p><em>Many of us did. We were the lucky ones. But the people who worked in those stores had to go to work every day. People needed food; and so grocery stores needed to stay open. And the people who worked in those stores had to help hundreds, maybe even thousands of people every day. They took huge risks to keep those stores open.</em></p>
</blockquote>
<p>Wow, I hadn’t thought of that.</p>
<blockquote>
<p><em>And then there were the delivery people. The people who drove trucks of food to the stores and trucks of products to people’s home. The people who worked for Amazon, and UPS, and Fedex, and the US Mail.</em></p>
</blockquote>
<p>Who else, Dad? Who else?</p>
<blockquote>
<p><em>Well, look son, there were so many. The police, the firemen, the sailors and soldiers, the air traffic controllers, the garbage men, the repairmen. Even though most people weren’t working, the essential parts of our civilization had to be kept running. And then there were just the everyday people who followed the rules and kept themselve at home for so many weeks. It was a huge effort that everyone had to play a part in.</em></p>
</blockquote>
<blockquote>
<p><em>But…</em></p>
</blockquote>
<p>But what, Dad?</p>
<blockquote>
<p><em>Well, there was one group of people who don’t often get mentioned; but without them the Pandemic would have been a hundred times worse than it was.</em></p>
</blockquote>
<p>Really? Who?</p>
<blockquote>
<p><em>The programmers.</em></p>
</blockquote>
<p>Dad… You’re a programmer aren’t you?</p>
<blockquote>
<p><em>Yes son, I am. Just like my mother – your gramma – before me. She was one of the ones who worked during the Pandemic.</em></p>
</blockquote>
<p>Was gramma a hero Dad?</p>
<blockquote>
<p><em>No more than anyone else, son. She worked from home. She wore masks, and kept the necessary social distance from others. I was just a little boy, but I remember those masks and how much we had to stay at home. Most programmers did just what Gramma did too. They worked from home.</em></p>
</blockquote>
<p>So then why were they heros, Dad? It sounds to me like they just did what everybody else did.</p>
<blockquote>
<p><em>Well, son, think of this. It was the programmers who made it possible for people to work from home; because it was the programmers who built the software that made the internet possible. You see, this was the first full scale national emergency during which people had instant access to the news, to the government, and to each other. When the President, and the Governors told people to shelter at home, almost everybody knew about it within minutes or hours. The news was sent to their computers, to their phones, and to their watches. Not only that, but people who were stuck at home could still talk to each other using Facebook and Twitter and Facetime. People could order products on Amazon, and on so many other on-line shopping networks. People could even order food from restaurants to be delivered or picked up. Without the programmers who made those systems, people would have had a much harder time sheltering at home; and the pandemic would have been much worse.</em></p>
</blockquote>
<p>So the programmers weren’t brave, like the doctors and nurses and police were brave. They weren’t heros like that.</p>
<blockquote>
<p><em>No, not like that. But without them, without the tools they created, so many more people would have died. For example, did you know that the genetic code of the virus was sequenced long before the pandemic spread? It was that RNA sequence that allowed our researchers to get a head start on the vaccines that eventually killed off the virus and saved so many people. It was programmers who built the software that ran in those RNA sequencers. Without those programmers, the vaccines might have come much too late.</em></p>
</blockquote>
<p>Wow! What else, Dad? What else?</p>
<blockquote>
<p><em>Well, you know that there was a time when people used paper money, right? Imagine how easily the virus would have spread if people paid for groceries or gasoline with paper money! But it was programmers who built the systems that allowed people to pay with credit cards, or by just waving their phone or watch over readers. They didn’t even have to touch antyhing! The virus couldn’t spread that way.</em></p>
</blockquote>
<blockquote>
<p><em>And then there was so much entertainment piped right into people’s homes. Netflix, and Amazon Prime, and Youtube, and.. Well the options were endless back then.</em></p>
</blockquote>
<blockquote>
<p><em>So people could work from home, shop from home, be entertained at home, and hardly ever had to leave their homes. And all that was because of the software written by programmers.</em></p>
</blockquote>
<p>And that saved us, didn’t it Dad?</p>
<blockquote>
<p><em>Well, son, it certainly played a pretty important part.</em></p>
</blockquote>
<p>Are you glad you’re a programmer Dad?</p>
<blockquote>
<p><em>It’s an important job, Son. I never want to be anything else. Except, of course, your Dad.</em></p>
</blockquote>

Open Letter to the Linux Foundation

2019-11-08T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2019/11/08/OpenLetterLinuxFoundation
<p>To: The Linux Foundation<br />
Jim Zemlin: Executive Director<br />
Angela Brown: VP of Events<br />
Andy Updegrove: Legal Council<br /></p>
<p>From: Robert Martin (@unclebobmartin) (unclebob@cleancoder.com)</p>
<p>Re: Code of Conduct case of Charles Max Wood.</p>
<p>Dear Linux Foundation:</p>
<p>I am writing to you as a concerned member of the software development community which I have enjoyed serving for the last 50 years. I am writing in public because the events I wish to describe took place in public. I fear that something has gone terribly wrong within your organization; and that it will have deep repercussions within this industry that I cherish.</p>
<p>The timeline of events, as far as I can determine them, is as follows:</p>
<p>The Linux Foundation received a public tweet sent to the @KubeCon twitter address. That tweet recommended that Kube Con discontinue their association with Charles Max Wood. The reasons given in this complaint were his request for an open and civil phone call, and a picture of Mr. Wood wearing a MAGA hat.</p>
<p>The Linux Foundation <em>publicly</em> replied from the @linuxfoundation twitter account as follows:</p>
<blockquote>
<p><em>Hi all, We have reviewed social and videos and determined that the Event Code of Conduct was violated and his registration to the event has been revoked. Our events should and will be a safe space.</em></p>
</blockquote>
<p>First let me say that I find it highly problematic that the complaint and the decision were public. Indeed I am surprised that LF would accept a publicly submitted code of conduct complaint. I am much more than surprised that LF would ever consider <em>publicly</em> responding to such a complaint. Indeed, it seems to me that the public complaint, and perhaps even the public response by LF, could be seen as public harassment – which is explicitly prohibited by the LF Code of Conduct.</p>
<p>It seems to me that Code of Conduct complaints made in public must be immediately rejected and viewed as Code of Conduct violations in and of themselves. Code of Conduct complaints should be submitted in private and remain private and confidential in order to prevent their use as a means of harassment. It also seems to me that while the process of accepting, reviewing, and adjudicating such complaints should be public, the proceedings and decision of each individual case should remain private and confidential in order to protect the parties from harm. Making them a public showcase is, simply, horrible.</p>
<p>Was the Code of Conduct actually violated by Mr. Wood? I have watched the videos in question and read the tweets and I can find no instance where Mr Wood violated the LF Code of Conduct. I understand that LF can make any decision they like about what constitutes a Code of Conduct violation. However, when both the complaint and the response are so blatantly public, it seems to me that LF owes it to the observing community to explain their decision and describe the due process that was used to make it – including the decision to make the public response that undoubtedly caused harm to Mr. Wood. To date no such explanation has been forthcoming, despite repeated requests.</p>
<p>The software community needs to understand how decisions like this are going to be made. Otherwise those of us who have watched this case may be forced to conclude that LF has no internal process, that no due diligence will be applied to Code of Conduct complaints and determinations, that the accused will have no rights either of appeal or privacy, that LF feels free to make its decisions based on the blowing of political winds, and will loudly announce their decisions regardless of the harm it might cause.</p>
<p>Therefore I have the following questions:</p>
<ul>
<li>
<p>Why was the initial complaint accepted and acknowledged in public? It was clearly political in nature, and very clearly intended to cause harm to Mr. Wood.</p>
</li>
<li>
<p>Is it LF policy to accept complaints that, in and of themselves, violate the LF Code of Conduct?</p>
</li>
<li>
<p>Why was the Code of Conduct determination announced publicly, despite the harm it would obviously cause to Mr. Wood?</p>
</li>
<li>
<p>Can LF specifically justify the determination that Mr. Wood violated the Code of Conduct?</p>
</li>
<li>
<p>Does LF have a documented process by which Code of Conduct complaints are to be submitted, reviewed, and adjudicated?</p>
</li>
<li>
<p>Is it LF policy to consider political affiliation, or support of certain public officials, as Code of Conduct violations?</p>
</li>
<li>
<p>Is it LF policy to publicly denounce registrants who have been determined to have violated the LF Code of Conduct?</p>
</li>
<li>
<p>Does LF have a Code of Conduct for how it conducts itself?</p>
</li>
</ul>
<p>In summary, it appears to this humble observer that The Code of Conduct process at The Linux Foundation went very badly off the rails with regard to Charles Max Wood. That LF owes Mr. Wood, and the Software Community at large, a <em>profound</em> apology. That LF should keep all future Code of Conduct complaints and decisions personal and confidential. That LF should publish and follow a well defined process for accepting, reviewing, and adjudicating future Code of Conduct complaints. And that some form of reparation be provided to Mr. Wood for the public harm that was done to him by the careless and unprofessional behavior of The Linux Foundation.</p>
<p>Yours</p>
<p>Robert C. Martin.</p>

What They Thought of Programmers.

2019-11-03T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2019/11/03/WhatTheyThoughtOfUs
<p>It is interesting and educational to go back in time and look at how programmers were represented in popular culture. What did they think of us? Did they know who were?</p>
<p>It’s important to remember that prior to 1946 there were no programmers, that computers themselves were virtually unknown until the late ’50s. That virtually nobody lived next door to a programmer back then.</p>
<p>Nowadays virtually everyone in the western world, and even in much of the developing world, is surrounded by computers. And while programming remains a mystery to many, programmers are common neighbors.</p>
<p>So let’s scan the last six decades and watch as the culture changes it’s view of just who we are and what we do.</p>
<h3 id="1956-forbidden-planet">1956 Forbidden Planet</h3>
<p>It’s best to begin at the beginning. The first truly classic Science Fiction movie. <em>Forbidden Planet</em>. If you haven’t seen it, you are missing something profound and spectacular. I urge you to watch – even study – it.</p>
<p>There are no explicit mentions of computers or programmers in this movie. The concept was simply not something that the public could relate to. However there was a machine. A very big machine. And the implication was that it was intelligent, but not sentient.</p>
<p><img src="/assets/krellMachine.jpeg" /></p>
<p>In the movie the anti-hero Dr Morbius is marooned on the uninhabited world of Altair 4. He discovers an ancient alien machine. Two decades later rescuers arrive. He shows them the machine and states: “I have reason to believe that years ago a minor alteration was performed throughout the entire 8000 cubic miles of it’s own fabric.”</p>
<p>The programmers of that big machine are long dead; but they are described as belonging to a highly evolved and benevolent alien race.</p>
<p>There is another machine on this planet. It is a robot named Robby.</p>
<p><img src="/assets/robby.jpeg" /></p>
<p>Robby is clearly intelligent and sentient. Robby speaks English, with the inflection of a proper british butler, rather in the manner of Carson on Downton Abbey. Dr. Morbius claims to have created the Robot; so he is clearly the programmer.</p>
<p>Morbius is studious, austere, even dour. He is not evil; but he is a hermit and does not particularly enjoy the company of others. He is massively intelligent but quite anti-social.</p>
<p>Now remember that this was the ’50s. Missiles and A-bombs. Scientists had a particular stereotype in those days, and Dr. Morbius is consistent with that; though with a hint of Captain Nemo.</p>
<h3 id="1954-tobor-the-great">1954 TOBOR the Great</h3>
<p>Yes, I’m going backwards two years, but only to say that I did not forget this movie. I just don’t count it as significant. This was a movie made for kids, and the semi-intelligent robot is much more like <em>Lassie</em> than Robby. The creator of Tobor is an eminent scientist who also fits the mold of the ’50s.</p>
<h3 id="1966-star-trek">1966 Star Trek</h3>
<p>With one exception, we learn very little about the programmers in Star Trek. The computer, however, is fascinating. The computer was voiced by Majel Barrett, Gene Roddenberry’s wife. She also played Nurse Chapel, and “Number One” in the pilot. She played the computer as utterly flat. The voice was monotone. The information was factual. The computer never offered an opinion, or an emotion of any kind. The computer was nothing more than a tool.</p>
<p>The exception was the episode entitled <em>The Ultimate Computer</em> in which a new intelligent computer was hooked up to the enterprise. The creator (and implicitly the programmer) of this machine was Dr. Daystrom. Both he and the computer have a simultaneous nervous breakdown, and Kirk has to “pull the plug”.</p>
<p>The implication is that programmers are so intelligent and driven that they eventually lose emotional stability.</p>
<p>This is one of the first instances of the computer acting as the villain.</p>
<h3 id="1968-2001-a-space-odyssey">1968 2001: A Space Odyssey</h3>
<p>Hal 9000 is the villain of this story. We know little of the programmer, Dr. Chandra, except that he taught the computer a song.</p>
<p>Note that during this era it is the computer that is the character. The programmers, if mentioned at all, are ancillary.</p>
<h3 id="1970-colossus-the-forbin-project">1970 Colossus: The Forbin Project</h3>
<p>Another movie in which the computer is the hyperintelligent villain. The programmer is a scientist from the Dr. Morbius mold.</p>
<h3 id="1982-blade-runner">1982 Blade Runner</h3>
<p>The computers are among the main characters and are essentially a race of slaves. We never meet the programmers, but it’s clear that they must be morally bankrupt.</p>
<h3 id="1982-tron">1982 Tron</h3>
<p>Hero programmer defeats evil computer. This is the first time we see the programmer as a good guy who defeats the computer. The movie is also a foreshadow of <em>The Matrix</em> because the main character gets transported into the computer. As a programmer (though they call him a “user”) he as powers.</p>
<p>The hero programmer is a world famous scientist and business man. He does not live next door.</p>
<h3 id="1983-war-games">1983 War Games</h3>
<p>The computer is again a character, though this time an innocent dupe. A young boy meets the programmer and psychoanalyses him in order to convince the computer to not destroy the world. The programmer is depicted as a famous scientist who is emotionally damaged. The computer is depicted as a child-like character who likes to play games.</p>
<h3 id="1984-the-terminator">1984 The Terminator</h3>
<p>This one is indirect. Well meaning humans program the evil computer, Skynet, that then programs the Terminator to kill Sarah Connor. So this is a <em>singularity</em> prediction. The computers program the computer.</p>
<p>One interesting aspect of this film is the depiction of the human-like machine being so utterly focused on it’s mission. At first you think of the terminator as almost human. But bit by bit that humanity is lost. In the end you see only the machine, half-destroyed, missing legs and all vestiges of human form, still intent on one purpose only.</p>
<h3 id="1986-short-circuit">1986 Short Circuit</h3>
<p>(Sigh) Jonny number five is a combat robot whose programming gets scrambled by a lightning strike. This makes the robot sentient and purely innocent. Eventually the robot invents it’s own moral code which is vastly superior to anything human.</p>
<p>So there is no programmer in this case – except nature or God or… And in that case all human flaws are exposed by the purity of the programming.</p>
<p>Cute movie, but very dumb.</p>
<h3 id="1993-jurassic-park">1993 Jurassic Park</h3>
<p>This is our first real glimpse of a humanized programmer. Dennis Nedry is not a mad scientist, not a well respected researcher, he’s just a common ordinary programmer. And he is a flawed human. Oh, there’s a bit of the Twinkie eating, basement dwelling stereotype there; but this is the first time the movies show a programmer as someone who might live next door.</p>
<p>The computer is not a character at all. It is just a tool (“a Unix System”).</p>
<h3 id="1995-the-net">1995 The Net</h3>
<p>The main character is a programmer who must user her skills as a programmer to defeat a ruthless plot to frame her for murder and other nefarious things.</p>
<p>This is another case where the programmer could be someone next door.</p>
<h3 id="1999-the-matrix">1999 The Matrix</h3>
<p>All the human characters are programmers. They all live next door. But, given the red pill, are transported to an alternate reality where they can “see” the code. They are engaged in an apocalyptic fight over good and evil. The main character is a type of Jesus.</p>
<h2 id="summary">Summary</h2>
<p>Note the progression. Over the years the representation of the computer changes from Main Character (Good or evil) to supporting character to tool. The programmer changes from obscurity to mad or damaged scientist, to Nature or Skynet, to the guy next door, to hyper-aware Savior.</p>
<p>What does this say about society’s opinion of us. Does society really think we are the folks who live next door who are simultaneously the hidden saviors?</p>
<p>Well, maybe we don’t want to read too much into things. Note that I stopped this review just prior to the millennium. Have there been any movies since then in which programmers played a significant role?</p>
<p>Actually, I think we have transitioned off the screen and have become part of the movie industry. Virtually no movie made nowadays can be made without massive computer graphics and programming effort. So now they know us intimately. We <em>do</em> live next door. And they don’t need to put us on the screen anymore.</p>

Circulatory

2019-10-31T00:00:00+00:00
http://blog.cleancoder.com/uncle-bob/2019/10/31/Circulatory
<p>My wife and I both got genetic analyses from <a href="https://www.23andme.com/">23andMe</a> recently. I discovered that my ancestry comes from Britain and Northern Europe. My wife is Mexican, and she found that her ancestry is very diverse.</p>
<p>One of the services of 23andMe is that they offer to connect you to relatives who have also used 23andMe. Using this service my wife found a second cousin whom she had never met, but whose extended family had overlapped with hers. By email they were able to compare the names of aunts and uncles, and the towns where they lived. The more they talked, the more they realized that the overlap with the extended families was large.</p>
<p>Some years back I went through the effort of scanning all the old photo albums that we had created or inherited over the years. From that trove of digitized pictures my wive was able to find a 50 year old photograph of that extended family, taken in a little town in Mexico. She shared that photo with her relative who happened to be visiting that town at the moment.</p>
<p>The relative showed the picture to her aunts, uncles, cousins, and they all started pointing to people that they recognized. Many tears flowed as warm recollections were conveyed. This is apparently the only surviving photograph of that extended family; and now they all have, and cherish, it.</p>
<p>Now I want you to consider what made this possible.</p>
<ul>
<li>I scanned those pictures on a whim, using <a href="https://photomyne.com">Photomyne</a> an iPhone app that makes scanning and cataloging old photos very easy.</li>
<li>My wife was able to find that picture using the Photos app on the Mac.</li>
<li>The software at 23andMe was able to find her distant relative.</li>
<li>Email and FaceTime allowed the two to communicate.</li>
<li>And the internet ran through it all.</li>
</ul>
<p>Software. It was software that drove the connection of all those people. It was software that enabled the warm tears of recollection to flow. It was software that provided the photo to the folks in that little town in Mexico, who had not seen the faces of their loved ones in 50 years. It was Software. It was you and I – the programmers who built the systems and the connections that made that miracle happen.</p>
<p>Software is the circulatory system of our civilization. Software digests, filters, and sorts the constituents of the information stream. Software routes the necessary element of that stream to the right places. Software is the heart, the lungs, the vessels, the liver and kidneys, and the digestive system of our civilization. Nothing works anymore without software. Our civilization could no longer survive without software.</p>
<p>But software does more than support the survival of our civilization. Software also supports those moments of joy that my wife and her relatives recently experienced.</p>
<p>It is things like this that make me proud to be a programmer. Without us, our civilization could not survive, and the warm connections between relatives and friends could not be made.</p>
<p>It is things like this that also make me yearn for a deeper discipline and professionalism for our industry. Too much depends upon us now. We’re going to have to leave the wild west of software behind and civilize ourselves, so that the civilization we support will continue to prosper.</p>

---

## Source: index.md

Clean Coder Blog


[![](/assets/clean_code_72_color.png)](/)

# The Clean Code Blog

by Robert C. Martin (Uncle Bob)



## Welcome!

[atom/rss feed](/atom.xml)


---

* [Functional Classes in Clojure](/uncle-bob/2023/01/19/functional-classes-clojure.html)

  01-19-2023
* [Functional Classes](/uncle-bob/2023/01/18/functional-classes.html)

  01-18-2023
* [Space War](/uncle-bob/2021/11/28/Spacewar.html)

  11-28-2021
* [Functional Duplications](/uncle-bob/2021/10/28/functional-duplication.html)

  10-28-2021
* [Roots](/uncle-bob/2021/09/25/roots.html)

  09-25-2021
* [More On Types](/uncle-bob/2021/06/29/MoreOnTypes.html)

  06-29-2021
* [On Types](/uncle-bob/2021/06/25/OnTypes.html)

  06-25-2021
* [if-else-switch](/uncle-bob/2021/03/06/ifElseSwitch.html)

  03-06-2021
* [Pairing Guidelines](/uncle-bob/2021/01/17/Pairing.html)

  01-17-2021
* [Solid Relevance](/uncle-bob/2020/10/18/Solid-Relevance.html)

  10-18-2020
* [Loopy](/uncle-bob/2020/09/30/loopy.html)

  09-30-2020
* [Conference Conduct](/uncle-bob/2020/09/23/ConferenceConduct.html)

  09-23-2020
* [The Disinvitation](/uncle-bob/2020/09/12/TheDisinvitation.html)

  09-12-2020
* [REPL Driven Design](/uncle-bob/2020/05/27/ReplDrivenDesign.html)

  05-27-2020
* [A Little More Clojure](/uncle-bob/2020/04/09/ALittleMoreClojure.html)

  04-09-2020
* [A Little Clojure](/uncle-bob/2020/04/06/ALittleClojure.html)

  04-06-2020
* [A New Hope](/uncle-bob/2020/04/05/ANewHope.html)

  04-05-2020
* [Open Letter to the Linux Foundation](/uncle-bob/2019/11/08/OpenLetterLinuxFoundation.html)

  11-08-2019
* [What They Thought of Programmers.](/uncle-bob/2019/11/03/WhatTheyThoughtOfUs.html)

  11-03-2019
* [Circulatory](/uncle-bob/2019/10/31/Circulatory.html)

  10-31-2019
* [Why Clojure?](/uncle-bob/2019/08/22/WhyClojure.html)

  08-22-2019
* [Why won't it...](/uncle-bob/2019/07/22/WhyWontIt.html)

  07-22-2019
* [Classes vs. Data Structures](/uncle-bob/2019/06/16/ObjectsAndDataStructures.html)

  06-16-2019
* [Types and Tests](/uncle-bob/2019/06/08/TestsAndTypes.html)

  06-08-2019
* [737 Max 8](/uncle-bob/2019/05/18/737-Max-8.html)

  05-18-2019
* [FP vs. OO List Processing](/uncle-bob/2018/12/17/FPvsOO-List-processing.html)

  12-17-2018
* [We, The Unoffended](/uncle-bob/2018/12/16/unoffended.html)

  12-16-2018
* [SJWJS](/uncle-bob/2018/12/14/SJWJS.html)

  12-14-2018
* [The Tragedy of Craftsmanship.](/uncle-bob/2018/08/28/CraftsmanshipMovement.html)

  08-28-2018
* [Too Clean?](/uncle-bob/2018/08/13/TooClean.html)

  08-13-2018
* [Integers and Estimates](/uncle-bob/2018/06/21/IntegersAndEstimates.html)

  06-21-2018
* [Pickled State](/uncle-bob/2018/06/06/PickledState.html)

  06-06-2018
* [Craftsman, Craftswoman, Craftsperson](/uncle-bob/2018/05/02/Craftsman-Craftswoman-Craftsperson.html)

  05-02-2018
* [FP vs. OO](/uncle-bob/2018/04/13/FPvsOO.html)

  04-13-2018
* [In The Large](/uncle-bob/2018/04/02/InTheLarge.html)

  04-02-2018
* [*We Programmers*](/uncle-bob/2018/03/29/WeProgrammers.html)

  03-29-2018
* [Uncle Bob Fly-In.  
  Have I got a deal for you!](/uncle-bob/2018/02/25/UncleBobFlyIn.html)

  02-25-2018
* [The Citizenship Argument](/uncle-bob/2018/01/18/TheCitizenshipArgument.html)

  01-18-2018
* [Operating Behind the Power Curve](/uncle-bob/2018/01/15/behindThePowerCurve.html)

  01-15-2018
* [Excuses](/uncle-bob/2017/12/18/Excuses.html)

  12-18-2017
* [Dbtails](/uncle-bob/2017/12/09/Dbtails.html)

  12-09-2017
* [Bobby Tables](/uncle-bob/2017/12/03/BobbyTables.html)

  12-03-2017
* [Living on the Plateau](/uncle-bob/2017/11/18/OnThePlateau.html)

  11-18-2017
* [Women In Demand](/uncle-bob/2017/10/04/WomenInDemand.html)

  10-04-2017
* [Tools are not the Answer](/uncle-bob/2017/10/04/CodeIsNotTheAnswer.html)

  10-04-2017
* [Test Contra-variance](/uncle-bob/2017/10/03/TestContravariance.html)

  10-03-2017
* [The Unscrupulous Meme](/uncle-bob/2017/09/29/TheUnscrupulousMeme.html)

  09-29-2017
* [Sierra Juliet Foxtrot](/uncle-bob/2017/09/26/SierraJulietFoxtrot.html)

  09-26-2017
* [Just Following Orders](/uncle-bob/2017/08/28/JustFollowingOders.html)

  08-28-2017
* [Women in Tech](/uncle-bob/2017/08/14/WomenInTech.html)

  08-14-2017
* [On the Diminished Capacity to Discuss Things Rationally](/uncle-bob/2017/08/10/OnTheInabilityToDiscussThingsRationally.html)

  08-10-2017
* [Thought Police](/uncle-bob/2017/08/09/ThoughtPolice.html)

  08-09-2017
* [The Brain Problem](/uncle-bob/2017/07/28/TheBrainProblem.html)

  07-28-2017
* [Drive me to Toronto, Hal.](/uncle-bob/2017/07/24/DriveMeToTorontoHal.html)

  07-24-2017
* [Pragmatic Functional Programming](/uncle-bob/2017/07/11/PragmaticFunctionalProgramming.html)

  07-11-2017
* [First-Class Tests.](/uncle-bob/2017/05/05/TestDefinitions.html)

  05-05-2017
* [Is Dr. Calvin in the Room?](/uncle-bob/2017/03/16/DrCalvin.html)

  03-16-2017
* [Symmetry Breaking](/uncle-bob/2017/03/07/SymmetryBreaking.html)

  03-07-2017
* [Testing Like the TSA](/uncle-bob/2017/03/06/TestingLikeTheTSA.html)

  03-06-2017
* [TDD Harms Architecture](/uncle-bob/2017/03/03/TDD-Harms-Architecture.html)

  03-03-2017
* [Necessary Comments](/uncle-bob/2017/02/23/NecessaryComments.html)

  02-23-2017
* [Types and Tests](/uncle-bob/2017/01/13/TypesAndTests.html)

  01-13-2017
* [The Dark Path](/uncle-bob/2017/01/11/TheDarkPath.html)

  01-11-2017
* [TDD Lesson - Terrain Generation](/uncle-bob/2017/01/09/DiamondSquare.html)

  01-09-2017
* [TDD Doesn't Work](/uncle-bob/2016/11/10/TDD-Doesnt-work.html)

  11-10-2016
* [Dijkstra's Algorithm](/uncle-bob/2016/10/26/DijkstrasAlg.html)

  10-26-2016
* [The Lurn](/uncle-bob/2016/09/01/TheLurn.html)

  09-01-2016
* [The Churn](/uncle-bob/2016/07/27/TheChurn.html)

  07-27-2016
* [Mutation Testing](/uncle-bob/2016/06/10/MutationTesting.html)

  06-10-2016
* [Blue. No! Yellow!](/uncle-bob/2016/05/21/BlueNoYellow.html)

  05-21-2016
* [Type Wars](/uncle-bob/2016/05/01/TypeWars.html)

  05-01-2016
* [Giving Up on TDD](/uncle-bob/2016/03/19/GivingUpOnTDD.html)

  03-19-2016
* [Manhandled](/uncle-bob/2016/01/15/Manhandled.html)

  01-15-2016
* [Stabilization Phases](/uncle-bob/2016/01/14/Stabilization.html)

  01-14-2016
* [A Little Architecture](/uncle-bob/2016/01/04/ALittleArchitecture.html)

  01-04-2016
* [Prelude to a Profession](/uncle-bob/2015/11/27/OathDiscussion.html)

  11-27-2015
* [The Programmer's Oath](/uncle-bob/2015/11/18/TheProgrammersOath.html)

  11-18-2015
* [The Force of Pliers](/uncle-bob/2015/11/01/PlierForce.html)

  11-01-2015
* [Future Proof](/uncle-bob/2015/10/30/FutureProof.html)

  10-30-2015
* [Agile is not now, nor was it ever, Waterfall.](/uncle-bob/2015/10/16/Agile-And-Waterfall.html)

  10-16-2015
* [VW](/uncle-bob/2015/10/14/VW.html)

  10-14-2015
* [WATS Line 54](/uncle-bob/2015/10/05/WattsLine54.html)

  10-05-2015
* [A Little Structure](/uncle-bob/2015/09/23/ALittleStructure.html)

  09-23-2015
* [Make the Magic go away.](/uncle-bob/2015/08/06/LetTheMagicDie.html)

  08-06-2015
* [Pattern Pushers](/uncle-bob/2015/07/05/PatternPushers.html)

  07-05-2015
* [The Little Singleton](/uncle-bob/2015/07/01/TheLittleSingleton.html)

  07-01-2015
* [The First Micro-service Architecture](/uncle-bob/2015/05/28/TheFirstMicroserviceArchitecture.html)

  05-28-2015
* [Language Layers](/uncle-bob/2015/04/27/LanguageLayers.html)

  04-27-2015
* [Does Organization Matter?](/uncle-bob/2015/04/15/DoesOrganizationMatter.html)

  04-15-2015
* [The MODE-B Imperative](/uncle-bob/2015/02/21/ModeBImperative.html)

  02-21-2015
* [They Called them Computers.](/uncle-bob/2015/02/19/ComputerHarem.html)

  02-19-2015
* ['Interface' Considered Harmful](/uncle-bob/2015/01/08/InterfaceConsideredHarmful.html)

  01-08-2015
* [The Cycles of TDD](/uncle-bob/2014/12/17/TheCyclesOfTDD.html)

  12-17-2014
* [OO vs FP](/uncle-bob/2014/11/24/FPvsOO.html)

  11-24-2014
* [Thorns around the Gold](/uncle-bob/2014/11/19/GoingForTheGold.html)

  11-19-2014
* [The Obligation of the Programmer.](/uncle-bob/2014/11/15/WeRuleTheWorld.html)

  11-15-2014
* [One Hacker Way!](/uncle-bob/2014/11/12/PutItInProduction.html)

  11-12-2014
* [Laughter in the male dominated room.](/uncle-bob/2014/10/26/LaughterInTheMaleDominatedRoom.html)

  10-26-2014
* [GOML-1, Responsive Design](/uncle-bob/2014/10/08/GOML1-ResponsiveDesign.html)

  10-08-2014
* [Clean Micro-service Architecture](/uncle-bob/2014/10/01/CleanMicroserviceArchitecture.html)

  10-01-2014
* [Microservices and Jars](/uncle-bob/2014/09/19/MicroServicesAndJars.html)

  09-19-2014
* [The More Things Change...](/uncle-bob/2014/09/18/TheMoreThingsChange.html)

  09-18-2014
* [Test Time](/uncle-bob/2014/09/03/TestTime.html)

  09-03-2014
* [A Little About Patterns.](/uncle-bob/2014/06/30/ALittleAboutPatterns.html)

  06-30-2014
* [My Lawn](/uncle-bob/2014/06/20/MyLawn.html)

  06-20-2014
* [Is TDD Dead?](/uncle-bob/2014/06/17/IsTddDeadFinalThoughts.html)

  06-17-2014
* [First](/uncle-bob/2014/05/19/First.html)

  05-19-2014
* [The Little Mocker](/uncle-bob/2014/05/14/TheLittleMocker.html)

  05-14-2014
* [The Open Closed Principle](/uncle-bob/2014/05/12/TheOpenClosedPrinciple.html)

  05-12-2014
* [Framework Bound[2]](/uncle-bob/2014/05/11/FrameworkBound.html)

  05-11-2014
* [When to Mock](/uncle-bob/2014/05/10/WhenToMock.html)

  05-10-2014
* [The Single Responsibility Principle](/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html)

  05-08-2014
* [Professionalism and TDD (Reprise)](/uncle-bob/2014/05/02/ProfessionalismAndTDD.html)

  05-02-2014
* [Test Induced Design Damage?](/uncle-bob/2014/05/01/Design-Damage.html)

  05-01-2014
* [When TDD doesn't work.](/uncle-bob/2014/04/30/When-tdd-does-not-work.html)

  04-30-2014
* [Monogamous TDD](/uncle-bob/2014/04/25/MonogamousTDD.html)

  04-25-2014
* [Code Hoarders](/uncle-bob/2014/04/03/Code-Hoarders.html)

  04-03-2014
* [The *True* Corruption of Agile](/uncle-bob/2014/03/28/The-Corruption-of-Agile.html)

  03-28-2014
* [When Should You Think?](/uncle-bob/2014/03/11/when-to-think.html)

  03-11-2014
* [A Spectrum of Trust](/uncle-bob/2014/02/27/TheTrustSpectrum.html)

  02-27-2014
* [Oh Foreman, Where art Thou?](/uncle-bob/2014/02/23/OhForemanWhereArtThou.html)

  02-23-2014
* [Where is the Foreman?](/uncle-bob/2014/02/21/WhereIsTheForeman.html)

  02-21-2014
* [The Domain Discontinuity](/uncle-bob/2014/01/27/TheChickenOrTheRoad.html)

  01-27-2014
* [Coding in the Clink (9)](/uncle-bob/2014/01/20/Marion_Correctional.html)

  01-20-2014
* [Extreme Programming, a Reflection](/uncle-bob/2013/12/10/Thankyou-Kent.html)

  12-10-2013
* [Novices. A Coda](/uncle-bob/2013/11/25/Novices-Coda.html)

  11-25-2013
* [Hordes Of Novices](/uncle-bob/2013/11/19/HoardsOfNovices.html)

  11-19-2013
* [Healthcare.gov](/uncle-bob/2013/11/12/Healthcare-gov.html)

  11-12-2013
* [The Careless Ones](/uncle-bob/2013/10/24/The-Careless-Ones.html)

  10-24-2013
* [Dance you Imps!](/uncle-bob/2013/10/01/Dance-You-Imps.html)

  10-01-2013
* [A.T. FAIL!](/uncle-bob/2013/09/26/AT-FAIL.html)

  09-26-2013
* [Test First](/uncle-bob/2013/09/23/Test-first.html)

  09-23-2013
* [Transformation Priority and Sorting](/uncle-bob/2013/05/27/TransformationPriorityAndSorting.html)

  05-27-2013
* [The Transformation Priority Premise](/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html)

  05-27-2013
* [Flash - TPP](/uncle-bob/2013/05/27/FlashTpp.html)

  05-27-2013
* [Fib. The T-P Premise.](/uncle-bob/2013/05/27/FibTPP.html)

  05-27-2013
* [There are Ladies Present](/uncle-bob/2013/03/22/There-are-ladies-present.html)

  03-22-2013
* [The Frenzied Panic of Rushing](/uncle-bob/2013/03/11/TheFrenziedPanicOfRushing.html)

  03-11-2013
* [An Open and Closed Case](/uncle-bob/2013/03/08/AnOpenAndClosedCase.html)

  03-08-2013
* [The Pragmatics of TDD](/uncle-bob/2013/03/06/ThePragmaticsOfTDD.html)

  03-06-2013
* [The Start-Up Trap](/uncle-bob/2013/03/05/TheStartUpTrap.html)

  03-05-2013
* [The Principles of Craftsmanship](/uncle-bob/2013/02/10/ThePrinciplesOfCraftsmanship.html)

  02-10-2013
* [The Humble Craftsman](/uncle-bob/2013/02/01/The-Humble-Craftsman.html)

  02-01-2013
* [The Laborer and the Craftsman](/uncle-bob/2013/01/30/The-Craftsman-And-The-Laborer.html)

  01-30-2013
* [FP Basics E4](/uncle-bob/2013/01/29/FPBE4-Lazy-Evaluation.html)

  01-29-2013
* [FP Basics E3](/uncle-bob/2013/01/07/FPBE3-Do-the-rules-change.html)

  01-07-2013
* [FP Basics E2](/uncle-bob/2013/01/02/FPBE2-Whys-it-called-functional.html)

  01-02-2013
* [Brave New Year](/uncle-bob/2012/12/29/Brave-New-Year.html)

  12-29-2012
* [FP Basics E1](/uncle-bob/2012/12/22/FPBE1-Whats-it-all-about.html)

  12-22-2012
* [Three Paradigms](/uncle-bob/2012/12/19/Three-Paradigms.html)

  12-19-2012
* [The New CTO](/uncle-bob/2012/09/06/I-am-Your-New-CTO.html)

  09-06-2012
* [Functional Programming for the Object Oriented Programmer](/uncle-bob/2012/08/24/functional-programming-for-the-object-oriented-programmer.html)

  08-24-2012
* [The Clean Architecture](/uncle-bob/2012/08/13/the-clean-architecture.html)

  08-13-2012
* [NO DB](/uncle-bob/2012/05/15/NODB.html)

  05-15-2012
* [Why is Estimating so Hard?](/uncle-bob/2012/04/20/Why-Is-Estimating-So-Hard.html)

  04-20-2012
* [After the Disaster](/uncle-bob/2012/04/18/After-The-Disaster.html)

  04-18-2012
* [Service Oriented Agony](/uncle-bob/2012/02/01/Service-Oriented-Agony.html)

  02-01-2012
* [The Ruby Colored Box](/uncle-bob/2012/01/31/The-Ruby-Colored-Box.html)

  01-31-2012
* [Fecophiles](/uncle-bob/2012/01/20/Fecophiles.html)

  01-20-2012
* [The Letter](/uncle-bob/2012/01/12/The-Letter.html)

  01-12-2012
* [Flipping the Bit](/uncle-bob/2012/01/11/Flipping-the-Bit.html)

  01-11-2012
* [The Barbarians are at the Gates](/uncle-bob/2011/12/11/The-Barbarians-are-at-the-Gates.html)

  12-11-2011
* [Clean Architecture](/uncle-bob/2011/11/22/Clean-Architecture.html)

  11-22-2011
* [Double Entry Bookkeeping Dilemma. Should I Invest or Not?](/uncle-bob/2011/11/06/Double-Entry-Bookkeeping-Dilemma-Should-I-Invest-or-Not.html)

  11-06-2011
* [Simple Hickey](/uncle-bob/2011/10/20/Simple-Hickey.html)

  10-20-2011
* [Screaming Architecture](/uncle-bob/2011/09/30/Screaming-Architecture.html)

  09-30-2011
* [Bringing Balance to the Force](/uncle-bob/2011/01/19/individuals-and-interactions.html)

  01-19-2011
* [What Software Craftsmanship is about](/uncle-bob/2011/01/17/software-craftsmanship-is-about.html)

  01-17-2011

---

## Source: uncle-bob_2012_08_13_the-clean-architecture.html.md

Clean Coder Blog


[![](/assets/clean_code_72_color.png)](/)

# The Clean Code Blog

by Robert C. Martin (Uncle Bob)



[atom/rss feed](/atom.xml)


---

* [Functional Classes in Clojure](/uncle-bob/2023/01/19/functional-classes-clojure.html)

  01-19-2023
* [Functional Classes](/uncle-bob/2023/01/18/functional-classes.html)

  01-18-2023
* [Space War](/uncle-bob/2021/11/28/Spacewar.html)

  11-28-2021
* [Functional Duplications](/uncle-bob/2021/10/28/functional-duplication.html)

  10-28-2021
* [Roots](/uncle-bob/2021/09/25/roots.html)

  09-25-2021
* [More On Types](/uncle-bob/2021/06/29/MoreOnTypes.html)

  06-29-2021
* [On Types](/uncle-bob/2021/06/25/OnTypes.html)

  06-25-2021
* [if-else-switch](/uncle-bob/2021/03/06/ifElseSwitch.html)

  03-06-2021
* [Pairing Guidelines](/uncle-bob/2021/01/17/Pairing.html)

  01-17-2021
* [Solid Relevance](/uncle-bob/2020/10/18/Solid-Relevance.html)

  10-18-2020
* [Loopy](/uncle-bob/2020/09/30/loopy.html)

  09-30-2020
* [Conference Conduct](/uncle-bob/2020/09/23/ConferenceConduct.html)

  09-23-2020
* [The Disinvitation](/uncle-bob/2020/09/12/TheDisinvitation.html)

  09-12-2020
* [REPL Driven Design](/uncle-bob/2020/05/27/ReplDrivenDesign.html)

  05-27-2020
* [A Little More Clojure](/uncle-bob/2020/04/09/ALittleMoreClojure.html)

  04-09-2020
* [A Little Clojure](/uncle-bob/2020/04/06/ALittleClojure.html)

  04-06-2020
* [A New Hope](/uncle-bob/2020/04/05/ANewHope.html)

  04-05-2020
* [Open Letter to the Linux Foundation](/uncle-bob/2019/11/08/OpenLetterLinuxFoundation.html)

  11-08-2019
* [What They Thought of Programmers.](/uncle-bob/2019/11/03/WhatTheyThoughtOfUs.html)

  11-03-2019
* [Circulatory](/uncle-bob/2019/10/31/Circulatory.html)

  10-31-2019
* [Why Clojure?](/uncle-bob/2019/08/22/WhyClojure.html)

  08-22-2019
* [Why won't it...](/uncle-bob/2019/07/22/WhyWontIt.html)

  07-22-2019
* [Classes vs. Data Structures](/uncle-bob/2019/06/16/ObjectsAndDataStructures.html)

  06-16-2019
* [Types and Tests](/uncle-bob/2019/06/08/TestsAndTypes.html)

  06-08-2019
* [737 Max 8](/uncle-bob/2019/05/18/737-Max-8.html)

  05-18-2019
* [FP vs. OO List Processing](/uncle-bob/2018/12/17/FPvsOO-List-processing.html)

  12-17-2018
* [We, The Unoffended](/uncle-bob/2018/12/16/unoffended.html)

  12-16-2018
* [SJWJS](/uncle-bob/2018/12/14/SJWJS.html)

  12-14-2018
* [The Tragedy of Craftsmanship.](/uncle-bob/2018/08/28/CraftsmanshipMovement.html)

  08-28-2018
* [Too Clean?](/uncle-bob/2018/08/13/TooClean.html)

  08-13-2018
* [Integers and Estimates](/uncle-bob/2018/06/21/IntegersAndEstimates.html)

  06-21-2018
* [Pickled State](/uncle-bob/2018/06/06/PickledState.html)

  06-06-2018
* [Craftsman, Craftswoman, Craftsperson](/uncle-bob/2018/05/02/Craftsman-Craftswoman-Craftsperson.html)

  05-02-2018
* [FP vs. OO](/uncle-bob/2018/04/13/FPvsOO.html)

  04-13-2018
* [In The Large](/uncle-bob/2018/04/02/InTheLarge.html)

  04-02-2018
* [*We Programmers*](/uncle-bob/2018/03/29/WeProgrammers.html)

  03-29-2018
* [Uncle Bob Fly-In.  
  Have I got a deal for you!](/uncle-bob/2018/02/25/UncleBobFlyIn.html)

  02-25-2018
* [The Citizenship Argument](/uncle-bob/2018/01/18/TheCitizenshipArgument.html)

  01-18-2018
* [Operating Behind the Power Curve](/uncle-bob/2018/01/15/behindThePowerCurve.html)

  01-15-2018
* [Excuses](/uncle-bob/2017/12/18/Excuses.html)

  12-18-2017
* [Dbtails](/uncle-bob/2017/12/09/Dbtails.html)

  12-09-2017
* [Bobby Tables](/uncle-bob/2017/12/03/BobbyTables.html)

  12-03-2017
* [Living on the Plateau](/uncle-bob/2017/11/18/OnThePlateau.html)

  11-18-2017
* [Women In Demand](/uncle-bob/2017/10/04/WomenInDemand.html)

  10-04-2017
* [Tools are not the Answer](/uncle-bob/2017/10/04/CodeIsNotTheAnswer.html)

  10-04-2017
* [Test Contra-variance](/uncle-bob/2017/10/03/TestContravariance.html)

  10-03-2017
* [The Unscrupulous Meme](/uncle-bob/2017/09/29/TheUnscrupulousMeme.html)

  09-29-2017
* [Sierra Juliet Foxtrot](/uncle-bob/2017/09/26/SierraJulietFoxtrot.html)

  09-26-2017
* [Just Following Orders](/uncle-bob/2017/08/28/JustFollowingOders.html)

  08-28-2017
* [Women in Tech](/uncle-bob/2017/08/14/WomenInTech.html)

  08-14-2017
* [On the Diminished Capacity to Discuss Things Rationally](/uncle-bob/2017/08/10/OnTheInabilityToDiscussThingsRationally.html)

  08-10-2017
* [Thought Police](/uncle-bob/2017/08/09/ThoughtPolice.html)

  08-09-2017
* [The Brain Problem](/uncle-bob/2017/07/28/TheBrainProblem.html)

  07-28-2017
* [Drive me to Toronto, Hal.](/uncle-bob/2017/07/24/DriveMeToTorontoHal.html)

  07-24-2017
* [Pragmatic Functional Programming](/uncle-bob/2017/07/11/PragmaticFunctionalProgramming.html)

  07-11-2017
* [First-Class Tests.](/uncle-bob/2017/05/05/TestDefinitions.html)

  05-05-2017
* [Is Dr. Calvin in the Room?](/uncle-bob/2017/03/16/DrCalvin.html)

  03-16-2017
* [Symmetry Breaking](/uncle-bob/2017/03/07/SymmetryBreaking.html)

  03-07-2017
* [Testing Like the TSA](/uncle-bob/2017/03/06/TestingLikeTheTSA.html)

  03-06-2017
* [TDD Harms Architecture](/uncle-bob/2017/03/03/TDD-Harms-Architecture.html)

  03-03-2017
* [Necessary Comments](/uncle-bob/2017/02/23/NecessaryComments.html)

  02-23-2017
* [Types and Tests](/uncle-bob/2017/01/13/TypesAndTests.html)

  01-13-2017
* [The Dark Path](/uncle-bob/2017/01/11/TheDarkPath.html)

  01-11-2017
* [TDD Lesson - Terrain Generation](/uncle-bob/2017/01/09/DiamondSquare.html)

  01-09-2017
* [TDD Doesn't Work](/uncle-bob/2016/11/10/TDD-Doesnt-work.html)

  11-10-2016
* [Dijkstra's Algorithm](/uncle-bob/2016/10/26/DijkstrasAlg.html)

  10-26-2016
* [The Lurn](/uncle-bob/2016/09/01/TheLurn.html)

  09-01-2016
* [The Churn](/uncle-bob/2016/07/27/TheChurn.html)

  07-27-2016
* [Mutation Testing](/uncle-bob/2016/06/10/MutationTesting.html)

  06-10-2016
* [Blue. No! Yellow!](/uncle-bob/2016/05/21/BlueNoYellow.html)

  05-21-2016
* [Type Wars](/uncle-bob/2016/05/01/TypeWars.html)

  05-01-2016
* [Giving Up on TDD](/uncle-bob/2016/03/19/GivingUpOnTDD.html)

  03-19-2016
* [Manhandled](/uncle-bob/2016/01/15/Manhandled.html)

  01-15-2016
* [Stabilization Phases](/uncle-bob/2016/01/14/Stabilization.html)

  01-14-2016
* [A Little Architecture](/uncle-bob/2016/01/04/ALittleArchitecture.html)

  01-04-2016
* [Prelude to a Profession](/uncle-bob/2015/11/27/OathDiscussion.html)

  11-27-2015
* [The Programmer's Oath](/uncle-bob/2015/11/18/TheProgrammersOath.html)

  11-18-2015
* [The Force of Pliers](/uncle-bob/2015/11/01/PlierForce.html)

  11-01-2015
* [Future Proof](/uncle-bob/2015/10/30/FutureProof.html)

  10-30-2015
* [Agile is not now, nor was it ever, Waterfall.](/uncle-bob/2015/10/16/Agile-And-Waterfall.html)

  10-16-2015
* [VW](/uncle-bob/2015/10/14/VW.html)

  10-14-2015
* [WATS Line 54](/uncle-bob/2015/10/05/WattsLine54.html)

  10-05-2015
* [A Little Structure](/uncle-bob/2015/09/23/ALittleStructure.html)

  09-23-2015
* [Make the Magic go away.](/uncle-bob/2015/08/06/LetTheMagicDie.html)

  08-06-2015
* [Pattern Pushers](/uncle-bob/2015/07/05/PatternPushers.html)

  07-05-2015
* [The Little Singleton](/uncle-bob/2015/07/01/TheLittleSingleton.html)

  07-01-2015
* [The First Micro-service Architecture](/uncle-bob/2015/05/28/TheFirstMicroserviceArchitecture.html)

  05-28-2015
* [Language Layers](/uncle-bob/2015/04/27/LanguageLayers.html)

  04-27-2015
* [Does Organization Matter?](/uncle-bob/2015/04/15/DoesOrganizationMatter.html)

  04-15-2015
* [The MODE-B Imperative](/uncle-bob/2015/02/21/ModeBImperative.html)

  02-21-2015
* [They Called them Computers.](/uncle-bob/2015/02/19/ComputerHarem.html)

  02-19-2015
* ['Interface' Considered Harmful](/uncle-bob/2015/01/08/InterfaceConsideredHarmful.html)

  01-08-2015
* [The Cycles of TDD](/uncle-bob/2014/12/17/TheCyclesOfTDD.html)

  12-17-2014
* [OO vs FP](/uncle-bob/2014/11/24/FPvsOO.html)

  11-24-2014
* [Thorns around the Gold](/uncle-bob/2014/11/19/GoingForTheGold.html)

  11-19-2014
* [The Obligation of the Programmer.](/uncle-bob/2014/11/15/WeRuleTheWorld.html)

  11-15-2014
* [One Hacker Way!](/uncle-bob/2014/11/12/PutItInProduction.html)

  11-12-2014
* [Laughter in the male dominated room.](/uncle-bob/2014/10/26/LaughterInTheMaleDominatedRoom.html)

  10-26-2014
* [GOML-1, Responsive Design](/uncle-bob/2014/10/08/GOML1-ResponsiveDesign.html)

  10-08-2014
* [Clean Micro-service Architecture](/uncle-bob/2014/10/01/CleanMicroserviceArchitecture.html)

  10-01-2014
* [Microservices and Jars](/uncle-bob/2014/09/19/MicroServicesAndJars.html)

  09-19-2014
* [The More Things Change...](/uncle-bob/2014/09/18/TheMoreThingsChange.html)

  09-18-2014
* [Test Time](/uncle-bob/2014/09/03/TestTime.html)

  09-03-2014
* [A Little About Patterns.](/uncle-bob/2014/06/30/ALittleAboutPatterns.html)

  06-30-2014
* [My Lawn](/uncle-bob/2014/06/20/MyLawn.html)

  06-20-2014
* [Is TDD Dead?](/uncle-bob/2014/06/17/IsTddDeadFinalThoughts.html)

  06-17-2014
* [First](/uncle-bob/2014/05/19/First.html)

  05-19-2014
* [The Little Mocker](/uncle-bob/2014/05/14/TheLittleMocker.html)

  05-14-2014
* [The Open Closed Principle](/uncle-bob/2014/05/12/TheOpenClosedPrinciple.html)

  05-12-2014
* [Framework Bound[2]](/uncle-bob/2014/05/11/FrameworkBound.html)

  05-11-2014
* [When to Mock](/uncle-bob/2014/05/10/WhenToMock.html)

  05-10-2014
* [The Single Responsibility Principle](/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html)

  05-08-2014
* [Professionalism and TDD (Reprise)](/uncle-bob/2014/05/02/ProfessionalismAndTDD.html)

  05-02-2014
* [Test Induced Design Damage?](/uncle-bob/2014/05/01/Design-Damage.html)

  05-01-2014
* [When TDD doesn't work.](/uncle-bob/2014/04/30/When-tdd-does-not-work.html)

  04-30-2014
* [Monogamous TDD](/uncle-bob/2014/04/25/MonogamousTDD.html)

  04-25-2014
* [Code Hoarders](/uncle-bob/2014/04/03/Code-Hoarders.html)

  04-03-2014
* [The *True* Corruption of Agile](/uncle-bob/2014/03/28/The-Corruption-of-Agile.html)

  03-28-2014
* [When Should You Think?](/uncle-bob/2014/03/11/when-to-think.html)

  03-11-2014
* [A Spectrum of Trust](/uncle-bob/2014/02/27/TheTrustSpectrum.html)

  02-27-2014
* [Oh Foreman, Where art Thou?](/uncle-bob/2014/02/23/OhForemanWhereArtThou.html)

  02-23-2014
* [Where is the Foreman?](/uncle-bob/2014/02/21/WhereIsTheForeman.html)

  02-21-2014
* [The Domain Discontinuity](/uncle-bob/2014/01/27/TheChickenOrTheRoad.html)

  01-27-2014
* [Coding in the Clink (9)](/uncle-bob/2014/01/20/Marion_Correctional.html)

  01-20-2014
* [Extreme Programming, a Reflection](/uncle-bob/2013/12/10/Thankyou-Kent.html)

  12-10-2013
* [Novices. A Coda](/uncle-bob/2013/11/25/Novices-Coda.html)

  11-25-2013
* [Hordes Of Novices](/uncle-bob/2013/11/19/HoardsOfNovices.html)

  11-19-2013
* [Healthcare.gov](/uncle-bob/2013/11/12/Healthcare-gov.html)

  11-12-2013
* [The Careless Ones](/uncle-bob/2013/10/24/The-Careless-Ones.html)

  10-24-2013
* [Dance you Imps!](/uncle-bob/2013/10/01/Dance-You-Imps.html)

  10-01-2013
* [A.T. FAIL!](/uncle-bob/2013/09/26/AT-FAIL.html)

  09-26-2013
* [Test First](/uncle-bob/2013/09/23/Test-first.html)

  09-23-2013
* [Transformation Priority and Sorting](/uncle-bob/2013/05/27/TransformationPriorityAndSorting.html)

  05-27-2013
* [The Transformation Priority Premise](/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html)

  05-27-2013
* [Flash - TPP](/uncle-bob/2013/05/27/FlashTpp.html)

  05-27-2013
* [Fib. The T-P Premise.](/uncle-bob/2013/05/27/FibTPP.html)

  05-27-2013
* [There are Ladies Present](/uncle-bob/2013/03/22/There-are-ladies-present.html)

  03-22-2013
* [The Frenzied Panic of Rushing](/uncle-bob/2013/03/11/TheFrenziedPanicOfRushing.html)

  03-11-2013
* [An Open and Closed Case](/uncle-bob/2013/03/08/AnOpenAndClosedCase.html)

  03-08-2013
* [The Pragmatics of TDD](/uncle-bob/2013/03/06/ThePragmaticsOfTDD.html)

  03-06-2013
* [The Start-Up Trap](/uncle-bob/2013/03/05/TheStartUpTrap.html)

  03-05-2013
* [The Principles of Craftsmanship](/uncle-bob/2013/02/10/ThePrinciplesOfCraftsmanship.html)

  02-10-2013
* [The Humble Craftsman](/uncle-bob/2013/02/01/The-Humble-Craftsman.html)

  02-01-2013
* [The Laborer and the Craftsman](/uncle-bob/2013/01/30/The-Craftsman-And-The-Laborer.html)

  01-30-2013
* [FP Basics E4](/uncle-bob/2013/01/29/FPBE4-Lazy-Evaluation.html)

  01-29-2013
* [FP Basics E3](/uncle-bob/2013/01/07/FPBE3-Do-the-rules-change.html)

  01-07-2013
* [FP Basics E2](/uncle-bob/2013/01/02/FPBE2-Whys-it-called-functional.html)

  01-02-2013
* [Brave New Year](/uncle-bob/2012/12/29/Brave-New-Year.html)

  12-29-2012
* [FP Basics E1](/uncle-bob/2012/12/22/FPBE1-Whats-it-all-about.html)

  12-22-2012
* [Three Paradigms](/uncle-bob/2012/12/19/Three-Paradigms.html)

  12-19-2012
* [The New CTO](/uncle-bob/2012/09/06/I-am-Your-New-CTO.html)

  09-06-2012
* [Functional Programming for the Object Oriented Programmer](/uncle-bob/2012/08/24/functional-programming-for-the-object-oriented-programmer.html)

  08-24-2012
* [The Clean Architecture](/uncle-bob/2012/08/13/the-clean-architecture.html)

  08-13-2012
* [NO DB](/uncle-bob/2012/05/15/NODB.html)

  05-15-2012
* [Why is Estimating so Hard?](/uncle-bob/2012/04/20/Why-Is-Estimating-So-Hard.html)

  04-20-2012
* [After the Disaster](/uncle-bob/2012/04/18/After-The-Disaster.html)

  04-18-2012
* [Service Oriented Agony](/uncle-bob/2012/02/01/Service-Oriented-Agony.html)

  02-01-2012
* [The Ruby Colored Box](/uncle-bob/2012/01/31/The-Ruby-Colored-Box.html)

  01-31-2012
* [Fecophiles](/uncle-bob/2012/01/20/Fecophiles.html)

  01-20-2012
* [The Letter](/uncle-bob/2012/01/12/The-Letter.html)

  01-12-2012
* [Flipping the Bit](/uncle-bob/2012/01/11/Flipping-the-Bit.html)

  01-11-2012
* [The Barbarians are at the Gates](/uncle-bob/2011/12/11/The-Barbarians-are-at-the-Gates.html)

  12-11-2011
* [Clean Architecture](/uncle-bob/2011/11/22/Clean-Architecture.html)

  11-22-2011
* [Double Entry Bookkeeping Dilemma. Should I Invest or Not?](/uncle-bob/2011/11/06/Double-Entry-Bookkeeping-Dilemma-Should-I-Invest-or-Not.html)

  11-06-2011
* [Simple Hickey](/uncle-bob/2011/10/20/Simple-Hickey.html)

  10-20-2011
* [Screaming Architecture](/uncle-bob/2011/09/30/Screaming-Architecture.html)

  09-30-2011
* [Bringing Balance to the Force](/uncle-bob/2011/01/19/individuals-and-interactions.html)

  01-19-2011
* [What Software Craftsmanship is about](/uncle-bob/2011/01/17/software-craftsmanship-is-about.html)

  01-17-2011

# The Clean Architecture

13 August 2012

![](/uncle-bob/images/2012-08-13-the-clean-architecture/CleanArchitecture.jpg)

Over the last several years we’ve seen a whole range of ideas regarding the architecture of systems. These include:

* [Hexagonal Architecture](http://alistair.cockburn.us/Hexagonal+architecture) (a.k.a. Ports and Adapters) by Alistair Cockburn and adopted by Steve Freeman, and Nat Pryce in their wonderful book [Growing Object Oriented Software](http://www.amazon.com/Growing-Object-Oriented-Software-Guided-Tests/dp/0321503627)
* [Onion Architecture](http://jeffreypalermo.com/blog/the-onion-architecture-part-1/) by Jeffrey Palermo
* [Screaming Architecture](http://blog.cleancoders.com/2011-09-30-Screaming-Architecture) from a blog of mine last year
* [DCI](http://www.amazon.com/Lean-Architecture-Agile-Software-Development/dp/0470684208/) from James Coplien, and Trygve Reenskaug.
* [BCE](http://www.amazon.com/Object-Oriented-Software-Engineering-Approach/dp/0201544350) by Ivar Jacobson from his book *Object Oriented Software Engineering: A Use-Case Driven Approach*

Though these architectures all vary somewhat in their details, they are very similar. They all have the same objective, which is the separation of concerns. They all achieve this separation by dividing the software into layers. Each has at least one layer for business rules, and another for interfaces.

Each of these architectures produce systems that are:

1. Independent of Frameworks. The architecture does not depend on the existence of some library of feature laden software. This allows you to use such frameworks as tools, rather than having to cram your system into their limited constraints.
2. Testable. The business rules can be tested without the UI, Database, Web Server, or any other external element.
3. Independent of UI. The UI can change easily, without changing the rest of the system. A Web UI could be replaced with a console UI, for example, without changing the business rules.
4. Independent of Database. You can swap out Oracle or SQL Server, for Mongo, BigTable, CouchDB, or something else. Your business rules are not bound to the database.
5. Independent of any external agency. In fact your business rules simply don’t know anything at all about the outside world.

The diagram at the top of this article is an attempt at integrating all these architectures into a single actionable idea.

## The Dependency Rule

The concentric circles represent different areas of software. In general, the further in you go, the higher level the software becomes. The outer circles are mechanisms. The inner circles are policies.

The overriding rule that makes this architecture work is *The Dependency Rule*. This rule says that *source code dependencies* can only point *inwards*. Nothing in an inner circle can know anything at all about something in an outer circle. In particular, the name of something declared in an outer circle must not be mentioned by the code in the an inner circle. That includes, functions, classes. variables, or any other named software entity.

By the same token, data formats used in an outer circle should not be used by an inner circle, especially if those formats are generate by a framework in an outer circle. We don’t want anything in an outer circle to impact the inner circles.

## *Entities*

Entities encapsulate *Enterprise wide* business rules. An entity can be an object with methods, or it can be a set of data structures and functions. It doesn’t matter so long as the entities could be used by many different applications in the enterprise.

If you don’t have an enterprise, and are just writing a single application, then these entities are the business objects of the application. They encapsulate the most general and high-level rules. They are the least likely to change when something external changes. For example, you would not expect these objects to be affected by a change to page navigation, or security. No operational change to any particular application should affect the entity layer.

## Use Cases

The software in this layer contains *application specific* business rules. It encapsulates and implements all of the use cases of the system. These use cases orchestrate the flow of data to and from the entities, and direct those entities to use their *enterprise wide* business rules to achieve the goals of the use case.

We do not expect changes in this layer to affect the entities. We also do not expect this layer to be affected by changes to externalities such as the database, the UI, or any of the common frameworks. This layer is isolated from such concerns.

We *do*, however, expect that changes to the operation of the application *will* affect the use-cases and therefore the software in this layer. If the details of a use-case change, then some code in this layer will certainly be affected.

## Interface Adapters

The software in this layer is a set of adapters that convert data from the format most convenient for the use cases and entities, to the format most convenient for some external agency such as the Database or the Web. It is this layer, for example, that will wholly contain the MVC architecture of a GUI. The Presenters, Views, and Controllers all belong in here. The models are likely just data structures that are passed from the controllers to the use cases, and then back from the use cases to the presenters and views.

Similarly, data is converted, in this layer, from the form most convenient for entities and use cases, into the form most convenient for whatever persistence framework is being used. i.e. The Database. No code inward of this circle should know anything at all about the database. If the database is a SQL database, then all the SQL should be restricted to this layer, and in particular to the parts of this layer that have to do with the database.

Also in this layer is any other adapter necessary to convert data from some external form, such as an external service, to the internal form used by the use cases and entities.

## Frameworks and Drivers.

The outermost layer is generally composed of frameworks and tools such as the Database, the Web Framework, etc. Generally you don’t write much code in this layer other than glue code that communicates to the next circle inwards.

This layer is where all the details go. The Web is a detail. The database is a detail. We keep these things on the outside where they can do little harm.

## Only Four Circles?

No, the circles are schematic. You may find that you need more than just these four. There’s no rule that says you must always have just these four. However, *The Dependency Rule* always applies. Source code dependencies always point inwards. As you move inwards the level of abstraction increases. The outermost circle is low level concrete detail. As you move inwards the software grows more abstract, and encapsulates higher level policies. The inner most circle is the most general.

## Crossing boundaries.

At the lower right of the diagram is an example of how we cross the circle boundaries. It shows the Controllers and Presenters communicating with the Use Cases in the next layer. Note the flow of control. It begins in the controller, moves through the use case, and then winds up executing in the presenter. Note also the source code dependencies. Each one of them points inwards towards the use cases.

We usually resolve this apparent contradiction by using the [Dependency Inversion Principle](http://en.wikipedia.org/wiki/Dependency_inversion_principle). In a language like Java, for example, we would arrange interfaces and inheritance relationships such that the source code dependencies oppose the flow of control at just the right points across the boundary.

For example, consider that the use case needs to call the presenter. However, this call must not be direct because that would violate *The Dependency Rule*: No name in an outer circle can be mentioned by an inner circle. So we have the use case call an interface (Shown here as Use Case Output Port) in the inner circle, and have the presenter in the outer circle implement it.

The same technique is used to cross all the boundaries in the architectures. We take advantage of dynamic polymorphism to create source code dependencies that oppose the flow of control so that we can conform to *The Dependency Rule* no matter what direction the flow of control is going in.

## What data crosses the boundaries.

Typically the data that crosses the boundaries is simple data structures. You can use basic structs or simple Data Transfer objects if you like. Or the data can simply be arguments in function calls. Or you can pack it into a hashmap, or construct it into an object. The important thing is that isolated, simple, data structures are passed across the boundaries. We don’t want to cheat and pass *Entities* or Database rows. We don’t want the data structures to have any kind of dependency that violates *The Dependency Rule*.

For example, many database frameworks return a convenient data format in response to a query. We might call this a RowStructure. We don’t want to pass that row structure inwards across a boundary. That would violate *The Dependency Rule* because it would force an inner circle to know something about an outer circle.

So when we pass data across a boundary, it is always in the form that is most convenient for the inner circle.

## Conclusion

Conforming to these simple rules is not hard, and will save you a lot of headaches going forward. By separating the software into layers, and conforming to *The Dependency Rule*, you will create a system that is intrinsically testable, with all the benefits that implies. When any of the external parts of the system become obsolete, like the database, or the web framework, you can replace those obsolete elements with a minimum of fuss.

---

## Source: uncle-bob_2023_01_18_functional-classes.html.md

Clean Coder Blog


[![](/assets/clean_code_72_color.png)](/)

# The Clean Code Blog

by Robert C. Martin (Uncle Bob)



[atom/rss feed](/atom.xml)


---

* [Functional Classes in Clojure](/uncle-bob/2023/01/19/functional-classes-clojure.html)

  01-19-2023
* [Functional Classes](/uncle-bob/2023/01/18/functional-classes.html)

  01-18-2023
* [Space War](/uncle-bob/2021/11/28/Spacewar.html)

  11-28-2021
* [Functional Duplications](/uncle-bob/2021/10/28/functional-duplication.html)

  10-28-2021
* [Roots](/uncle-bob/2021/09/25/roots.html)

  09-25-2021
* [More On Types](/uncle-bob/2021/06/29/MoreOnTypes.html)

  06-29-2021
* [On Types](/uncle-bob/2021/06/25/OnTypes.html)

  06-25-2021
* [if-else-switch](/uncle-bob/2021/03/06/ifElseSwitch.html)

  03-06-2021
* [Pairing Guidelines](/uncle-bob/2021/01/17/Pairing.html)

  01-17-2021
* [Solid Relevance](/uncle-bob/2020/10/18/Solid-Relevance.html)

  10-18-2020
* [Loopy](/uncle-bob/2020/09/30/loopy.html)

  09-30-2020
* [Conference Conduct](/uncle-bob/2020/09/23/ConferenceConduct.html)

  09-23-2020
* [The Disinvitation](/uncle-bob/2020/09/12/TheDisinvitation.html)

  09-12-2020
* [REPL Driven Design](/uncle-bob/2020/05/27/ReplDrivenDesign.html)

  05-27-2020
* [A Little More Clojure](/uncle-bob/2020/04/09/ALittleMoreClojure.html)

  04-09-2020
* [A Little Clojure](/uncle-bob/2020/04/06/ALittleClojure.html)

  04-06-2020
* [A New Hope](/uncle-bob/2020/04/05/ANewHope.html)

  04-05-2020
* [Open Letter to the Linux Foundation](/uncle-bob/2019/11/08/OpenLetterLinuxFoundation.html)

  11-08-2019
* [What They Thought of Programmers.](/uncle-bob/2019/11/03/WhatTheyThoughtOfUs.html)

  11-03-2019
* [Circulatory](/uncle-bob/2019/10/31/Circulatory.html)

  10-31-2019
* [Why Clojure?](/uncle-bob/2019/08/22/WhyClojure.html)

  08-22-2019
* [Why won't it...](/uncle-bob/2019/07/22/WhyWontIt.html)

  07-22-2019
* [Classes vs. Data Structures](/uncle-bob/2019/06/16/ObjectsAndDataStructures.html)

  06-16-2019
* [Types and Tests](/uncle-bob/2019/06/08/TestsAndTypes.html)

  06-08-2019
* [737 Max 8](/uncle-bob/2019/05/18/737-Max-8.html)

  05-18-2019
* [FP vs. OO List Processing](/uncle-bob/2018/12/17/FPvsOO-List-processing.html)

  12-17-2018
* [We, The Unoffended](/uncle-bob/2018/12/16/unoffended.html)

  12-16-2018
* [SJWJS](/uncle-bob/2018/12/14/SJWJS.html)

  12-14-2018
* [The Tragedy of Craftsmanship.](/uncle-bob/2018/08/28/CraftsmanshipMovement.html)

  08-28-2018
* [Too Clean?](/uncle-bob/2018/08/13/TooClean.html)

  08-13-2018
* [Integers and Estimates](/uncle-bob/2018/06/21/IntegersAndEstimates.html)

  06-21-2018
* [Pickled State](/uncle-bob/2018/06/06/PickledState.html)

  06-06-2018
* [Craftsman, Craftswoman, Craftsperson](/uncle-bob/2018/05/02/Craftsman-Craftswoman-Craftsperson.html)

  05-02-2018
* [FP vs. OO](/uncle-bob/2018/04/13/FPvsOO.html)

  04-13-2018
* [In The Large](/uncle-bob/2018/04/02/InTheLarge.html)

  04-02-2018
* [*We Programmers*](/uncle-bob/2018/03/29/WeProgrammers.html)

  03-29-2018
* [Uncle Bob Fly-In.  
  Have I got a deal for you!](/uncle-bob/2018/02/25/UncleBobFlyIn.html)

  02-25-2018
* [The Citizenship Argument](/uncle-bob/2018/01/18/TheCitizenshipArgument.html)

  01-18-2018
* [Operating Behind the Power Curve](/uncle-bob/2018/01/15/behindThePowerCurve.html)

  01-15-2018
* [Excuses](/uncle-bob/2017/12/18/Excuses.html)

  12-18-2017
* [Dbtails](/uncle-bob/2017/12/09/Dbtails.html)

  12-09-2017
* [Bobby Tables](/uncle-bob/2017/12/03/BobbyTables.html)

  12-03-2017
* [Living on the Plateau](/uncle-bob/2017/11/18/OnThePlateau.html)

  11-18-2017
* [Women In Demand](/uncle-bob/2017/10/04/WomenInDemand.html)

  10-04-2017
* [Tools are not the Answer](/uncle-bob/2017/10/04/CodeIsNotTheAnswer.html)

  10-04-2017
* [Test Contra-variance](/uncle-bob/2017/10/03/TestContravariance.html)

  10-03-2017
* [The Unscrupulous Meme](/uncle-bob/2017/09/29/TheUnscrupulousMeme.html)

  09-29-2017
* [Sierra Juliet Foxtrot](/uncle-bob/2017/09/26/SierraJulietFoxtrot.html)

  09-26-2017
* [Just Following Orders](/uncle-bob/2017/08/28/JustFollowingOders.html)

  08-28-2017
* [Women in Tech](/uncle-bob/2017/08/14/WomenInTech.html)

  08-14-2017
* [On the Diminished Capacity to Discuss Things Rationally](/uncle-bob/2017/08/10/OnTheInabilityToDiscussThingsRationally.html)

  08-10-2017
* [Thought Police](/uncle-bob/2017/08/09/ThoughtPolice.html)

  08-09-2017
* [The Brain Problem](/uncle-bob/2017/07/28/TheBrainProblem.html)

  07-28-2017
* [Drive me to Toronto, Hal.](/uncle-bob/2017/07/24/DriveMeToTorontoHal.html)

  07-24-2017
* [Pragmatic Functional Programming](/uncle-bob/2017/07/11/PragmaticFunctionalProgramming.html)

  07-11-2017
* [First-Class Tests.](/uncle-bob/2017/05/05/TestDefinitions.html)

  05-05-2017
* [Is Dr. Calvin in the Room?](/uncle-bob/2017/03/16/DrCalvin.html)

  03-16-2017
* [Symmetry Breaking](/uncle-bob/2017/03/07/SymmetryBreaking.html)

  03-07-2017
* [Testing Like the TSA](/uncle-bob/2017/03/06/TestingLikeTheTSA.html)

  03-06-2017
* [TDD Harms Architecture](/uncle-bob/2017/03/03/TDD-Harms-Architecture.html)

  03-03-2017
* [Necessary Comments](/uncle-bob/2017/02/23/NecessaryComments.html)

  02-23-2017
* [Types and Tests](/uncle-bob/2017/01/13/TypesAndTests.html)

  01-13-2017
* [The Dark Path](/uncle-bob/2017/01/11/TheDarkPath.html)

  01-11-2017
* [TDD Lesson - Terrain Generation](/uncle-bob/2017/01/09/DiamondSquare.html)

  01-09-2017
* [TDD Doesn't Work](/uncle-bob/2016/11/10/TDD-Doesnt-work.html)

  11-10-2016
* [Dijkstra's Algorithm](/uncle-bob/2016/10/26/DijkstrasAlg.html)

  10-26-2016
* [The Lurn](/uncle-bob/2016/09/01/TheLurn.html)

  09-01-2016
* [The Churn](/uncle-bob/2016/07/27/TheChurn.html)

  07-27-2016
* [Mutation Testing](/uncle-bob/2016/06/10/MutationTesting.html)

  06-10-2016
* [Blue. No! Yellow!](/uncle-bob/2016/05/21/BlueNoYellow.html)

  05-21-2016
* [Type Wars](/uncle-bob/2016/05/01/TypeWars.html)

  05-01-2016
* [Giving Up on TDD](/uncle-bob/2016/03/19/GivingUpOnTDD.html)

  03-19-2016
* [Manhandled](/uncle-bob/2016/01/15/Manhandled.html)

  01-15-2016
* [Stabilization Phases](/uncle-bob/2016/01/14/Stabilization.html)

  01-14-2016
* [A Little Architecture](/uncle-bob/2016/01/04/ALittleArchitecture.html)

  01-04-2016
* [Prelude to a Profession](/uncle-bob/2015/11/27/OathDiscussion.html)

  11-27-2015
* [The Programmer's Oath](/uncle-bob/2015/11/18/TheProgrammersOath.html)

  11-18-2015
* [The Force of Pliers](/uncle-bob/2015/11/01/PlierForce.html)

  11-01-2015
* [Future Proof](/uncle-bob/2015/10/30/FutureProof.html)

  10-30-2015
* [Agile is not now, nor was it ever, Waterfall.](/uncle-bob/2015/10/16/Agile-And-Waterfall.html)

  10-16-2015
* [VW](/uncle-bob/2015/10/14/VW.html)

  10-14-2015
* [WATS Line 54](/uncle-bob/2015/10/05/WattsLine54.html)

  10-05-2015
* [A Little Structure](/uncle-bob/2015/09/23/ALittleStructure.html)

  09-23-2015
* [Make the Magic go away.](/uncle-bob/2015/08/06/LetTheMagicDie.html)

  08-06-2015
* [Pattern Pushers](/uncle-bob/2015/07/05/PatternPushers.html)

  07-05-2015
* [The Little Singleton](/uncle-bob/2015/07/01/TheLittleSingleton.html)

  07-01-2015
* [The First Micro-service Architecture](/uncle-bob/2015/05/28/TheFirstMicroserviceArchitecture.html)

  05-28-2015
* [Language Layers](/uncle-bob/2015/04/27/LanguageLayers.html)

  04-27-2015
* [Does Organization Matter?](/uncle-bob/2015/04/15/DoesOrganizationMatter.html)

  04-15-2015
* [The MODE-B Imperative](/uncle-bob/2015/02/21/ModeBImperative.html)

  02-21-2015
* [They Called them Computers.](/uncle-bob/2015/02/19/ComputerHarem.html)

  02-19-2015
* ['Interface' Considered Harmful](/uncle-bob/2015/01/08/InterfaceConsideredHarmful.html)

  01-08-2015
* [The Cycles of TDD](/uncle-bob/2014/12/17/TheCyclesOfTDD.html)

  12-17-2014
* [OO vs FP](/uncle-bob/2014/11/24/FPvsOO.html)

  11-24-2014
* [Thorns around the Gold](/uncle-bob/2014/11/19/GoingForTheGold.html)

  11-19-2014
* [The Obligation of the Programmer.](/uncle-bob/2014/11/15/WeRuleTheWorld.html)

  11-15-2014
* [One Hacker Way!](/uncle-bob/2014/11/12/PutItInProduction.html)

  11-12-2014
* [Laughter in the male dominated room.](/uncle-bob/2014/10/26/LaughterInTheMaleDominatedRoom.html)

  10-26-2014
* [GOML-1, Responsive Design](/uncle-bob/2014/10/08/GOML1-ResponsiveDesign.html)

  10-08-2014
* [Clean Micro-service Architecture](/uncle-bob/2014/10/01/CleanMicroserviceArchitecture.html)

  10-01-2014
* [Microservices and Jars](/uncle-bob/2014/09/19/MicroServicesAndJars.html)

  09-19-2014
* [The More Things Change...](/uncle-bob/2014/09/18/TheMoreThingsChange.html)

  09-18-2014
* [Test Time](/uncle-bob/2014/09/03/TestTime.html)

  09-03-2014
* [A Little About Patterns.](/uncle-bob/2014/06/30/ALittleAboutPatterns.html)

  06-30-2014
* [My Lawn](/uncle-bob/2014/06/20/MyLawn.html)

  06-20-2014
* [Is TDD Dead?](/uncle-bob/2014/06/17/IsTddDeadFinalThoughts.html)

  06-17-2014
* [First](/uncle-bob/2014/05/19/First.html)

  05-19-2014
* [The Little Mocker](/uncle-bob/2014/05/14/TheLittleMocker.html)

  05-14-2014
* [The Open Closed Principle](/uncle-bob/2014/05/12/TheOpenClosedPrinciple.html)

  05-12-2014
* [Framework Bound[2]](/uncle-bob/2014/05/11/FrameworkBound.html)

  05-11-2014
* [When to Mock](/uncle-bob/2014/05/10/WhenToMock.html)

  05-10-2014
* [The Single Responsibility Principle](/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html)

  05-08-2014
* [Professionalism and TDD (Reprise)](/uncle-bob/2014/05/02/ProfessionalismAndTDD.html)

  05-02-2014
* [Test Induced Design Damage?](/uncle-bob/2014/05/01/Design-Damage.html)

  05-01-2014
* [When TDD doesn't work.](/uncle-bob/2014/04/30/When-tdd-does-not-work.html)

  04-30-2014
* [Monogamous TDD](/uncle-bob/2014/04/25/MonogamousTDD.html)

  04-25-2014
* [Code Hoarders](/uncle-bob/2014/04/03/Code-Hoarders.html)

  04-03-2014
* [The *True* Corruption of Agile](/uncle-bob/2014/03/28/The-Corruption-of-Agile.html)

  03-28-2014
* [When Should You Think?](/uncle-bob/2014/03/11/when-to-think.html)

  03-11-2014
* [A Spectrum of Trust](/uncle-bob/2014/02/27/TheTrustSpectrum.html)

  02-27-2014
* [Oh Foreman, Where art Thou?](/uncle-bob/2014/02/23/OhForemanWhereArtThou.html)

  02-23-2014
* [Where is the Foreman?](/uncle-bob/2014/02/21/WhereIsTheForeman.html)

  02-21-2014
* [The Domain Discontinuity](/uncle-bob/2014/01/27/TheChickenOrTheRoad.html)

  01-27-2014
* [Coding in the Clink (9)](/uncle-bob/2014/01/20/Marion_Correctional.html)

  01-20-2014
* [Extreme Programming, a Reflection](/uncle-bob/2013/12/10/Thankyou-Kent.html)

  12-10-2013
* [Novices. A Coda](/uncle-bob/2013/11/25/Novices-Coda.html)

  11-25-2013
* [Hordes Of Novices](/uncle-bob/2013/11/19/HoardsOfNovices.html)

  11-19-2013
* [Healthcare.gov](/uncle-bob/2013/11/12/Healthcare-gov.html)

  11-12-2013
* [The Careless Ones](/uncle-bob/2013/10/24/The-Careless-Ones.html)

  10-24-2013
* [Dance you Imps!](/uncle-bob/2013/10/01/Dance-You-Imps.html)

  10-01-2013
* [A.T. FAIL!](/uncle-bob/2013/09/26/AT-FAIL.html)

  09-26-2013
* [Test First](/uncle-bob/2013/09/23/Test-first.html)

  09-23-2013
* [Transformation Priority and Sorting](/uncle-bob/2013/05/27/TransformationPriorityAndSorting.html)

  05-27-2013
* [The Transformation Priority Premise](/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html)

  05-27-2013
* [Flash - TPP](/uncle-bob/2013/05/27/FlashTpp.html)

  05-27-2013
* [Fib. The T-P Premise.](/uncle-bob/2013/05/27/FibTPP.html)

  05-27-2013
* [There are Ladies Present](/uncle-bob/2013/03/22/There-are-ladies-present.html)

  03-22-2013
* [The Frenzied Panic of Rushing](/uncle-bob/2013/03/11/TheFrenziedPanicOfRushing.html)

  03-11-2013
* [An Open and Closed Case](/uncle-bob/2013/03/08/AnOpenAndClosedCase.html)

  03-08-2013
* [The Pragmatics of TDD](/uncle-bob/2013/03/06/ThePragmaticsOfTDD.html)

  03-06-2013
* [The Start-Up Trap](/uncle-bob/2013/03/05/TheStartUpTrap.html)

  03-05-2013
* [The Principles of Craftsmanship](/uncle-bob/2013/02/10/ThePrinciplesOfCraftsmanship.html)

  02-10-2013
* [The Humble Craftsman](/uncle-bob/2013/02/01/The-Humble-Craftsman.html)

  02-01-2013
* [The Laborer and the Craftsman](/uncle-bob/2013/01/30/The-Craftsman-And-The-Laborer.html)

  01-30-2013
* [FP Basics E4](/uncle-bob/2013/01/29/FPBE4-Lazy-Evaluation.html)

  01-29-2013
* [FP Basics E3](/uncle-bob/2013/01/07/FPBE3-Do-the-rules-change.html)

  01-07-2013
* [FP Basics E2](/uncle-bob/2013/01/02/FPBE2-Whys-it-called-functional.html)

  01-02-2013
* [Brave New Year](/uncle-bob/2012/12/29/Brave-New-Year.html)

  12-29-2012
* [FP Basics E1](/uncle-bob/2012/12/22/FPBE1-Whats-it-all-about.html)

  12-22-2012
* [Three Paradigms](/uncle-bob/2012/12/19/Three-Paradigms.html)

  12-19-2012
* [The New CTO](/uncle-bob/2012/09/06/I-am-Your-New-CTO.html)

  09-06-2012
* [Functional Programming for the Object Oriented Programmer](/uncle-bob/2012/08/24/functional-programming-for-the-object-oriented-programmer.html)

  08-24-2012
* [The Clean Architecture](/uncle-bob/2012/08/13/the-clean-architecture.html)

  08-13-2012
* [NO DB](/uncle-bob/2012/05/15/NODB.html)

  05-15-2012
* [Why is Estimating so Hard?](/uncle-bob/2012/04/20/Why-Is-Estimating-So-Hard.html)

  04-20-2012
* [After the Disaster](/uncle-bob/2012/04/18/After-The-Disaster.html)

  04-18-2012
* [Service Oriented Agony](/uncle-bob/2012/02/01/Service-Oriented-Agony.html)

  02-01-2012
* [The Ruby Colored Box](/uncle-bob/2012/01/31/The-Ruby-Colored-Box.html)

  01-31-2012
* [Fecophiles](/uncle-bob/2012/01/20/Fecophiles.html)

  01-20-2012
* [The Letter](/uncle-bob/2012/01/12/The-Letter.html)

  01-12-2012
* [Flipping the Bit](/uncle-bob/2012/01/11/Flipping-the-Bit.html)

  01-11-2012
* [The Barbarians are at the Gates](/uncle-bob/2011/12/11/The-Barbarians-are-at-the-Gates.html)

  12-11-2011
* [Clean Architecture](/uncle-bob/2011/11/22/Clean-Architecture.html)

  11-22-2011
* [Double Entry Bookkeeping Dilemma. Should I Invest or Not?](/uncle-bob/2011/11/06/Double-Entry-Bookkeeping-Dilemma-Should-I-Invest-or-Not.html)

  11-06-2011
* [Simple Hickey](/uncle-bob/2011/10/20/Simple-Hickey.html)

  10-20-2011
* [Screaming Architecture](/uncle-bob/2011/09/30/Screaming-Architecture.html)

  09-30-2011
* [Bringing Balance to the Force](/uncle-bob/2011/01/19/individuals-and-interactions.html)

  01-19-2011
* [What Software Craftsmanship is about](/uncle-bob/2011/01/17/software-craftsmanship-is-about.html)

  01-17-2011

# Functional Classes

18 January 2023

I recently tweeted the following:

> Should you subdivide a functional program into classes the way you would an object oriented program?  
>   
> Yes. You should. Because the rules don’t change just because you’ve chosen to use immutable data structures.
>
> — Uncle Bob Martin (@unclebobmartin) [January 17, 2023](https://twitter.com/unclebobmartin/status/1615436628385824769?ref_src=twsrc%5Etfw)

This led to a bevy of interesting responses about the difference between classes and modules. In answer to those responses I tweeted this:

> A class is a group of cohesive and narrowly defined functions that operate on an encapsulated data structure. The functions may, or may not, be polymorphically deployed.
>
> — Uncle Bob Martin (@unclebobmartin) [January 17, 2023](https://twitter.com/unclebobmartin/status/1615438162746134528?ref_src=twsrc%5Etfw)

Of course that only led to an increased number of interesting responses. And so I thought that it might be wise to blog about my reasoning rather than to continue trying to cram that reasoning into tweets.

If you are in doubt about what FP is, and about what OO is, and about whether the two are compatible, then I recommend [this](http://blog.cleancoder.com/uncle-bob/2018/04/13/FPvsOO.html) old blog of mine.

What is a class? According to the dictionary a class is:

> *A set, collection, group, or configuration containing members regarded as having certain attributes or traits in common; a kind or category.*

Now consider that definition when reading the next paragraph.

In OO languages we organize our programs into classes of objects that share similar traits. We describe those objects in terms of the attributes and behaviors that they have in common. We strive to create hierarchies of classification that those objects can fit within. We consider the higher level classifications to be abstractions that allow the expression of general truths that are independent of irrelevant details. (Indeed, I once defined abstraction as: *The Amplification of the essential, and the elimination of the irrelevant.*[[1]](https://www.amazon.com/Designing-Object-Oriented-Applications-Method/dp/0132038374))

In 1966 the power of abstraction by classification led the authors of Simula to create the keyword `class`. In 1980, Bjarne Stroustrup continued that convention and used the `class` keyword in C++. This was actually somewhat strange because C already had the keyword `struct` which had a virtually identical meaning. But the power of the word `class` held sway.

In the mid 90s the power of that word led the authors of Java (and then C#) to declare *and enforce* that *everything* in a program must be part of a class. This was a dramatic overreach. It seems to me that some of the things that Java forces into classes ought not to be in classes at all. For example, the class `java.lang.Math` is really just a namespace for a batch of functions and is not, in any sense, a classification of objects.

This conflation of object classification and namespaces is confusing and unnecessary; and is probably part of the reason my initial tweet generated the responses that it did.

Another overreach in Java (and by extension C#) is that methods are polymorphic by default. Polymorphism is a tool, not a rule. Many, if not most, function calls do not require dynamic dispatch.

These kinds of overreach lead to confusion about what a class really is. I believe that most of the responses to my tweet were the result of that confusion.

So let’s cut to the chase.

One of the oldest rules of software design is that we should partition the elements of the system into loosely coupled and internally cohesive elements. Those elements become well named places where we can put data and behavior. This follows the old proverb: *A place for everything, and everything in its place.*

What are those elements? It seems obvious that the classification structures of objects ought to be high on the list. Namespaced function libraries like `java.lang.Math` are another obvious choice. In the one case we have a batch of functions that manipulate an internal data structure. In the other case we have a batch of functions that manipulate an external data structure.

The essential charachteristic of these elements, these batches of functions, is that they are internally cohesive. That means that all the functions in the batch are strongly related to each other because they manipulate the same data structures, whether internal or external. It is that cohesion that drives the partitioning of a software design.

###Example

Recently I have been writing an application called [`more-speech`](http://github.com/unclebob/more-speech) which is a client that browses messages on the [`nostr`](https://nostr.com) network. This nework is composed of relays that use a simple websocket protocol to transmit messages to clients. The `more-speech` client is written in Clojure, which is a Functional Programming language.

Early on I created a module named `protocol` to house the code that implemented the `nostr` protocol. I began this module by managing the websockets over which the messages travelled, and then decoding those messages and manipulating them according to the rules of the protocol.

Clojure is not a traditional OOPL, there is no `class` keyword that is used to declare and define objects and the methods that manipulate them. Rather, a module in Clojure is just a batch of functions that are not syntactically bound to any particular data. Thus my `protocol` module had functions that dealt with `WebSocket`s and functions that dealth with messages and functions that dealth with protocol elements. They were cohesive in the sense that they were all related to the `nostr` protocol; but there was no central data structure that unified them.

The other day I realized that I was missing an abstraction. The `nostr` protocol may be transmitted over websockets but the protocol rules have nothing to do with websockets. Those rules deal with the data that comes through the websockets, but not the websockets themselves. Yet my `protocol` module was littered with websocket code.

So I separated the websocket code from the `protocol` code by creating an abstraction that I called `relay`. A `relay` is a data structure that contains the `url` of a websocket, the websocket itself, and a function to call when messages are received. The `relay` data structure is manipulated by functions such as `make`, `open`, `close`, and `send`.

This `relay` module very clearly defines a class of objects. The `protocol` constructs a `relay` object for each of the urls in a list of active relays. It `open`s those `relay`s and `send`s messages to them. Messages that are received are sent to `protocol` through the callback functions that are passed into the function that constructs the `relay` object. In order to maintain the immutability and referential transparency constraints of Functional Programming, the functions that update the state of a `relay` return a new instance of that `relay`.

###Lesson

Java, C#, Ruby, and C++ all either enforce, or stronly encourage, the partitioning of systems into classes. Clojure does not; it is entirely agnostic about classes. The lesson that I learned from `protocol` and `relay` is that I had not been paying enough attention to class structure when writing complex Clojure programs. Instead, I had been allowing functions to accumulate in modules in a, more or less, ad hoc fashion – similar to the way one might program in C, Fortran, Basic, or even Assembler. But that was lazy. Objects exist in programs, and they can, and should, be classified. So, from now on, I will be paying much more attention to the classification structure of the objects my systems.

> *A place for everything, and everything in its place.*

---

## Source: uncle-bob_2023_01_19_functional-classes-clojure.html.md

Clean Coder Blog


[![](/assets/clean_code_72_color.png)](/)

# The Clean Code Blog

by Robert C. Martin (Uncle Bob)



[atom/rss feed](/atom.xml)


---

* [Functional Classes in Clojure](/uncle-bob/2023/01/19/functional-classes-clojure.html)

  01-19-2023
* [Functional Classes](/uncle-bob/2023/01/18/functional-classes.html)

  01-18-2023
* [Space War](/uncle-bob/2021/11/28/Spacewar.html)

  11-28-2021
* [Functional Duplications](/uncle-bob/2021/10/28/functional-duplication.html)

  10-28-2021
* [Roots](/uncle-bob/2021/09/25/roots.html)

  09-25-2021
* [More On Types](/uncle-bob/2021/06/29/MoreOnTypes.html)

  06-29-2021
* [On Types](/uncle-bob/2021/06/25/OnTypes.html)

  06-25-2021
* [if-else-switch](/uncle-bob/2021/03/06/ifElseSwitch.html)

  03-06-2021
* [Pairing Guidelines](/uncle-bob/2021/01/17/Pairing.html)

  01-17-2021
* [Solid Relevance](/uncle-bob/2020/10/18/Solid-Relevance.html)

  10-18-2020
* [Loopy](/uncle-bob/2020/09/30/loopy.html)

  09-30-2020
* [Conference Conduct](/uncle-bob/2020/09/23/ConferenceConduct.html)

  09-23-2020
* [The Disinvitation](/uncle-bob/2020/09/12/TheDisinvitation.html)

  09-12-2020
* [REPL Driven Design](/uncle-bob/2020/05/27/ReplDrivenDesign.html)

  05-27-2020
* [A Little More Clojure](/uncle-bob/2020/04/09/ALittleMoreClojure.html)

  04-09-2020
* [A Little Clojure](/uncle-bob/2020/04/06/ALittleClojure.html)

  04-06-2020
* [A New Hope](/uncle-bob/2020/04/05/ANewHope.html)

  04-05-2020
* [Open Letter to the Linux Foundation](/uncle-bob/2019/11/08/OpenLetterLinuxFoundation.html)

  11-08-2019
* [What They Thought of Programmers.](/uncle-bob/2019/11/03/WhatTheyThoughtOfUs.html)

  11-03-2019
* [Circulatory](/uncle-bob/2019/10/31/Circulatory.html)

  10-31-2019
* [Why Clojure?](/uncle-bob/2019/08/22/WhyClojure.html)

  08-22-2019
* [Why won't it...](/uncle-bob/2019/07/22/WhyWontIt.html)

  07-22-2019
* [Classes vs. Data Structures](/uncle-bob/2019/06/16/ObjectsAndDataStructures.html)

  06-16-2019
* [Types and Tests](/uncle-bob/2019/06/08/TestsAndTypes.html)

  06-08-2019
* [737 Max 8](/uncle-bob/2019/05/18/737-Max-8.html)

  05-18-2019
* [FP vs. OO List Processing](/uncle-bob/2018/12/17/FPvsOO-List-processing.html)

  12-17-2018
* [We, The Unoffended](/uncle-bob/2018/12/16/unoffended.html)

  12-16-2018
* [SJWJS](/uncle-bob/2018/12/14/SJWJS.html)

  12-14-2018
* [The Tragedy of Craftsmanship.](/uncle-bob/2018/08/28/CraftsmanshipMovement.html)

  08-28-2018
* [Too Clean?](/uncle-bob/2018/08/13/TooClean.html)

  08-13-2018
* [Integers and Estimates](/uncle-bob/2018/06/21/IntegersAndEstimates.html)

  06-21-2018
* [Pickled State](/uncle-bob/2018/06/06/PickledState.html)

  06-06-2018
* [Craftsman, Craftswoman, Craftsperson](/uncle-bob/2018/05/02/Craftsman-Craftswoman-Craftsperson.html)

  05-02-2018
* [FP vs. OO](/uncle-bob/2018/04/13/FPvsOO.html)

  04-13-2018
* [In The Large](/uncle-bob/2018/04/02/InTheLarge.html)

  04-02-2018
* [*We Programmers*](/uncle-bob/2018/03/29/WeProgrammers.html)

  03-29-2018
* [Uncle Bob Fly-In.  
  Have I got a deal for you!](/uncle-bob/2018/02/25/UncleBobFlyIn.html)

  02-25-2018
* [The Citizenship Argument](/uncle-bob/2018/01/18/TheCitizenshipArgument.html)

  01-18-2018
* [Operating Behind the Power Curve](/uncle-bob/2018/01/15/behindThePowerCurve.html)

  01-15-2018
* [Excuses](/uncle-bob/2017/12/18/Excuses.html)

  12-18-2017
* [Dbtails](/uncle-bob/2017/12/09/Dbtails.html)

  12-09-2017
* [Bobby Tables](/uncle-bob/2017/12/03/BobbyTables.html)

  12-03-2017
* [Living on the Plateau](/uncle-bob/2017/11/18/OnThePlateau.html)

  11-18-2017
* [Women In Demand](/uncle-bob/2017/10/04/WomenInDemand.html)

  10-04-2017
* [Tools are not the Answer](/uncle-bob/2017/10/04/CodeIsNotTheAnswer.html)

  10-04-2017
* [Test Contra-variance](/uncle-bob/2017/10/03/TestContravariance.html)

  10-03-2017
* [The Unscrupulous Meme](/uncle-bob/2017/09/29/TheUnscrupulousMeme.html)

  09-29-2017
* [Sierra Juliet Foxtrot](/uncle-bob/2017/09/26/SierraJulietFoxtrot.html)

  09-26-2017
* [Just Following Orders](/uncle-bob/2017/08/28/JustFollowingOders.html)

  08-28-2017
* [Women in Tech](/uncle-bob/2017/08/14/WomenInTech.html)

  08-14-2017
* [On the Diminished Capacity to Discuss Things Rationally](/uncle-bob/2017/08/10/OnTheInabilityToDiscussThingsRationally.html)

  08-10-2017
* [Thought Police](/uncle-bob/2017/08/09/ThoughtPolice.html)

  08-09-2017
* [The Brain Problem](/uncle-bob/2017/07/28/TheBrainProblem.html)

  07-28-2017
* [Drive me to Toronto, Hal.](/uncle-bob/2017/07/24/DriveMeToTorontoHal.html)

  07-24-2017
* [Pragmatic Functional Programming](/uncle-bob/2017/07/11/PragmaticFunctionalProgramming.html)

  07-11-2017
* [First-Class Tests.](/uncle-bob/2017/05/05/TestDefinitions.html)

  05-05-2017
* [Is Dr. Calvin in the Room?](/uncle-bob/2017/03/16/DrCalvin.html)

  03-16-2017
* [Symmetry Breaking](/uncle-bob/2017/03/07/SymmetryBreaking.html)

  03-07-2017
* [Testing Like the TSA](/uncle-bob/2017/03/06/TestingLikeTheTSA.html)

  03-06-2017
* [TDD Harms Architecture](/uncle-bob/2017/03/03/TDD-Harms-Architecture.html)

  03-03-2017
* [Necessary Comments](/uncle-bob/2017/02/23/NecessaryComments.html)

  02-23-2017
* [Types and Tests](/uncle-bob/2017/01/13/TypesAndTests.html)

  01-13-2017
* [The Dark Path](/uncle-bob/2017/01/11/TheDarkPath.html)

  01-11-2017
* [TDD Lesson - Terrain Generation](/uncle-bob/2017/01/09/DiamondSquare.html)

  01-09-2017
* [TDD Doesn't Work](/uncle-bob/2016/11/10/TDD-Doesnt-work.html)

  11-10-2016
* [Dijkstra's Algorithm](/uncle-bob/2016/10/26/DijkstrasAlg.html)

  10-26-2016
* [The Lurn](/uncle-bob/2016/09/01/TheLurn.html)

  09-01-2016
* [The Churn](/uncle-bob/2016/07/27/TheChurn.html)

  07-27-2016
* [Mutation Testing](/uncle-bob/2016/06/10/MutationTesting.html)

  06-10-2016
* [Blue. No! Yellow!](/uncle-bob/2016/05/21/BlueNoYellow.html)

  05-21-2016
* [Type Wars](/uncle-bob/2016/05/01/TypeWars.html)

  05-01-2016
* [Giving Up on TDD](/uncle-bob/2016/03/19/GivingUpOnTDD.html)

  03-19-2016
* [Manhandled](/uncle-bob/2016/01/15/Manhandled.html)

  01-15-2016
* [Stabilization Phases](/uncle-bob/2016/01/14/Stabilization.html)

  01-14-2016
* [A Little Architecture](/uncle-bob/2016/01/04/ALittleArchitecture.html)

  01-04-2016
* [Prelude to a Profession](/uncle-bob/2015/11/27/OathDiscussion.html)

  11-27-2015
* [The Programmer's Oath](/uncle-bob/2015/11/18/TheProgrammersOath.html)

  11-18-2015
* [The Force of Pliers](/uncle-bob/2015/11/01/PlierForce.html)

  11-01-2015
* [Future Proof](/uncle-bob/2015/10/30/FutureProof.html)

  10-30-2015
* [Agile is not now, nor was it ever, Waterfall.](/uncle-bob/2015/10/16/Agile-And-Waterfall.html)

  10-16-2015
* [VW](/uncle-bob/2015/10/14/VW.html)

  10-14-2015
* [WATS Line 54](/uncle-bob/2015/10/05/WattsLine54.html)

  10-05-2015
* [A Little Structure](/uncle-bob/2015/09/23/ALittleStructure.html)

  09-23-2015
* [Make the Magic go away.](/uncle-bob/2015/08/06/LetTheMagicDie.html)

  08-06-2015
* [Pattern Pushers](/uncle-bob/2015/07/05/PatternPushers.html)

  07-05-2015
* [The Little Singleton](/uncle-bob/2015/07/01/TheLittleSingleton.html)

  07-01-2015
* [The First Micro-service Architecture](/uncle-bob/2015/05/28/TheFirstMicroserviceArchitecture.html)

  05-28-2015
* [Language Layers](/uncle-bob/2015/04/27/LanguageLayers.html)

  04-27-2015
* [Does Organization Matter?](/uncle-bob/2015/04/15/DoesOrganizationMatter.html)

  04-15-2015
* [The MODE-B Imperative](/uncle-bob/2015/02/21/ModeBImperative.html)

  02-21-2015
* [They Called them Computers.](/uncle-bob/2015/02/19/ComputerHarem.html)

  02-19-2015
* ['Interface' Considered Harmful](/uncle-bob/2015/01/08/InterfaceConsideredHarmful.html)

  01-08-2015
* [The Cycles of TDD](/uncle-bob/2014/12/17/TheCyclesOfTDD.html)

  12-17-2014
* [OO vs FP](/uncle-bob/2014/11/24/FPvsOO.html)

  11-24-2014
* [Thorns around the Gold](/uncle-bob/2014/11/19/GoingForTheGold.html)

  11-19-2014
* [The Obligation of the Programmer.](/uncle-bob/2014/11/15/WeRuleTheWorld.html)

  11-15-2014
* [One Hacker Way!](/uncle-bob/2014/11/12/PutItInProduction.html)

  11-12-2014
* [Laughter in the male dominated room.](/uncle-bob/2014/10/26/LaughterInTheMaleDominatedRoom.html)

  10-26-2014
* [GOML-1, Responsive Design](/uncle-bob/2014/10/08/GOML1-ResponsiveDesign.html)

  10-08-2014
* [Clean Micro-service Architecture](/uncle-bob/2014/10/01/CleanMicroserviceArchitecture.html)

  10-01-2014
* [Microservices and Jars](/uncle-bob/2014/09/19/MicroServicesAndJars.html)

  09-19-2014
* [The More Things Change...](/uncle-bob/2014/09/18/TheMoreThingsChange.html)

  09-18-2014
* [Test Time](/uncle-bob/2014/09/03/TestTime.html)

  09-03-2014
* [A Little About Patterns.](/uncle-bob/2014/06/30/ALittleAboutPatterns.html)

  06-30-2014
* [My Lawn](/uncle-bob/2014/06/20/MyLawn.html)

  06-20-2014
* [Is TDD Dead?](/uncle-bob/2014/06/17/IsTddDeadFinalThoughts.html)

  06-17-2014
* [First](/uncle-bob/2014/05/19/First.html)

  05-19-2014
* [The Little Mocker](/uncle-bob/2014/05/14/TheLittleMocker.html)

  05-14-2014
* [The Open Closed Principle](/uncle-bob/2014/05/12/TheOpenClosedPrinciple.html)

  05-12-2014
* [Framework Bound[2]](/uncle-bob/2014/05/11/FrameworkBound.html)

  05-11-2014
* [When to Mock](/uncle-bob/2014/05/10/WhenToMock.html)

  05-10-2014
* [The Single Responsibility Principle](/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html)

  05-08-2014
* [Professionalism and TDD (Reprise)](/uncle-bob/2014/05/02/ProfessionalismAndTDD.html)

  05-02-2014
* [Test Induced Design Damage?](/uncle-bob/2014/05/01/Design-Damage.html)

  05-01-2014
* [When TDD doesn't work.](/uncle-bob/2014/04/30/When-tdd-does-not-work.html)

  04-30-2014
* [Monogamous TDD](/uncle-bob/2014/04/25/MonogamousTDD.html)

  04-25-2014
* [Code Hoarders](/uncle-bob/2014/04/03/Code-Hoarders.html)

  04-03-2014
* [The *True* Corruption of Agile](/uncle-bob/2014/03/28/The-Corruption-of-Agile.html)

  03-28-2014
* [When Should You Think?](/uncle-bob/2014/03/11/when-to-think.html)

  03-11-2014
* [A Spectrum of Trust](/uncle-bob/2014/02/27/TheTrustSpectrum.html)

  02-27-2014
* [Oh Foreman, Where art Thou?](/uncle-bob/2014/02/23/OhForemanWhereArtThou.html)

  02-23-2014
* [Where is the Foreman?](/uncle-bob/2014/02/21/WhereIsTheForeman.html)

  02-21-2014
* [The Domain Discontinuity](/uncle-bob/2014/01/27/TheChickenOrTheRoad.html)

  01-27-2014
* [Coding in the Clink (9)](/uncle-bob/2014/01/20/Marion_Correctional.html)

  01-20-2014
* [Extreme Programming, a Reflection](/uncle-bob/2013/12/10/Thankyou-Kent.html)

  12-10-2013
* [Novices. A Coda](/uncle-bob/2013/11/25/Novices-Coda.html)

  11-25-2013
* [Hordes Of Novices](/uncle-bob/2013/11/19/HoardsOfNovices.html)

  11-19-2013
* [Healthcare.gov](/uncle-bob/2013/11/12/Healthcare-gov.html)

  11-12-2013
* [The Careless Ones](/uncle-bob/2013/10/24/The-Careless-Ones.html)

  10-24-2013
* [Dance you Imps!](/uncle-bob/2013/10/01/Dance-You-Imps.html)

  10-01-2013
* [A.T. FAIL!](/uncle-bob/2013/09/26/AT-FAIL.html)

  09-26-2013
* [Test First](/uncle-bob/2013/09/23/Test-first.html)

  09-23-2013
* [Transformation Priority and Sorting](/uncle-bob/2013/05/27/TransformationPriorityAndSorting.html)

  05-27-2013
* [The Transformation Priority Premise](/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html)

  05-27-2013
* [Flash - TPP](/uncle-bob/2013/05/27/FlashTpp.html)

  05-27-2013
* [Fib. The T-P Premise.](/uncle-bob/2013/05/27/FibTPP.html)

  05-27-2013
* [There are Ladies Present](/uncle-bob/2013/03/22/There-are-ladies-present.html)

  03-22-2013
* [The Frenzied Panic of Rushing](/uncle-bob/2013/03/11/TheFrenziedPanicOfRushing.html)

  03-11-2013
* [An Open and Closed Case](/uncle-bob/2013/03/08/AnOpenAndClosedCase.html)

  03-08-2013
* [The Pragmatics of TDD](/uncle-bob/2013/03/06/ThePragmaticsOfTDD.html)

  03-06-2013
* [The Start-Up Trap](/uncle-bob/2013/03/05/TheStartUpTrap.html)

  03-05-2013
* [The Principles of Craftsmanship](/uncle-bob/2013/02/10/ThePrinciplesOfCraftsmanship.html)

  02-10-2013
* [The Humble Craftsman](/uncle-bob/2013/02/01/The-Humble-Craftsman.html)

  02-01-2013
* [The Laborer and the Craftsman](/uncle-bob/2013/01/30/The-Craftsman-And-The-Laborer.html)

  01-30-2013
* [FP Basics E4](/uncle-bob/2013/01/29/FPBE4-Lazy-Evaluation.html)

  01-29-2013
* [FP Basics E3](/uncle-bob/2013/01/07/FPBE3-Do-the-rules-change.html)

  01-07-2013
* [FP Basics E2](/uncle-bob/2013/01/02/FPBE2-Whys-it-called-functional.html)

  01-02-2013
* [Brave New Year](/uncle-bob/2012/12/29/Brave-New-Year.html)

  12-29-2012
* [FP Basics E1](/uncle-bob/2012/12/22/FPBE1-Whats-it-all-about.html)

  12-22-2012
* [Three Paradigms](/uncle-bob/2012/12/19/Three-Paradigms.html)

  12-19-2012
* [The New CTO](/uncle-bob/2012/09/06/I-am-Your-New-CTO.html)

  09-06-2012
* [Functional Programming for the Object Oriented Programmer](/uncle-bob/2012/08/24/functional-programming-for-the-object-oriented-programmer.html)

  08-24-2012
* [The Clean Architecture](/uncle-bob/2012/08/13/the-clean-architecture.html)

  08-13-2012
* [NO DB](/uncle-bob/2012/05/15/NODB.html)

  05-15-2012
* [Why is Estimating so Hard?](/uncle-bob/2012/04/20/Why-Is-Estimating-So-Hard.html)

  04-20-2012
* [After the Disaster](/uncle-bob/2012/04/18/After-The-Disaster.html)

  04-18-2012
* [Service Oriented Agony](/uncle-bob/2012/02/01/Service-Oriented-Agony.html)

  02-01-2012
* [The Ruby Colored Box](/uncle-bob/2012/01/31/The-Ruby-Colored-Box.html)

  01-31-2012
* [Fecophiles](/uncle-bob/2012/01/20/Fecophiles.html)

  01-20-2012
* [The Letter](/uncle-bob/2012/01/12/The-Letter.html)

  01-12-2012
* [Flipping the Bit](/uncle-bob/2012/01/11/Flipping-the-Bit.html)

  01-11-2012
* [The Barbarians are at the Gates](/uncle-bob/2011/12/11/The-Barbarians-are-at-the-Gates.html)

  12-11-2011
* [Clean Architecture](/uncle-bob/2011/11/22/Clean-Architecture.html)

  11-22-2011
* [Double Entry Bookkeeping Dilemma. Should I Invest or Not?](/uncle-bob/2011/11/06/Double-Entry-Bookkeeping-Dilemma-Should-I-Invest-or-Not.html)

  11-06-2011
* [Simple Hickey](/uncle-bob/2011/10/20/Simple-Hickey.html)

  10-20-2011
* [Screaming Architecture](/uncle-bob/2011/09/30/Screaming-Architecture.html)

  09-30-2011
* [Bringing Balance to the Force](/uncle-bob/2011/01/19/individuals-and-interactions.html)

  01-19-2011
* [What Software Craftsmanship is about](/uncle-bob/2011/01/17/software-craftsmanship-is-about.html)

  01-17-2011

# Functional Classes in Clojure

19 January 2023

My previous [blog](http://blog.cleancoder.com/uncle-bob/2023/01/18/functional-classes.html) seemed only to continue the confusion regarding classes in Functional Programming. Indeed, many people got quite irate. So perhaps a bit of code will help.

**Trigger Warning**:

* Object Oriented Terminology.
* Dynamically Typed Language.
* Mixed Metaphors.
* Distracting Animations.

> To all the adherents of the *Statically Typed* Functional Programming religion: I know that you believe that *Static Typing* is an essential aspect of Functional Programming and that no mere dynamically typed language could ever begin to approach the heights and glory of *The One True and Holy TYPED Functional Apotheotic Paradigm*. But we lowly programmers quivering down here at the base of *Orthanc* can only hope to meekly subsist on the dregs that fall from on high.

(R.I.P. Kirstie Alley

OK, so, once again…

> *A class is an intentionally named abstraction that consists of a set of narrowly cohesive functions that operate over an internally defined data structure.*

We do not need the `class` keyword. Nor do we need polymorphic dispatch. Nor do we need inheritance. A class is just a description, whether in full or in part, of an object.

For example – it’s time we talked about clouds (which I have looked at from both sides now; and do, in fact, understand pretty well).

So… Here come your father’s parentheses!

![](https://i.pinimg.com/originals/4f/1e/26/4f1e261d1afa9d58fd1125db5a5a4a12.jpg)

```
(ns spacewar.game-logic.clouds
  (:require [clojure.spec.alpha :as s]
            [spacewar.geometry :as geo]
            [spacewar.game-logic.config :as glc]))

(s/def ::x number?)
(s/def ::y number?)
(s/def ::concentration number?)

(s/def ::cloud (s/keys :req-un [::x ::y ::concentration]))
(s/def ::clouds (s/coll-of ::cloud))

(defn valid-cloud? [cloud]
  (let [valid (s/valid? ::cloud cloud)]
    (when (not valid)
      (println (s/explain-str ::cloud cloud)))
    valid))

(defn make-cloud
  ([]
   (make-cloud 0 0 0))
  ([x y concentration]
  {:x x
   :y y
   :concentration concentration}))

(defn harvest-dilithium [ms ship cloud]
  (let [ship-pos [(:x ship) (:y ship)]
        cloud-pos [(:x cloud) (:y cloud)]]
    (if (< (geo/distance ship-pos cloud-pos) glc/dilithium-harvest-range)
      (let [max-harvest (* ms glc/dilithium-harvest-rate)
            need (- glc/ship-dilithium (:dilithium ship))
            cloud-content (:concentration cloud)
            harvest (min max-harvest cloud-content need)
            ship (update ship :dilithium + harvest)
            cloud (update cloud :concentration - harvest)]
        [ship cloud])
      [ship cloud])))

(defn update-dilithium-harvest [ms world]
  (let [{:keys [clouds ship]} world]
    (loop [clouds clouds ship ship harvested-clouds []]
      (if (empty? clouds)
        (assoc world :ship ship :clouds harvested-clouds)
        (let [[ship cloud] (harvest-dilithium ms ship (first clouds))]
          (recur (rest clouds) ship (conj harvested-clouds cloud)))))))

(defn update-clouds-age [ms world]
  (let [clouds (:clouds world)
        decay (Math/pow glc/cloud-decay-rate ms)
        clouds (map #(update % :concentration * decay) clouds)
        clouds (filter #(> (:concentration %) 1) clouds)
        clouds (doall clouds)]
    (assoc world :clouds clouds)))

(defn update-clouds [ms world]
  (->> world
       (update-clouds-age ms)
       (update-dilithium-harvest ms)))
```

Some years back I wrote a nice little [spacewar game](http://blog.cleancoder.com/uncle-bob/2021/11/28/Spacewar.html) in Clojure. You can play it [here](http://spacewar.fikesfarm.com/spacewar.html). While playing, if you manage to blow up a Klingon, a sparkling cloud of *Dilithium Crystals* will remain behind, quickly dissipating. If you can guide your ship into the midst of that cloud, you will harvest some of that *Dilithium* and replenish your stores.

The code you see above is the *class* that represents the *Dilithium Cloud*.

The first thing to notice is that I defined the *TYPE* of the `cloud` *class* – *dynamically*.  
![](https://yt3.ggpht.com/a/AATXAJxJ07NzOxzlMLuiV6SGv808JXSCrALLJMXJ1w=s900-c-k-c0xffffffff-no-rj-mo)

A `cloud` is an object with an `x` and `y` coordinate, and a `concentration`; all of which must be numbers. I also created a little type checking function named `valid-cloud?` that is used by my unit tests (not shown) to make sure the *TYPE* is not violated by any of the *methods*.

Next comes `make-cloud` the *constructor* of the `cloud` *class*.

[via GIPHY](https://giphy.com/gifs/theoffice-the-office-tv-frame-toby-vyTnNTrs3wqQ0UIvwE)

There are two overloads of the *constructor*. The first takes no arguments and simply creates a `cloud` at (0,0) with no *Dilithium* in it. The second takes three arguments and loads the *instance variables* of the *class*.

[via GIPHY](https://giphy.com/gifs/monty-python-2yP1jNgjNAkvu)

There are two primary *methods* of the `cloud` *class*: `update-clouds-age` and `update-dilithium-harvest`. The `update-clouds-age` *method* finds all the `cloud` *instances* in the `world` *object* and decreases their concentration by the `decay` factor – which is a function of the number of milliseconds (`ms`) since the last time they were updated. The `update-dilithium-harvest` *method* finds all the `cloud` *objects* that are within the `ship` *object*’s harvesting range and transfers *Dilithium* from those `cloud` *objects* to the `ship` *object*.

Now, you might notice that these *methods* are not the traditional style of method you would find in a Java program. For one thing, they deal with a list of `cloud` *objects* rather than an individual `cloud` *object*. Secondly, there’s nothing polymorphic about them. Third, they are *functional*, because they return a new `world` *object* with new `cloud` *objects* and, in the case of `update-dilithium-harvest`, a new `ship` *object*.

So are these really *methods* of the `cloud` *class*? Sure! Why not? They are a set of narrowly cohesive functions that manipulate an internal data structure within an intentionally named abstraction.

For all intents and purposes `cloud` is a °°°°°° °°°°°°° *class*.

[via GIPHY](https://giphy.com/gifs/reaction-laughing-lotr-TcdpZwYDPlWXC)

So there.

---
