"""Sample journal, atlas, and kit for a fictional traveler."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Post:
    """One filed dispatch."""

    slug: str
    number: str
    title: str
    kicker: str
    dek: str
    date: str
    place: str
    continent: str
    read_time: str
    lead_initial: str
    lead_rest: str
    pull: str
    body: list[str]
    href: str


@dataclass(frozen=True)
class Place:
    """A destination Inez returns to, or means to."""

    name: str
    country: str
    continent: str
    season: str
    latitude: str
    summary: str
    note: str
    dispatch_slug: str = ""


@dataclass(frozen=True)
class KitItem:
    """Something that earns a place in the bag."""

    id: str
    category: str
    label: str
    note: str


def _post(
    slug: str,
    number: str,
    title: str,
    kicker: str,
    dek: str,
    date: str,
    place: str,
    continent: str,
    read_time: str,
    lead: str,
    pull: str,
    body: tuple[str, ...],
) -> Post:
    return Post(
        slug=slug,
        number=number,
        title=title,
        kicker=kicker,
        dek=dek,
        date=date,
        place=place,
        continent=continent,
        read_time=read_time,
        lead_initial=lead[0],
        lead_rest=lead[1:],
        pull=pull,
        body=list(body),
        href=f"/dispatches/{slug}",
    )


POSTS: tuple[Post, ...] = (
    _post(
        slug="night-train-thessaloniki",
        number="01",
        title="The Last Night Train to Thessaloniki",
        kicker="Europe · Dispatch 41",
        dek="A sleeper that still punches paper tickets, and the station cats who know the timetable better than anyone on the platform.",
        date="12 September 2026",
        place="Thessaloniki, Greece",
        continent="Europe",
        read_time="8 min",
        lead="The conductor still uses a hole punch. I watched him line my ticket up with the window light, as if the hole had to land on a particular kilometer.",
        pull="The interesting part of a railway was never the arrival. It was the permission to be between places.",
        body=(
            "We left Athens late enough that the city had given up performing. The carriage smelled of orange peel and a detergent I have met on three other railways, which makes me think there is a single factory somewhere that supplies every sleeper in southern Europe.",
            "My berth mate was a dentist from Larissa who unpacked a tin of almonds and did not offer any, which I respected. He read the football pages with a pencil. Around Lamia he turned the light off without asking, and he was right to.",
            "I woke once in a station that was only a platform and a dog. The dog looked employed. Somewhere a radio was playing a song that had already been old when the carriage was new. I wrote down the name of the station and in the morning I could not read my own handwriting.",
            "Thessaloniki at dawn is a city arguing with its sea. I walked the waterfront before the cafés had decided to be open, bought a sesame ring from a man who was not officially there, and ate it sitting on my case. The ticket, with its careful hole, is still in the notebook. I do not collect tickets. I just have not thrown this one away.",
        ),
    ),
    _post(
        slug="market-rain-stone-town",
        number="02",
        title="Market Rain in Stone Town",
        kicker="Africa · Dispatch 38",
        dek="Clove smoke, a borrowed umbrella, and the hour when the market stops selling and starts talking.",
        date="3 June 2026",
        place="Stone Town, Zanzibar",
        continent="Africa",
        read_time="7 min",
        lead="The rain arrived sideways, which the fish sellers treated as a suggestion rather than a reason to close.",
        pull="A market is a city telling you the truth before it has had coffee.",
        body=(
            "I had come for the doors, like everyone who has read one book. The doors are beautiful and they know it. The market does not know it, which is why I stayed. A woman selling limes lent me half an umbrella and kept the half that faced the wind. She said the rain would be finished before the call to prayer. She was off by four minutes, which is better than any forecast I have paid for.",
            "Under the tin roof the air was clove, diesel, and the sweet rot of mango. A boy ran a tray of coffee through the aisles as if the rain were a room he had to cross. I drank one standing up. It was thick enough to count as breakfast and bitter enough to count as a decision.",
            "In the afternoon the alleys steamed. I got lost on purpose and then by accident, which is a different and less romantic thing. A man repairing a radio pointed me back toward the sea with his screwdriver and did not look up. I found the house I was staying in by the color of the cat on the step, not by the number.",
            "I wrote this at a plastic table while my shoes dried on a second chair. The lime seller's umbrella is by the door. I am to return it in the morning, which means I have a plan, which is more than I had when the ferry docked.",
        ),
    ),
    _post(
        slug="kitchen-facing-the-andes",
        number="03",
        title="A Kitchen That Faces the Andes",
        kicker="South America · Dispatch 36",
        dek="Altitude, a borrowed stove, and the potato that finally convinced me to sit down.",
        date="18 March 2026",
        place="Cusco, Peru",
        continent="South America",
        read_time="9 min",
        lead="The stove was not mine, and neither was the view, but the woman who owned both told me to use the smaller burner because the larger one lied about its heat.",
        pull="At altitude, ambition is a kind of rudeness. The city would like you to sit.",
        body=(
            "I had arrived the day before and spent it pretending I was not breathless. Cusco is patient with this performance and then, around hour twenty, it stops being patient. I sat on the kitchen step with a cup of coca tea that tasted like wet hay and good intentions, and I watched the mountains do nothing, which was the point.",
            "The house belonged to a friend of a friend, a violin teacher who travels with a photograph of her students and a rule about shoes. She showed me the market by pointing from the roof: meat there, flowers there, the bread that is worth the walk, the bread that is a trick. I went down too fast and had to stand in a doorway until the black spots left.",
            "Dinner was potatoes in more forms than I had names for, and a fried egg that I was allowed to cook myself once I had been judged competent with the smaller burner. We ate with the door open. Someone in the next building was practicing the same four bars of a waltz, badly, and then suddenly well.",
            "I slept under two blankets and woke to frost on the roof tiles and the violin teacher already gone to a lesson, a note on the table that said the bread worth the walk would be gone by eight. It was seven-twenty. I put on the shoes. I did not run.",
        ),
    ),
    _post(
        slug="ferry-grammar-seto",
        number="04",
        title="Ferry Grammar in the Seto Inland Sea",
        kicker="Asia · Dispatch 33",
        dek="Island hopping by timetable, and the small grammar of boats that leave whether you are ready or not.",
        date="29 November 2025",
        place="Naoshima, Japan",
        continent="Asia",
        read_time="8 min",
        lead="The ferry did not care that I had understood the sign. It left while I was still being proud of having understood the sign.",
        pull="A timetable is a poem with consequences.",
        body=(
            "I made the next one by running, which in November, with a bag that has opinions, is a short and undignified sport. An older woman on the bench by the rail watched me with the calm of someone who has missed this ferry on purpose at least once. She offered me a tangerine and the information that the good seat is the one that faces backward. She was right about the seat.",
            "The inland sea in late autumn is a stack of gray papers. Islands appear, then decide they are clouds. I wrote down the names I could read and left blank lines for the ones I could not. A high school team in matching jackets slept in a pile like coats.",
            "Naoshima, when I finally stepped onto it, was quieter than the postcards. The art is there, and it is serious, and it does not need me to describe it. What I will keep is the vending machine at the top of a hill that sold hot corn soup, and the man refilling it who nodded as if I had arrived at the correct hour of my life.",
            "I have started to think of ferries as grammar. There is the departure, which is a full stop you do not get to negotiate, and the crossing, which is a long subordinate clause, and the dock, which is where the sentence finds out what it was about. I missed the first full stop and still liked the sentence.",
        ),
    ),
    _post(
        slug="red-dust-kimberley",
        number="05",
        title="Red Dust and a Borrowed Hat",
        kicker="Oceania · Dispatch 29",
        dek="A road that forgets you, a hat that belonged to someone more sensible, and the color red doing all the talking.",
        date="7 August 2025",
        place="The Kimberley, Australia",
        continent="Oceania",
        read_time="8 min",
        lead="The hat was too big and had belonged to the station cook, who said I could have it if I brought it back with the same amount of head inside.",
        pull="Distance out here is not a number. It is a decision you keep making.",
        body=(
            "I had come up from Broome in a shared truck with a hydrologist, a dog, and a carton of mangoes that did not survive the dog. The road was the color of a brick that has been thinking about fire. Every hour the radio found a song and then lost it, as if the songs lived in the creeks.",
            "We stopped where a hand-painted sign promised fuel and delivered a fridge, a chair, and a woman reading a novel with the cover torn off. She sold me water, a meat pie of philosophical dryness, and the advice to put the hat on before I needed it, not after. The hydrologist talked to the dog about aquifers. I wrote nothing. The page would only have said red, red, red.",
            "In the late light the boab trees looked like they had been inflated by a rumor. I walked out from the fuel sign until the truck was small and then walked back, which is the entire plot of a lot of stories about this country, and also the correct plot. The cook's hat smelled like woodsmoke and dish soap.",
            "That night we slept in swags and I listened to something move through the grass with the confidence of a local. In the morning the hat was still a hat. I returned it with the same amount of head. The cook looked inside, nodded, and gave me a mango the dog had missed. It tasted like July pretending to be generous.",
        ),
    ),
    _post(
        slug="winter-light-st-lawrence",
        number="06",
        title="Winter Light on the St. Lawrence",
        kicker="North America · Dispatch 27",
        dek="Ice, a diner that takes its pie seriously, and a wrong turn that turned out to be the point.",
        date="14 February 2025",
        place="Kamouraska, Québec",
        continent="North America",
        read_time="7 min",
        lead="I took the wrong road out of the village and the wrong road was the one with the view, which is the only kind of mistake I trust.",
        pull="Winter is honest about distance. It does not bother to decorate it.",
        body=(
            "Kamouraska in February is a town made of wood, smoke, and the long bright fact of the river. The ice on the St. Lawrence did not look like a metaphor. It looked like ice, and it went all the way to a horizon that seemed to have been ironed.",
            "I had meant to stay one night and stayed for four, because the woman at the bakery asked if I had tried the next village and I had not, and because the room above the diner was warm in a way that felt earned rather than purchased. The diner pie was maple and also a test of character. I failed it twice a day.",
            "On the wrong road I met a man salting his steps who wanted to know where I thought I was going, and when I told him, he said that road was fine if I liked looking at the same beautiful thing for a long time. I said I did. He said that was unusual for someone with a suitcase, and then he told me where the road actually ended, which was a church, a fence, and the wind.",
            "I wrote the last page of that notebook there, glove off, until the pen complained. The light was the color of weak tea and brass. A ship sat in the ice like a building that had changed its mind. I walked back to the diner the long way, on purpose, and ordered the pie before I took my coat off.",
        ),
    ),
)

POSTS_BY_SLUG = {post.slug: post for post in POSTS}

MISSING = Post(
    slug="",
    number="",
    title="This dispatch was never filed",
    kicker="",
    dek="",
    date="",
    place="",
    continent="",
    read_time="",
    lead_initial="",
    lead_rest="",
    pull="",
    body=[],
    href="/dispatches",
)

PLACES: tuple[Place, ...] = (
    Place(
        name="Lisbon",
        country="Portugal",
        continent="Europe",
        season="Spring, and whenever the rent is due",
        latitude="38.72° N",
        summary="The nominal home. A rented room in Alfama with a kettle that takes its time and a window that faces a wall the color of a late peach.",
        note="Tram 28 is a performance. The 760 bus to the station is the city.",
    ),
    Place(
        name="Thessaloniki",
        country="Greece",
        continent="Europe",
        season="Early autumn",
        latitude="40.64° N",
        summary="Arrive by sleeper if you can still find one. The waterfront is already in an argument with the morning, and you will want to take a side.",
        note="Eat the sesame ring before you look for a café. The café can wait.",
        dispatch_slug="night-train-thessaloniki",
    ),
    Place(
        name="Palermo",
        country="Italy",
        continent="Europe",
        season="Late spring, before the heat makes a speech",
        latitude="38.12° N",
        summary="Markets first, sea second, any plan third. The ferries leave when they feel like it, which is its own kind of timetable.",
        note="Keep the photocopy of your passport somewhere the laundry cannot reach.",
    ),
    Place(
        name="Stone Town",
        country="Zanzibar",
        continent="Africa",
        season="The short rains",
        latitude="6.16° S",
        summary="A coral city that smells of clove and rain on hot stone. The carved doors are famous. The market is the better chapter.",
        note="Return the umbrella. It was a loan, not a souvenir.",
        dispatch_slug="market-rain-stone-town",
    ),
    Place(
        name="Saint-Louis",
        country="Senegal",
        continent="Africa",
        season="Dry season, late afternoon",
        latitude="16.03° N",
        summary="A river island where the colonial grid runs out of paint and the light turns the water the color of weak tea.",
        note="Cross the bridge on foot at least once, when the wind is doing the work.",
    ),
    Place(
        name="Chefchaouen",
        country="Morocco",
        continent="Africa",
        season="Spring mornings",
        latitude="35.17° N",
        summary="Blue stairs, a bus that stops for sheep, and a town that looks staged until you buy bread and the spell becomes ordinary.",
        note="The blue is real. The quiet is not, once the day tours arrive. Go earlier.",
    ),
    Place(
        name="Naoshima",
        country="Japan",
        continent="Asia",
        season="Late November",
        latitude="34.46° N",
        summary="An island in the Seto Inland Sea where the ferries are more precise than your intentions. Art everywhere, and a hilltop vending machine that sells soup.",
        note="Face backward on the boat. The islands arrange themselves better that way.",
        dispatch_slug="ferry-grammar-seto",
    ),
    Place(
        name="Luang Prabang",
        country="Laos",
        continent="Asia",
        season="The cool weeks after the river drops",
        latitude="19.89° N",
        summary="Dawn alms, a slow Mekong, and French colonial porches that have outlived the empire that built them. The town closes its voice at night.",
        note="Skip the first café on the main street. The second one knows your order is not a personality.",
    ),
    Place(
        name="George Town",
        country="Penang, Malaysia",
        continent="Asia",
        season="Any month you can stand the shine on the street",
        latitude="5.41° N",
        summary="Clan jetties, a mural you can ignore, and breakfast that requires no commentary. The ferry to the mainland is the honest way in.",
        note="Order the kopi. Sit long enough that the fan becomes part of the sentence.",
    ),
    Place(
        name="Cusco",
        country="Peru",
        continent="South America",
        season="March, when the mountains are blunt",
        latitude="13.53° S",
        summary="A high city that would like you to sit down. Borrow a kitchen if you are offered one. The potatoes will explain the rest.",
        note="The smaller burner tells the truth. Walk downhill slowly.",
        dispatch_slug="kitchen-facing-the-andes",
    ),
    Place(
        name="Valparaíso",
        country="Chile",
        continent="South America",
        season="Shoulder season, when the fog has opinions",
        latitude="33.05° S",
        summary="A port stacked like a dare. Ascensors, peeling paint, and a sea that looks cold even when it is not your business to swim.",
        note="Take the funicular up and the stairs down. The city reads better in that direction.",
    ),
    Place(
        name="Kamouraska",
        country="Québec",
        continent="North America",
        season="February, on purpose",
        latitude="47.57° N",
        summary="A village on the St. Lawrence where the ice does not bother to be picturesque. There is a diner, a bakery, and a wrong road with the right view.",
        note="Order the pie before you take your coat off. The coat can wait. The pie has a schedule.",
        dispatch_slug="winter-light-st-lawrence",
    ),
    Place(
        name="Oaxaca",
        country="Mexico",
        continent="North America",
        season="The weeks after the rains",
        latitude="17.07° N",
        summary="Markets with a grammar of their own, a zócalo that performs every evening, and kitchens that will correct your idea of a mole.",
        note="Learn the name of one bread and stick with it until the baker trusts you with a second.",
    ),
    Place(
        name="Broome",
        country="Australia",
        continent="Oceania",
        season="The dry, before the build-up",
        latitude="17.96° S",
        summary="A pearling town where the light goes red and stays there. Camel trains on the beach are for other people. The road north is the story.",
        note="Borrow a hat from someone who has already made the mistakes.",
        dispatch_slug="red-dust-kimberley",
    ),
    Place(
        name="Hobart",
        country="Tasmania",
        continent="Oceania",
        season="Late winter into a reluctant spring",
        latitude="42.88° S",
        summary="A harbour city with a mountain on its shoulder and a market that still feels like a Saturday rather than a brand. The ferry south is worth the wind.",
        note="Eat something smoked. Walk until the mountain becomes a fact instead of a view.",
    ),
)

CONTINENTS: tuple[str, ...] = (
    "All",
    "Africa",
    "Asia",
    "Europe",
    "North America",
    "Oceania",
    "South America",
)

KIT_ITEMS: tuple[KitItem, ...] = (
    KitItem("passport", "Papers", "Passport, and a photocopy in the other bag", "The copy once survived a laundry mix-up in Palermo."),
    KitItem("tickets", "Papers", "Paper tickets, even when a code exists", "Station machines prefer to die at the interesting hour."),
    KitItem("addresses", "Papers", "A card of handwritten addresses", "Phones get wet. Pencil does not."),
    KitItem("dress", "On the body", "One charcoal dress", "It can be rinsed in a sink and look intentional by dinner."),
    KitItem("wool", "On the body", "A thin wool layer, even in July", "Platforms are a different climate from the city they claim to serve."),
    KitItem("shoes", "On the body", "Shoes that are already broken in", "New shoes are a letter she refuses to write."),
    KitItem("scarf", "On the body", "A square scarf", "Sun, dust, and the shoulders of churches."),
    KitItem("sleep", "Night trains", "Earplugs and a mask", "The second berth always snores in a new language."),
    KitItem("lock", "Night trains", "A small lock for the berth", "Not a fortress. Just a way to sleep."),
    KitItem("cash", "Night trains", "Small notes for the attendant", "Kept separate from the rest of the money, so the thanks is ready."),
    KitItem("bottle", "Night trains", "A bottle, empty at the checkpoint", "Filled at the platform tap, after security has had its moment."),
    KitItem("bags", "Markets", "Two cloth bags", "Plastic is a habit she is trying to leave in 2019."),
    KitItem("salt", "Markets", "A tin of salt", "Borrowed kitchens are generous with everything except this."),
    KitItem("cup", "Markets", "A metal cup and a twist of tea", "The cup has outlasted three kettles that were not hers."),
    KitItem("spoon", "Markets", "A short spoon", "It has outlasted the knives she was asked to surrender."),
    KitItem("notebook", "The notebook", "A cheap notebook", "If the page is precious, she will not write the true thing."),
    KitItem("pen", "The notebook", "A pen that writes on damp paper", "Rain is not an editorial excuse."),
    KitItem("pencil", "The notebook", "A pencil for the margins", "For markets, timetables, and the names of dogs."),
)

KIT_TOTAL = len(KIT_ITEMS)

TIMELINE: tuple[tuple[str, str, str], ...] = (
    ("2014", "Setúbal", "An aunt who ran the station kiosk teaches her which trains are real and which are printed to comfort people."),
    ("2016", "Lisbon", "A desk at a regional operator. She edits timetables and starts keeping a private column for the minutes nobody admits."),
    ("2019", "A copper evening", "She leaves the job in the week the roofs in Alfama go the color of a pan left too long on the heat. The journal gets its name."),
    ("2022", "The St. Lawrence", "First winter on purpose. She learns that a wrong road can be the assignment."),
    ("2025", "The Kimberley", "Red dust, a borrowed hat, and a page that only says one word, three times."),
    ("2026", "This issue", "Between stations. The sleeper to Thessaloniki is the newest page, and it is not the last."),
)

METHOD: tuple[tuple[str, str], ...] = (
    ("Trains and ferries first", "She flies only when the land and the water have both refused. A journey under four days is not an emergency."),
    ("No new shoes", "Blisters are a failure of planning, and planning is the one vanity she kept from the timetable desk."),
    ("Write it the same day", "Memory edits overnight. The notebook gets the version with the dent still in it."),
    ("Nothing sponsored", "The journal is paid for by a small kiosk inheritance and the occasional essay for a Lisbon review. If a place wants a mention, it can be interesting."),
    ("Return what you borrow", "Umbrellas, hats, burners, and the quieter half of a conversation."),
)
