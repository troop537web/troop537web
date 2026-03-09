# Build all static pages for Troop 537 replica

NAV = """
<div id="location-bar">Lakewood, CO</div>
<div id="header">
  <div id="header-inner">
    <div id="logo-area">
      <div id="logo-images">
        <img src="https://www.troop537.com/wp-content/themes/scouttroop-nIXQ0c/images/Universal_Emblem_tiny.gif" alt="B.S.A. Fleur De Lis">
        <img src="https://www.troop537.com/wp-content/themes/scouttroop-nIXQ0c/images/Universal_Emblem_bar.png" alt="B.S.A. Fleur De Lis">
        <img src="https://www.troop537.com/wp-content/themes/scouttroop-nIXQ0c/images/bsa_brand.png" alt="Boy Scouts of America">
      </div>
      <a id="site-title" href="index.html">Troop and Crew 537</a>
    </div>
    <nav id="main-navigation">
      <ul>
        <li{home}><a href="index.html">Home</a></li>
        <li{about}><a href="about.html">About Troop 537</a></li>
        <li{crew}><a href="crew.html">Crew 537</a></li>
        <li{events}><a href="recent-events.html">Recent Events</a></li>
        <li{calendar}><a href="calendar.html">Calendar</a></li>
        <li{photos}><a href="photos.html">Photos</a></li>
        <li{parents}><a href="parents.html">Parents</a></li>
        <li{resources}><a href="resources.html">Resources</a></li>
        <li{contact}><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
  </div>
</div>
"""

SIDEBAR = """
<div id="sidebar">
  <div class="widget">
    <img src="https://www.troop537.com/wp-content/uploads/2020/06/IMG_0883-300x234.jpg" alt="">
  </div>
  <div class="widget">
    <form class="search-form" action="#" method="get">
      <input type="search" placeholder="Search for:">
    </form>
  </div>
  <div class="widget">
    <img class="prepared-img" src="https://www.troop537.com/wp-content/themes/scouttroop-nIXQ0c/images/prepared_standard_rev.gif" alt="Do Your Best!">
  </div>
</div>
"""

FOOTER = """
<div id="footer">
  <div id="footer-inner">
    <p>&copy; 2026 Troop and Crew 537 - Denver Area Council, Alpine District - Lakewood, CO - <a href="http://www.scouting.org/">Boy Scouts of America</a> | <a href="privacy.html">Privacy Policy</a></p>
    <p>&copy; 2026 Troop and Crew 537 - Denver Area Council, Alpine District - Lakewood, CO - <a href="http://www.scouting.org/">Boy Scouts of America</a> - <a href="privacy.html">Privacy Policy</a></p>
  </div>
</div>
"""

def page(title, current, hero_html, content_html):
    flags = {k: '' for k in ['home','about','crew','events','calendar','photos','parents','resources','contact']}
    flags[current] = ' class="current"'
    nav = NAV.format(**flags)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Troop and Crew 537 | Lakewood, CO</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
{nav}
{hero_html}
<div id="wrapper">
  <div id="content">
{content_html}
  </div>
{SIDEBAR}
</div>
{FOOTER}
</body>
</html>"""

# ── INDEX ──────────────────────────────────────────────
home_hero = """
<div id="hero-image">
  <img class="front-pic" src="https://www.troop537.com/wp-content/themes/scouttroop-nIXQ0c/images/front-pic.jpg" alt="Boy Scouts of America">
  <img class="prepared" src="https://www.troop537.com/wp-content/themes/scouttroop-nIXQ0c/images/Prepared_for_life.gif" alt="Prepared for Life">
</div>
"""

home_content = """
    <h1>Troop 537 Lakewood</h1>
    <p>Troop 537 is one of the most active Scout Troops in the Denver area area and has a program designed to keep any Scout busy! Some of these activities include backpacking, cycling, camping, shooting, hiking, mountain biking, rafting, rappelling, rock climbing, fishing, skiing and snowboarding. These are just a few of the things that Troop 537 does!</p>
    <p><strong>WHERE:</strong> Our troop meets on Wednesday @ 7PM. We meet at our charter organization, <a href="https://www.google.com/maps/place/Our+Saviour's+Corner+of+Hope/@39.6816702,-105.1033748,17z" target="_blank">Our Savior's Church</a>, on the corner of Garrison St. &amp; Jewell Ave.</p>
    <p>If you would like to chat, or join our private Minecraft server, join our <strong>DISCORD:</strong> <a href="https://discord.gg/yd486Ru" target="_blank">https://discord.gg/yd486Ru</a></p>

    <h1>Camping</h1>
    <p>Troop 537 has campouts every month. Past campouts have focused on canoeing, snow shoeing, rock climbing and rappelling, caving, biking, &amp; hiking. We have several regular events like the Fall Green Mountain night hike &amp; lock-in, an annual snow shelter &amp; tubing campout, and the Klondike Derby sled race. Each summer we attend a week-long summer camp at Peaceful Valley Boys Scout camp. Traditionally, we have an additional week-long adventure to places like Moab, Boundary Waters, Philmont Scout Ranch, and Melita Island.</p>

    <h1>Adventure!</h1>
    <p><a href="recent-events.html"><img src="https://wp.troop537.com/wp-content/uploads/2020/06/adventure.jpg" alt="Adventure"></a></p>
    <p>See some of the <a href="recent-events.html">things we've been doing lately.</a></p>

    <h1>Merit Badges</h1>
    <p>Merit badges are awards earned by youth members of the Boy Scouts of America (BSA), based on activities within an area of study by completing a list of periodically updated requirements. The purpose of the merit badge program is to allow Scouts to examine subjects to determine if they would like to further pursue them as a career or a vocation. Additionally, Scouts will learn about sports, crafts, science, trades, &amp; business. Troop 537 has a very active adult and parent Merit Badge counseling support system which covers most of the 135 merit badges available.</p>
"""

# ── ABOUT ──────────────────────────────────────────────
about_content = """
    <h1>About Troop 537</h1>
    <p>Troop 537 was established in 1979 and we are proud to have produced over 70 Eagle Scouts. We are committed to making hands on learning fun for our Scouts! Troop 537 is part of the <a href="https://www.denverboyscouts.org/districts/alpine/" target="_blank">Alpine District</a> in the <a href="https://www.denverboyscouts.org/" target="_blank">Denver Area Council</a>. If you are interested in visiting or learning more about Troop 537 or scouting, <a href="contact.html">please contact us!</a></p>

    <h2>Where we meet</h2>
    <p>Charter Organization: Our Savior's Church<br>
    1975 S. Garrison St.,<br>
    Lakewood, CO 80227</p>
    <p>We meet from 7:00-8:30PM on Wednesday nights all year long.</p>

    <h2>Monthly Outings</h2>
    <p>Each month the troop goes on an outing. Typically for these we leave on Friday evening and return on Sunday. These are usually camps, adventures such as canoeing, shooting sports, mountain biking, sailing or climbing.</p>

    <h2>Summer camps</h2>
    <p>Troop 537 attends a traditional BSA, week-long Summer camp each year. Usually, Summer camp is at our own council's Peaceful Valley, but in 2021 we will be attending camp at Melita Island, MT.</p>

    <h2>High Adventure</h2>
    <p>In addition to Summer camp and the adventures each month, Troop 537 plans a High Adventure trip each summer. The troop traditionally goes to one of the Boy Scouts of America High Adventure Bases such as the Philmont Scout Ranch in New Mexico or organizes a trip places like the Boundary Waters, Moab, Swamp Base, Sea Base, or Colorado ranges such as the San Juans.</p>

    <h2>Scoutmaster Fleming</h2>
    <div class="clearfix">
      <img class="scoutmaster-photo" src="https://www.troop537.com/wp-content/uploads/2023/12/Headshot-1024x768.jpg" alt="Scoutmaster Fleming">
      <p>Sam Fleming, a Front Range native, began his Scouting journey as a Cub Scout in 1978 and developed a profound passion for the outdoors during his time at Montana State University. With extensive experience in rafting, kayaking, skiing, mountain biking, and other outdoor pursuits, Sam is skilled at leading multi-day backcountry trips whether on the river or in the mountains. Before moving up to Boy Scouts with Ryan, Sam significantly expanded Pack 548 during his tenure as Cubmaster, growing it from 11 scouts to a thriving community of over 60. His contributions extend further as a committee member and coordinator for the Greater Colorado Council Roundtable. He's been recognized for his dedication, receiving awards like the Timberline District Volunteer of the Year in 2019 and the Alpine District Award of Merit in 2022.</p>
      <p>As Scoutmaster, Sam prioritizes creating a safe space for scouts to explore and learn, emphasizing discovery rather than simply providing answers. He humorously admits, "Sometimes the Scouts surprise me and teach me a thing or two!" Sam finds immense joy in his roles as a loving husband to Susan and a father to Ryan and Jack. He treasures family adventures, whether on Idaho rivers, the slopes at Mary Jane, mountain bike race sidelines, or at choir, band and orchestra performances. Mr. Fleming welcomes you and your family to Troop 537 and invites you to attend a meeting to learn more about our Troop and Scouting.</p>
    </div>

    <h2>Former Scoutmaster Mocilac</h2>
    <div class="clearfix">
      <img class="former-sm-photo" src="https://www.troop537.com/wp-content/uploads/2021/03/Charles.png" alt="Troop 537 Scoutmaster, Charles Mocilac">
      <p>Troop 537 is honored to have long time Scouting veteran Charles Mocilac as part of our troop. Charles started scouting in 1973 when growing up in Rialto, California. Coming from a family of Eagle Scouts, he earned his eagle in 1976 and has one gold palm. Charles worked at Camp Emerson, Inland Empire Council's summer camp, for three years. Then, he received a commission as a second lieutenant in the US Army as a helicopter pilot. Charles retired from the Army after serving 21 years, and now has a graduate degree. During this his time in service, Charles participated in Scouting while stationed in Germany, Korea, Hawaii, and now, Colorado. Charles continues to work for the Department of Veterans Affairs Office of Community care in Denver. Here in Colorado, Charles has held the past positions as Cubmaster, Assistant Scoutmaster, Committee Chair, District Advancement Chairman and Venture Crew Advisor, and has been active in the Order of the Arrow. Both of Charles sons have earned their Eagle Scout award while in Troop 537, and he continues his passion for Scouting by leading and supporting many more adventures with this troop.</p>
    </div>

    <h2>Supporting Cast</h2>
    <p>While Troop 537 is a Scout led troop, we are fortunate to many very active Scouters and parents helping this group of Scouts by passing along their skills and experiences and being there to encourage the Scouts along on their journey to Eagle and beyond.</p>
    <div class="supporting-photos">
      <img src="https://troop537.com/wp-content/uploads/2020/08/IMG_0876-754x1024.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/08/image1-753x1024.jpg" alt="">
      <img src="https://www.troop537.com/wp-content/uploads/2021/12/IMG_1264-752x1024.jpg" alt="">
    </div>
    <p><img src="https://www.troop537.com/wp-content/uploads/2020/06/IMG_0883-300x234.jpg" alt="" style="max-width:300px;"></p>
"""

# ── CREW 537 ──────────────────────────────────────────
crew_content = """
    <h1>Crew 537</h1>
    <img class="crew-logo" src="https://www.troop537.com/wp-content/uploads/2022/11/venture-crew-logo.png" alt="Venture Crew">
    <p>Venture Crew 537 is now active, growing, and a key part of the growth and development of older existing Scouts and youth new to Scouting who are just interested in the high adventure trips.</p>
    <p>Venturing is a co-ed youth-led program all about building adventures with your friends. Choose to do activities that matter to you and develop essential skills like leadership, event-planning, organization, communication, and responsibility while having a blast!</p>
    <p>Venture Crew meets on Wed evenings at 7PM at this location:</p>
    <p>Charter Organization: Our Savior's Church<br>
    1975 S. Garrison St.,<br>
    Lakewood, CO 80227</p>
"""

# ── RECENT EVENTS ──────────────────────────────────────
events_content = """
    <h2><a href="#">Merry Weather 2025!</a></h2>
    <p class="post-meta">Posted on August 2, 2025 by Webmaster</p>
    <p>Our scouts traveled all the way to the pacific west coast to go the merry weather scout reservation. spending nights camping along side the beach, and having an awesome time at camp.</p>
    <div class="photo-gallery" style="margin-bottom:20px;">
      <img src="https://www.troop537.com/wp-content/uploads/2025/08/IMG_E5952-1024x745.jpg" alt="">
      <img src="https://www.troop537.com/wp-content/uploads/2025/08/IMG_E5953-2-1024x763.jpg" alt="">
    </div>

    <h2><a href="#">Patrol Cookoff 2025!</a></h2>
    <p class="post-meta">Posted on July 23, 2025 by Webmaster</p>
    <p>Our judges enjoying some delicious food prepared by our very own scouts, in a cook off dedicated to teaching our scouts about patrol boxes and camp out cooking.</p>
    <div class="photo-gallery" style="margin-bottom:20px;">
      <img src="https://www.troop537.com/wp-content/uploads/2025/08/IMG_E5954-1024x771.jpg" alt="">
    </div>

    <h2><a href="#">12 Day Philmont Trek</a></h2>
    <p class="post-meta">Posted on June 24, 2025 by Webmaster</p>
    <p>Congratulations to Crew 612-N on completing their 12 day Trek through the beautiful New Mexico backcountry. They were able to overcome all challenges thrown at them and pushed through to the end, while seeing breath taking views atop mount Phillips and the famous Tooth of Time.</p>
    <div class="photo-gallery" style="margin-bottom:20px;">
      <img src="https://www.troop537.com/wp-content/uploads/2025/08/CHHQ5084-1-1024x683.jpg" alt="">
      <img src="https://www.troop537.com/wp-content/uploads/2025/08/IMG_E5951-1-1024x747.jpg" alt="">
    </div>

    <h2><a href="#">Goose Creek Backpacking Trek 2025!</a></h2>
    <p class="post-meta">Posted on May 17, 2025 by Webmaster</p>
    <p>Our scouts went on a amazing backpacking trek into the wilderness of Colorado to goose creek. They went to visit the old man of the mountain, got to see the old abandoned car, the old lodging houses for the dam builders, and had a exciting time playing all over the rocks.</p>
    <div class="photo-gallery" style="margin-bottom:20px;">
      <img src="https://www.troop537.com/wp-content/uploads/2025/08/IMG_E5950-1024x453.jpg" alt="">
    </div>

    <h2><a href="#">Sand Dunes 2025!</a></h2>
    <p class="post-meta">Posted on April 12, 2025 by Webmaster</p>
    <p>Our scouts bathing in the sun atop the great sand dunes. Our troop traveled down to the San Luis Valley to spend a weekend at Great Sand Dunes National Park, hiking up to star dune and playing in the sand to create a amazing weekend.</p>
    <div class="photo-gallery" style="margin-bottom:20px;">
      <img src="https://www.troop537.com/wp-content/uploads/2025/08/IMG_E5949-1024x754.jpg" alt="">
    </div>

    <h2><a href="#">Gulch Clean Up 2025!</a></h2>
    <p class="post-meta">Posted on March 8, 2025 by Webmaster</p>
    <p>Our scouts took some time out of their busy lives to take part in a gulch clean up of the surrounding community by our church.</p>
    <div class="photo-gallery" style="margin-bottom:20px;">
      <img src="https://www.troop537.com/wp-content/uploads/2025/08/IMG_E5947.jpg" alt="">
    </div>

    <h2><a href="#">Night Hike 2024</a></h2>
    <p class="post-meta">Posted on December 6, 2024 by Webmaster</p>
    <p>Another troop night hike. We made it all the way to the top of green mountain with a beautiful Denver nighttime view.</p>
    <div class="photo-gallery" style="margin-bottom:20px;">
      <img src="https://www.troop537.com/wp-content/uploads/2025/08/IMG_E5948.jpg" alt="">
    </div>

    <h2><a href="#">Patrol Cookoff 2024!</a></h2>
    <p class="post-meta">Posted on November 20, 2024 by Webmaster</p>
    <p>Our older scouts judging the food made by our patrols with our fun challenge being you must use our closet food and limited ingredients in our annual patrol cook off competition.</p>
    <div class="photo-gallery" style="margin-bottom:20px;">
      <img src="https://www.troop537.com/wp-content/uploads/2025/08/IMG_E5957-1024x685.jpg" alt="">
    </div>

    <h2><a href="#">Jamboree 2024!</a></h2>
    <p class="post-meta">Posted on September 30, 2024 by Webmaster</p>
    <p>Our scouts got back from an awesome weekend up at Peaceful Valley Scout Ranch for the Colorado jamboree. They spent their time learning new skills that will help them on their scouting adventures and met tons of new scouts from across the state.</p>
    <div class="photo-gallery" style="margin-bottom:20px;">
      <img src="https://www.troop537.com/wp-content/uploads/2025/05/IMG_1511.jpeg" alt="">
    </div>

    <h2><a href="#">Melita Island 2024!</a></h2>
    <p class="post-meta">Posted on August 6, 2024 by Webmaster</p>
    <p>Our troop made it all the way up to Melita Island Scout Camp for an amazing week with incredible stops along the way like Glacier and Yellowstone National Park.</p>
    <div class="photo-gallery" style="margin-bottom:20px;">
      <img src="https://www.troop537.com/wp-content/uploads/2024/08/RIQS7152-1024x771.jpg" alt="">
    </div>
"""

# ── CALENDAR ───────────────────────────────────────────
calendar_content = """
    <h1>Calendar</h1>
    <p>Troop 537 upcoming events.</p>

    <div class="calendar-embed">
      <iframe src="https://calendar.google.com/calendar/embed?src=brl50k6ukvqdpnboaugkdv7lualhe5f4%40import.calendar.google.com&ctz=America%2FDenver" style="border:0" width="720" height="500" frameborder="0" scrolling="no"></iframe>
    </div>

    <p>How to subscribe to the Troop Calendar:</p>

    <h3>iOS calendar:</h3>
    <ul>
      <li>Copy this link: <a href="https://calendar.google.com/calendar/ical/brl50k6ukvqdpnboaugkdv7lualhe5f4%40import.calendar.google.com/public/basic.ics">Troop 537 Calendar Link</a></li>
      <li>Open your <strong>Settings</strong></li>
      <li>Select <strong>Passwords &amp; Accounts</strong></li>
      <li>Scroll down to and tap <strong>Add Account</strong></li>
      <li>Tap <strong>Other</strong> and on the next screen tap <strong>Add Subscribed Calendar</strong></li>
      <li>Now just paste in the link you copied. Tap in the box and hold for a second until the <strong>Paste</strong> option displays and tap it</li>
      <li>Tap <strong>Next</strong></li>
      <li>Tap <strong>Save</strong></li>
    </ul>

    <h3>Android calendar:</h3>
    <ul>
      <li>Since this is a Google calendar, you can click the "+" on the calendar above.</li>
      <li>Import manually by opening Google Calendar</li>
      <li>In the top right, click Settings &gt; Settings.</li>
      <li>In the menu on the left, click <strong>Import &amp; Export</strong>.</li>
      <li>Use this link: <a href="https://calendar.google.com/calendar/ical/brl50k6ukvqdpnboaugkdv7lualhe5f4%40import.calendar.google.com/public/basic.ics">Troop 537 Calendar Link</a></li>
      <li>Choose which calendar to add the imported events to.</li>
      <li>Click <strong>Import</strong>.</li>
    </ul>
"""

# ── PHOTOS ─────────────────────────────────────────────
photos_content = """
    <h1>Photos</h1>
    <div class="photo-gallery">
      <img src="https://www.troop537.com/wp-content/uploads/2021/03/DSC_0130-683x1024.jpg" alt="">
      <img src="https://www.troop537.com/wp-content/uploads/2021/03/DSC_0326-1024x721.jpg" alt="">
      <img src="https://www.troop537.com/wp-content/uploads/2021/03/DSC_0298-683x1024.jpg" alt="">
      <img src="https://www.troop537.com/wp-content/uploads/2021/03/DSC_0165-1024x658.jpg" alt="">
      <img src="https://www.troop537.com/wp-content/uploads/2021/07/canoe-skills-1024x576.jpg" alt="">
      <img src="https://www.troop537.com/wp-content/uploads/2021/07/IMG_0398-1024x554.jpg" alt="">
      <img src="https://www.troop537.com/wp-content/uploads/2021/07/DSC_8632-1024x902.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/07/DSC_1977-1024x523.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/07/20190716_170245-scaled.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/07/DSC_8899-1024x765.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/07/20190807_194414-1024x581.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/07/IMG_1248-1024x227.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/07/IMG_1301-1024x768.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/07/IMG_0956-1024x768.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/07/IMG_0906-1024x768.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/07/DSC_5757-1024x683.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/07/DSC_5387-1024x683.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/07/DSC_5494-1024x498.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/07/20190817_185306-1024x768.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/07/DSC_3734-1-1024x683.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/07/DSC_4683-1024x580.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/07/IMG_E0674-1020x1024.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/07/DSC_6110-1024x612.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/07/IMG_0059-1024x447.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/09/20200229_130844_resized-1024x768.jpg" alt="">
      <img src="https://troop537.com/wp-content/uploads/2020/12/IMG_1851-2-1024x742.jpg" alt="">
    </div>
"""

# ── PARENTS ────────────────────────────────────────────
parents_content = """
    <h1>Parents</h1>
    <p>Welcome to Scouting! Through Scouting, youth develop strong connections and make important contributions to their families, their community, and society at large. Scouting provides the key ingredients for helping youth grow into competent, caring, and confident adults. Research about our highly effective programs has shown that these ingredients are:</p>
    <ul>
      <li>Positive and sustained adult-youth relationships</li>
      <li>Youth activities that build life skills</li>
      <li>Youth participation in and leadership of valued community activities</li>
    </ul>
    <p>The Scouting program significantly enhances opportunities for personal development, including higher grades, school engagement, self-esteem, and resilience. The program provides a safe environment where relationships are built with caring and competent adults, where youth are encouraged to take leadership of their development, and where useful life skills are acquired.</p>
    <p>Troop 537 has a very active adult leadership team and are fully committed growing and protecting our youth. Each one of our leaders is certified by BSA and has fulfilled the <a href="https://www.denverboyscouts.org/resources/other-useful-resources/background-check-requirements/" target="_blank">background check requirements</a> maintained by our council. If you are interested in joining our troop and/or becoming an adult leader with Troop 537, please look over the available BSA <a href="https://www.scouting.org/training/adult/" target="_blank">Adult Training</a> &amp; <a href="https://www.scouting.org/training/youth-protection/" target="_blank">Youth Protection</a> information. Also, additional adult training resources specific to Denver <a href="https://www.denverboyscouts.org/resources/adult-training-programs/" target="_blank">can be found here</a>.</p>
    <p>If you have any questions about the leadership of our troop, or if you are interested in participating as an adult, please let us know! <a href="contact.html">You can contact us here</a>, and we will respond as soon as possible.</p>
"""

# ── RESOURCES ──────────────────────────────────────────
resources_content = """
    <h1>Resources</h1>
    <div class="clearfix">
      <img class="resource-img" src="https://troop537.com/wp-content/uploads/2020/06/denver-area-coucil.jpg" alt="Denver Area Council">
      <p>Troop 537 is part of the <strong>Alpine District</strong> (<a href="https://scoutingcolorado.org/districts/alpine/" target="_blank">https://scoutingcolorado.org/districts/alpine/</a>) in the <strong>Greater Colorado Council</strong> (<a href="https://scoutingcolorado.org/" target="_blank">https://scoutingcolorado.org/</a>).</p>
      <p>Support Troop 537 – If you would like to donate to Troop 537, please <a href="contact.html">contact us directly</a> to take donations. If you would like to support Troop 537 through our <a href="https://www.troop537.com/wp-content/uploads/2024/05/Support-537-at-King-Soopers.pdf" target="_blank">King Soopers program</a>, you can sign up here and part of your grocery spend will be donated to us! This is a fantastic program that has supported our Troop for many years. <a href="https://www.troop537.com/wp-content/uploads/2024/05/Support-537-at-King-Soopers.pdf" target="_blank">Read more here.</a></p>
      <p><strong>Merit Badges</strong> – There are currently <a href="https://www.scouting.org/programs/scouts-bsa/advancement-and-awards/merit-badges/" target="_blank">135 Merit Badges available</a>. You can see them all here. When working on a Merit Badge, you should print a workbook to keep track of your progress – <a href="http://usscouts.org/mb/worksheets/list.asp" target="_blank">Merit Badge Workbooks</a>. Our troop has Merit Badge counselors to cover each of these.</p>
      <p><strong>Local Campgrounds</strong> – The <a href="https://www.troop537.com/wp-content/uploads/2021/07/Forest-Service-Campgrounds.pdf" target="_blank">Rocky Mountain Region Campground List</a> and the contact information – <a href="https://www.troop537.com/wp-content/uploads/2021/07/Forest-Service-Campgrounds.pdf" target="_blank">Rocky Mountain Region Directory</a>.</p>
    </div>
"""

# ── CONTACT ────────────────────────────────────────────
contact_content = """
    <h1>Contact</h1>
    <p>Are you interested in joining our Troop or want more information?</p>
    <div class="contact-form">
      <form action="https://formspree.io/f/REPLACE_WITH_YOUR_ID" method="POST">
        <div class="field-row">
          <label>Name *</label>
          <div class="name-row">
            <div>
              <input type="text" name="first_name" placeholder="First" required>
            </div>
            <div>
              <input type="text" name="last_name" placeholder="Last" required>
            </div>
          </div>
        </div>
        <div class="field-row">
          <label>Email *</label>
          <input type="email" name="email" required>
        </div>
        <div class="field-row">
          <label>Comment or Message *</label>
          <textarea name="message" required></textarea>
        </div>
        <div class="field-row">
          <button type="submit" class="submit-btn">Submit</button>
        </div>
      </form>
    </div>
    <p style="margin-top:16px;"><img src="https://www.troop537.com/wp-content/uploads/2020/06/IMG_0883-300x234.jpg" alt="" style="max-width:300px;"></p>
"""

pages = [
    ('index.html',        'Troop and Crew 537',    'home',      home_hero,  home_content),
    ('about.html',        'About Troop 537',        'about',     '',         about_content),
    ('crew.html',         'Crew 537',               'crew',      '',         crew_content),
    ('recent-events.html','Recent Events',          'events',    '',         events_content),
    ('calendar.html',     'Calendar',               'calendar',  '',         calendar_content),
    ('photos.html',       'Photos',                 'photos',    '',         photos_content),
    ('parents.html',      'Parents',                'parents',   '',         parents_content),
    ('resources.html',    'Resources',              'resources', '',         resources_content),
    ('contact.html',      'Contact',                'contact',   '',         contact_content),
]

import os
out = '/home/claude/troop537'
for fname, title, current, hero, content in pages:
    html = page(title, current, hero, content)
    with open(os.path.join(out, fname), 'w') as f:
        f.write(html)
    print(f'Written: {fname}')

print('All pages done.')
