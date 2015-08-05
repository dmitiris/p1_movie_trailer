from media import Movie
import fresh_tomatoes

# MOVIE DATA
mission_impossible = Movie(
    movie_title = "Mission: Impossible – Rogue Nation",
    movie_storyline = ("With the IMF disbanded, and Ethan (Tom Cruise) out "
                       "in the cold, the team now faces off against a network "
                       "of highly skilled special agents, the Syndicate. "
                       "These highly trained operatives are hellbent on "
                       "creating a new world order through an escalating "
                       "series of terrorist attacks. Ethan gathers his team "
                       "and joins forces with disavowed British agent Ilsa "
                       "Faust (Rebecca Ferguson), who may or may not be a "
                       "member of this rogue nation, as the group faces their "
                       "most impossible mission yet."),
    movie_poster = "https://upload.wikimedia.org/wikipedia/en/f/fb/Mission_Impossible_Rogue_Nation_poster.jpg",
    trailer_youtube = "https://youtu.be/F-qBD17wwrQ",    
    )

ant_man = Movie(
    movie_title = "Ant-man",
    movie_storyline = ("Armed with the astonishing ability to shrink in scale "
                       "but increase in strength, master thief Scott Lang "
                       "must embrace his inner-hero and help his mentor, Dr. "
                       "Hank Pym, protect the secret behind his spectacular "
                       "Ant-Man suit from a new generation of towering threats."
                       " Against seemingly insurmountable obstacles, Pym and "
                       "Lang must plan and pull off a heist that will save the "
                       "world."),
    movie_poster = "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg", # URL
    trailer_youtube = "https://www.youtube.com/watch?v=pWdKf3MneyI",
    )

vacation = Movie(
    movie_title = "Vacation",
    movie_storyline = ("Following in his father's footsteps and hoping for "
                       "some much-needed family bondling, a grown-up Rusty "
                       "Griswold surprises his wife, Debbie, and their two "
                       "sons with a cross-country trip back to America's "
                       '"favorite family fun park," '
                       "Walley World."),
    movie_poster = "https://upload.wikimedia.org/wikipedia/en/1/19/Vacation_poster.jpg",
    trailer_youtube = "https://www.youtube.com/watch?v=SgqtBV8WKJw",
    )

minions = Movie(
    movie_title = "Minions",
    movie_storyline = ("Minions Stuart, Kevin and Bob are recruited by "
                       "Scarlet Overkill, a super-villain who, alongside her "
                       "inventor husband Herb, hatches a plot to take over "
                       "the world."),
    movie_poster = "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",
    trailer_youtube = "https://www.youtube.com/watch?v=Wfql_DoHRKc",
    )

pixels = Movie(
    movie_title = "Pixels",
    movie_storyline = ("As kids in the 1980s, Sam Brenner, Will Cooper, "
                       "Ludlow Lamonsoff, and Eddie “The Fire Blaster” Plant "
                       "saved the world thousands of times – at 25 cents a "
                       "game in the video arcades. Now, they’re going to have "
                       "to do it for real. In Pixels, when intergalactic "
                       "aliens discover video feeds of classic arcade games "
                       "and misinterpret them as a declaration of war, they "
                       "attack the Earth, using the video games as the models "
                       "for their assaults -- and now-U.S. President Cooper "
                       "must call on his old-school arcade friends to save "
                       "the world from being destroyed by PAC-MAN, Donkey "
                       "Kong, Galaga, Centipede, and Space Invaders. Joining "
                       "them is Lt. Col. Violet Van Patten, a specialist "
                       "supplying the arcaders with unique weapons to fight "
                       "the aliens."),
    movie_poster = "https://upload.wikimedia.org/wikipedia/en/f/f0/PixelsOfficialPoster.jpg",
    trailer_youtube = "https://youtu.be/eIOcWZOQL5M",
    )

trainwreck = Movie(
    movie_title = "Trainwreck",
    movie_storyline = ("Since she was a little girl, it’s been drilled into "
                       "Amy’s head by her rascal of a dad that monogamy isn’t "
                       "realistic. Now a magazine writer, Amy lives by that "
                       "credo—enjoying what she feels is an uninhibited life "
                       "free from stifling, boring romantic commitment—but "
                       "in actuality, she’s kind of in a rut. When she finds "
                       "herself starting to fall for the subject of the new "
                       "article she’s writing, a charming and successful "
                       "sports doctor named Aaron Conners, Amy starts to "
                       "wonder if other grown-ups, including this guy who "
                       "really seems to like her, might be on to something."),
    movie_poster = "https://upload.wikimedia.org/wikipedia/en/c/c5/Trainwreck_poster.jpg",
    trailer_youtube = "https://www.youtube.com/watch?v=y_KP9x80Z9Q",
    )


## object Movie structure
##movie_name = Movie(
##    movie_title = "", # Text
##    movie_storyline = (""), # Text
##    movie_poster = "", # URL
##    trailer_youtube = "", # URL
##    )

# making a list of Movie objects
movie_list = [minions, ant_man, vacation,
              mission_impossible, pixels, trainwreck]

# Generating web-page
# open_movies_page() takes a list of Movie objects to generate a web-page and open
# it in default browser
fresh_tomatoes.open_movies_page(movie_list)
