# Notes:
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    disabled_events: list[int | str] = []

    i = 1  # ==== hinamizawa_sonmin_shuukai1 ====
    if i not in disabled_events:
        event_name = f"hinamizawa_sonmin_shuukai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "01_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/2/https://mattari-an.net/shu-kai/1st/index.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="チラシ絵提供：珠洲城くるみ 様 (MilkCandy)",
            ),
            Medium(
                "01_20080117170741_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20080117170741/http://shu-kai.hinamizawa.info/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1590924, 136.9298891),
                address="2 Chome-6-3 Fukiage, Chikusa Ward, Nagoya, Aichi 464-0856, Japan",
                description="名古屋中小企業福祉会館 ６階ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20080117170741/http://shu-kai.hinamizawa.info/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWkq7ADwtY0_LzlU3mk0DFlmJeNo1bo9bpZ2vqyiopbdHLCB4zA_pSkSpa9YKGQsJgPRhkx6a0R8e8OPBlstCq-5saYTJ5-avtnX6fZR-cI6YHIZgV7pYeOLMsw_PDlSU2wW-9f9=s0?imgmax=0",
                url="https://maps.app.goo.gl/5QerDbUB3hz5Xcjq9",
            ),
        ]
        event = Event(
            aliases=[
                "雛見沢村民集会",
                "雛見沢村民集会1",
                "Hinamizawa Sonmin Shuukai 1",
            ],
            dates="2008.06.29",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20080117170741/http://shu-kai.hinamizawa.info/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20250628073152/https://mattari-an.net/shu-kai/1st/list.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.10.18",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 2  # ==== hinamizawa_sonmin_shuukai2 ====
    if i not in disabled_events:
        event_name = f"hinamizawa_sonmin_shuukai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "02_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20250628073415/https://mattari-an.net/shu-kai/2nd/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="表紙絵提供：珠洲城くるみ 様 (MilkCandy)",
            ),
            Medium(
                "02_Witch's_tanabata_cover.webp",
                [
                    Source(
                        "https://07th-expansion.fandom.com/wiki/Hinamizawa_Village_Assembly",
                        (RT.Likely, OT.External),
                    )
                ],
            ),
            Medium(
                "02_kannai.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20250524172154/https://mattari-an.net/shu-kai/2nd/kannai.jpg",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "https://web.archive.org/web/2/https://mattari-an.net/shu-kai/2nd/kannai.pdf",
                [
                    Source(
                        "https://web.archive.org/web/2/https://mattari-an.net/shu-kai/2nd/kannai.pdf",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1590924, 136.9298891),
                address="2 Chome-6-3 Fukiage, Chikusa Ward, Nagoya, Aichi 464-0856, Japan",
                description="名古屋中小企業福祉会館 ６階ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20081217140801/http://shu-kai.hinamizawa.info:80/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWkq7ADwtY0_LzlU3mk0DFlmJeNo1bo9bpZ2vqyiopbdHLCB4zA_pSkSpa9YKGQsJgPRhkx6a0R8e8OPBlstCq-5saYTJ5-avtnX6fZR-cI6YHIZgV7pYeOLMsw_PDlSU2wW-9f9=s0?imgmax=0",
                url="https://maps.app.goo.gl/5QerDbUB3hz5Xcjq9",
            ),
        ]
        event = Event(
            aliases=["雛見沢村民集会2", "Hinamizawa Sonmin Shuukai 2"],
            dates="2009.06.28",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20081217140801/http://shu-kai.hinamizawa.info:80/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20250521165848/https://mattari-an.net/shu-kai/2nd/list.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2018.10.18",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 3  # ==== hinamizawa_sonmin_shuukai3 ====
    if i not in disabled_events:
        event_name = f"hinamizawa_sonmin_shuukai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "03_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20250628074352/https://mattari-an.net/shu-kai/3rd/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="表紙絵提供：珠洲城くるみ 様（MilkCandy）",
            ),
            Medium(
                "03_Jessica_love_charm_cover.webp",
                [
                    Source(
                        "https://07th-expansion.fandom.com/wiki/Hinamizawa_Village_Assembly",
                        (ReliabilityTypes.Likely, OriginTypes.External),
                    )
                ],
            ),
            Medium(
                "https://web.archive.org/web/20250522090708/https://mattari-an.net/shu-kai/3rd/kannai.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20250628075503/https://mattari-an.net/shu-kai/3rd/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "https://web.archive.org/web/20250522122309/https://mattari-an.net/shu-kai/3rd/kannai.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20250522122309/https://mattari-an.net/shu-kai/3rd/kannai.pdf",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.0960914, 136.9241402),
                address="5 Chome-1-16 Higashimatabeecho, Minami Ward, Nagoya, Aichi 457-0833, Japan",
                description="日本ガイシフォーラム",
                sources=[
                    Source(
                        "https://web.archive.org/web/20250628074352/https://mattari-an.net/shu-kai/3rd/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmj8MzT8MDc2f6y-m4HKbW409CgcjzT-W5sICqc_6FGCydMMyIdsr37ZfspiGt3FF4_viq4XCwlLXeK4sHeI428n6LGylj2FGApSjctQAT_dR0dwUcv0i9FQt7mKQ5a4YH401m5Ig=s0?imgmax=0",
                url="https://maps.app.goo.gl/UY9XC3cm89b4qD8g7",
            ),
        ]
        event = Event(
            aliases=["雛見沢村民集会3", "Hinamizawa Sonmin Shuukai 3"],
            dates="2010.06.27",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20250628074352/https://mattari-an.net/shu-kai/3rd/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20250628075503/https://mattari-an.net/shu-kai/3rd/list.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2018.10.18",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 4  # ==== hinamizawa_sonmin_shuukai4 ====
    if i not in disabled_events:
        event_name = f"hinamizawa_sonmin_shuukai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "04_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20250628075002/https://mattari-an.net/shu-kai/4th/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="表紙絵提供：伽藍快 様（ENJOY MIX）",
            ),
            Medium(
                "04_Forgery_no_xxx_cover.webp",
                [
                    Source(
                        "https://07th-expansion.fandom.com/wiki/Hinamizawa_Village_Assembly",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            Medium(
                "04_20120101162827_titlelogo.gif",
                [
                    Source(
                        "https://web.archive.org/web/20120101162827/http://shu-kai.hinamizawa.info:80/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            Medium(
                "04_kannai.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20250628074951/https://mattari-an.net/shu-kai/4th/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "https://web.archive.org/web/20250628075002/https://mattari-an.net/shu-kai/4th/kannai.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20250628075002/https://mattari-an.net/shu-kai/4th/kannai.pdf",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1708859, 136.8837218),
                address="4-chōme-4-38 Meieki, Nakamura Ward, Nagoya, Aichi 450-0002, Japan",
                description="ウインクあいち 5F　小ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20110827005110/http://shu-kai.hinamizawa.info/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://streetviewpixels-pa.googleapis.com/v1/thumbnail?output=thumbnail&cb_client=maps_sv.tactile.gps&panoid=plEI7dd2WTUE58egOJKX3g&w=1177&h=1300&yaw=170&pitch=-40",
                url="https://maps.app.goo.gl/6F2N7Dtys66bRMQQ9",
            ),
        ]
        event = Event(
            aliases=[
                "雛見沢村民集会tetra",
                "Hinamizawa Sonmin Shuukai Tetra",
                "雛見沢村民集会4",
                "Hinamizawa Sonmin Shuukai 4",
            ],
            dates="2011.06.19",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date, alias: https://web.archive.org/web/20110827005110/http://shu-kai.hinamizawa.info/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20250628074951/https://mattari-an.net/shu-kai/4th/list.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2018.10.18",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = "petit"  # ==== hinamizawa_sonmin_shuukaipetit ====
    if i not in disabled_events:
        event_name = f"hinamizawa_sonmin_shuukai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "petit_hinamizawaimg.jpg",
                [
                    Source(
                        "https://web.archive.org/web/2/http://www.comic-state.com/html/only/hinamizawa.html",
                        (RT.Reliable, OT.OfficialExt),
                    )
                ],
            ),
            Medium(
                "petit_hinamizawaimg_2.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20150710022055/http://www.comic-state.com/html/only/hinamizawa.html",
                        (RT.Reliable, OT.OfficialExt),
                    )
                ],
            ),
            Medium(
                "petit_35230906_p0_master1200.jpg",
                [
                    Source(
                        "https://www.pixiv.net/en/artworks/35230906",
                        (RT.Likely, OT.OfficialExt),
                    )
                ],
                comments="Perhaps illust for this event.",
            ),
            Medium(
                "petit_link11.png",
                [
                    Source(
                        "https://web.archive.org/web/20150710022055/http://www.comic-state.com/html/only/hinamizawa.html",
                        (RT.Reliable, OT.OfficialExt),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(34.947157, 137.1740327),
                address="5-1 Higashimyodaijicho, Okazaki, Aichi 444-0863, Japan",
                description="愛知県岡崎市竜美丘会館 大ホール+野外",
                sources=[
                    Source(
                        "https://web.archive.org/web/20130810044121/http://shu-kai.hinamizawa.info/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/ANWiy9Q-C-MLl5Pvn1OPQrSITCt8tYTjwbTiLporDLwXRA4tSf-afo18EnwwzucTyTIfyBiI1kcBy0pnxHL5c5QGILJF4XdRfoJLjsj4L8OMhjnbNZAlCYFE-Zaw1uq4vlwnGSwFqOGR2SLseRP7=s1354-k-no",
                url="https://maps.app.goo.gl/qVUt53kHQHsfzU3y9",
            ),
        ]
        event = Event(
            aliases=["雛見沢村民集会ぷち", "Hinamizawa Sonmin Shuukai Petit"],
            dates="2013.06.23",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20130310170503/http://shu-kai.hinamizawa.info/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Part of (date matches, TALES PARTY4 being a プチオンリー sub-event): https://x.com/comic_state1995/status/342169025234751488?s=20",
                    (RT.Guess, OT.Official),
                ),
                # Source("Participating circles: ", (RT.Reliable, OT.Official)),
            ],
            locations=locations,
            description="Part of the TALES PARTY4 venue, itself part of the コミックステイトin岡崎78 venue.",
            # comments=None,
            last_edited="2018.10.18",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 5  # ==== hinamizawa_sonmin_shuukai5 ====
    if i not in disabled_events:
        event_name = f"hinamizawa_sonmin_shuukai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "kizuna_20140107135344_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20140107135344/http://shu-kai.hinamizawa.info/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="チラシ絵提供：伽藍 快 様（ENJOY MIX）",
            ),
            Medium(
                "kizuna_titlelogo.gif",
                [
                    Source(
                        "https://web.archive.org/web/20250525162704/https://mattari-an.net/shu-kai/5th/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "kizuna_kannai.jpg",
                [
                    Source(
                        "https://web.archive.org/web/2/https://mattari-an.net/shu-kai/5th/kannai.jpg",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1313699, 136.8980176),
                address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
                description="名古屋国際会議場　白鳥ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20250524130545/https://mattari-an.net/shu-kai/5th/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn7Lqm9_Q0NEdha1ASXnQ5vdfjHbPJAbiquEME-dTc0IQlVMwwldl4PgCGmoqwXy7f1H0VzeeQ34Sfh31dwy-yLo6SG1i6J7RxOt2LCAXGM3sea6CVPSdGtLv8BqQvcjQ9wGbdq8g=s0?imgmax=0",
                url="https://maps.app.goo.gl/WvWpsu1s7P6fTsdj9",
            ),
        ]
        event = Event(
            aliases=[
                "雛見沢村民集会・絆",
                "Hinamizawa Sonmin Shuukai Kizuna",
                "雛見沢村民集会5",
                "Hinamizawa Sonmin Shuukai 5",
            ],
            dates="2014.09.21",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20131014080522/http://shu-kai.hinamizawa.info/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20250525162704/https://mattari-an.net/shu-kai/5th/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2018.10.18",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 6  # ==== hinamizawa_sonmin_shuukai6 ====
    if i not in disabled_events:
        event_name = f"hinamizawa_sonmin_shuukai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "06_20210102134216_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20210102134216/https://mattari-an.net/shu-kai/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="チラシ絵 提供：様",
            ),
            Medium(
                "06_20210102134216_titlelogo.png",
                [
                    Source(
                        "https://web.archive.org/web/20210102134216/https://mattari-an.net/shu-kai/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            Medium(
                "06_mapa.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20210707224026/https://mattari-an.net/shu-kai/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.049002, 136.8427695),
                address="Japan, 〒455-0848 Aichi, Nagoya, Minato Ward, Kinjofuto, 2 Chome−２−7",
                description="ポートメッセなごや　第2展示館",
                sources=[
                    Source(
                        "https://web.archive.org/web/20220217140706/https://mattari-an.net/shu-kai/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWltuZIN2ftdO5MYmovI0xw1aUUJZZSKKiAMBtqta_mdBRCA9IDIqkP7O-TZq3j7BbMQ8sbcoMMryoFgX3ihj4158Y9F1LWnqmZTo4Dg71d0HHruH0UBUW-9AoxbUIl7TxAvlqie=s0?imgmax=0",
                url="https://maps.app.goo.gl/GiDmeLj3FgwVfg3p6",
            ),
        ]
        event = Event(
            aliases=["雛見沢村民集会6", "Hinamizawa Sonmin Shuukai 6"],
            dates="2021.06.20 → 2021.07.18",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date + postponed: https://web.archive.org/web/20220217140706/https://mattari-an.net/shu-kai/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20210707224026/https://mattari-an.net/shu-kai/list.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2018.10.22",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 7  # ==== hinamizawa_sonmin_shuukai7 ====
    if i not in disabled_events:
        event_name = f"hinamizawa_sonmin_shuukai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "07_20220315133237_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20220315133237/https://mattari-an.net/shu-kai/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="ビジュアル提供：キリコ様",
            ),
            Medium(
                "07_20220315133237_titlelogo.png",
                [
                    Source(
                        "https://web.archive.org/web/20220315133237/https://mattari-an.net/shu-kai/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "07_20220906024521_titlelogo.png",
                [
                    Source(
                        "https://web.archive.org/web/20220906024521/https://mattari-an.net/shu-kai/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "07_map.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20250628075543/https://mattari-an.net/shu-kai/7th/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "https://web.archive.org/web/20200926012825/http://meikasai.com/circle_map.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20250628075543/https://mattari-an.net/shu-kai/7th/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.049002, 136.8427695),
                address="Japan, 〒455-0848 Aichi, Nagoya, Minato Ward, Kinjofuto, 2 Chome−２−7",
                description="ポートメッセなごや　第2展示館",
                sources=[
                    Source(
                        "https://web.archive.org/web/20250628075604/https://mattari-an.net/shu-kai/7th/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWltuZIN2ftdO5MYmovI0xw1aUUJZZSKKiAMBtqta_mdBRCA9IDIqkP7O-TZq3j7BbMQ8sbcoMMryoFgX3ihj4158Y9F1LWnqmZTo4Dg71d0HHruH0UBUW-9AoxbUIl7TxAvlqie=s0?imgmax=0",
                url="https://maps.app.goo.gl/GiDmeLj3FgwVfg3p6",
            ),
        ]
        event = Event(
            aliases=[
                "雛見沢村民集会7..",
                "Hinamizawa Sonmin Shuukai 7..",
                "雛見沢村民集会7",
                "Hinamizawa Sonmin Shuukai 7",
            ],
            dates="2022.06.05",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20250628075604/https://mattari-an.net/shu-kai/7th/",
                    (RT.Reliable, OT.Official),
                ),
                Source("Alias with dots: title in cover.", (RT.Reliable, OT.Official)),
                Source(
                    "Participating circles: https://web.archive.org/web/20250628075543/https://mattari-an.net/shu-kai/7th/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2018.10.25",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = "07th"  # ==== hinamizawa_sonmin_shuukai 07th ====
    if i not in disabled_events:
        event_name = f"hinamizawa_sonmin_shuukai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "7th_20221014131910_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20221014131910/http://mattari-an.net/shu-kai/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="ビジュアル提供：鈴羅木かりん様",
            ),
            Medium(
                "7th_Gousotsu_another_end_cover.webp",
                [
                    Source(
                        "https://07th-expansion.fandom.com/wiki/Hinamizawa_Village_Assembly",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "7th_20220906024521_titlelogo.png",
                [
                    Source(
                        "https://web.archive.org/web/20220315133237/https://mattari-an.net/shu-kai/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "7th_Fe4eeiEUAAIi6qJ.jpg",
                [
                    Source(
                        "https://x.com/Villagerrally/status/1580234369783824385",
                        (RT.Reliable, OT.OfficialExt),
                    )
                ],
            ),
            Medium(
                "7th_map.png",
                [
                    Source(
                        "https://web.archive.org/web/20220906024521/https://mattari-an.net/shu-kai/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "https://web.archive.org/web/20221014131850/https://mattari-an.net/shu-kai/circleguid.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20221014131850/https://mattari-an.net/shu-kai/circleguid.pdf",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.6889181, 139.7862194),
                address="Japan, 〒103-0007 Tokyo, Chuo City, Nihonbashihamacho, 1 Chome−1−12 2F",
                description="東京都　プラザマーム2F",
                sources=[
                    Source(
                        "https://web.archive.org/web/20221014131910/http://mattari-an.net/shu-kai/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/grass-cs/AABkmLeuhaVw_v7kcc7dtj53ID_ZE1mkvipaUUbQe5CUVj1L2SU3xAJGBrorglhwLsNL3zzvqLAKHJH7_zMEup8vxfo_KeOrm3WVkvT_q4j-julLLiFQF9RnpMBAcTg90AbVhchO5YQ=s0?imgmax=0",
                url="https://maps.app.goo.gl/EbJHgTeBwqXRBWe9A",
            ),
        ]
        event = Event(
            aliases=["07th村民集会", "07th Sonmin Shuukai"],
            dates="2022.10.15",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date, alias: https://web.archive.org/web/20221014131910/http://mattari-an.net/shu-kai/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20220906024521/https://mattari-an.net/shu-kai/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="20th anniversary of 7th Expansion, linked here: https://web.archive.org/web/20221008021911/https://07th-expansion.net/event/07thdaienkai/\nMisc: https://07thpublicbath.web.fc2.com/\nMisc: https://07th-expansion.net/event/07thdaienkai/",
            # comments=None,
            last_edited="2018.10.25",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 8  # ==== hinamizawa_sonmin_shuukai8 ====
    if i not in disabled_events:
        event_name = f"hinamizawa_sonmin_shuukai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "08_20230529001620_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20230529001620/https://mattari-an.net/shu-kai/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="ビジュアル提供：キリコ様",
            ),
            Medium(
                "08_20230529001620_titlelogo.png",
                [
                    Source(
                        "https://web.archive.org/web/20230529001620/https://mattari-an.net/shu-kai/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "08_FzYerKSacAUd41N.jpg",
                [
                    Source(
                        "https://x.com/Villagerrally/status/1672558042146287616",
                        (RT.Reliable, OT.OfficialExt),
                    )
                ],
            ),
            Medium(
                "08_map.png",
                [
                    Source(
                        "https://web.archive.org/web/20250522214648/https://mattari-an.net/shu-kai/8th/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.049002, 136.8427695),
                address="Japan, 〒455-0848 Aichi, Nagoya, Minato Ward, Kinjofuto, 2 Chome−２−7",
                description="ポートメッセなごや　第2展示館",
                sources=[
                    Source(
                        "https://web.archive.org/web/20250522142636/https://mattari-an.net/shu-kai/8th/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWltuZIN2ftdO5MYmovI0xw1aUUJZZSKKiAMBtqta_mdBRCA9IDIqkP7O-TZq3j7BbMQ8sbcoMMryoFgX3ihj4158Y9F1LWnqmZTo4Dg71d0HHruH0UBUW-9AoxbUIl7TxAvlqie=s0?imgmax=0",
                url="https://maps.app.goo.gl/GiDmeLj3FgwVfg3p6",
            ),
        ]
        event = Event(
            aliases=[
                "雛見沢村民集会Ⅷ",
                "雛見沢村民集会8",
                "Hinamizawa Village Assembly 8",
            ],
            dates="2023.06.25",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date, Alias: https://web.archive.org/web/20250522142636/https://mattari-an.net/shu-kai/8th/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20250522215723/https://mattari-an.net/shu-kai/8th/cutlist/cutlist.html",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles (alt): https://web.archive.org/web/20250522214648/https://mattari-an.net/shu-kai/8th/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2018.10.25",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = "Q"  # ==== hinamizawa_sonmin_shuukaiQ ====
    if i not in disabled_events:
        event_name = f"hinamizawa_sonmin_shuukai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "Q_20240603232058_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20240603232058/https://mattari-an.net/shu-kai/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="ビジュアル提供：キリコ様",
            ),
            Medium(
                "Q_20240603232058_titlelogo.png",
                [
                    Source(
                        "https://web.archive.org/web/20240603232058/https://mattari-an.net/shu-kai/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            Medium(
                "Q_map.png",
                [
                    Source(
                        "https://web.archive.org/web/20250522200511/https://mattari-an.net/shu-kai/9th/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.6889181, 139.7862194),
                address="Japan, 〒103-0007 Tokyo, Chuo City, Nihonbashihamacho, 1 Chome−1−12 2F",
                description="東京都　プラザマーム2F",
                sources=[
                    Source(
                        "https://web.archive.org/web/20250522175236/https://mattari-an.net/shu-kai/9th/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/grass-cs/AABkmLeuhaVw_v7kcc7dtj53ID_ZE1mkvipaUUbQe5CUVj1L2SU3xAJGBrorglhwLsNL3zzvqLAKHJH7_zMEup8vxfo_KeOrm3WVkvT_q4j-julLLiFQF9RnpMBAcTg90AbVhchO5YQ=s0?imgmax=0",
                url="https://maps.app.goo.gl/EbJHgTeBwqXRBWe9A",
            ),
        ]
        event = Event(
            aliases=[
                "雛見沢村民集会Q",
                "Hinamizawa Sonmin Shuukai Q",
                "雛見沢村民集会9",
                "Hinamizawa Sonmin Shuukai 9",
            ],
            dates="2024.06.09",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date, Alias: https://web.archive.org/web/20250522175236/https://mattari-an.net/shu-kai/9th/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Is also 9th (which makes sense from the spelling): from url of https://mattari-an.net/shu-kai/9th/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20250524102203/https://mattari-an.net/shu-kai/9th/cutlist/cutlist.html",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles (alt): https://web.archive.org/web/20250522200511/https://mattari-an.net/shu-kai/9th/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            comments="Referenced: https://web.archive.org/web/20240523105015/http://pastaparty.starfree.jp/sonmin-q/event.html",
            last_edited="2018.10.25",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = "shirakawa"  # ==== hinamizawa_sonmin_shuukaishirakawa ====
    if i not in disabled_events:
        event_name = f"hinamizawa_sonmin_shuukai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "shirakawa_20250521174133_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20250521174133/https://mattari-an.net/shu-kai/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="ビジュアル提供：結城きもの様",
            ),
            Medium(
                "shirakawa_20250521174133_titlelogo.png",
                [
                    Source(
                        "https://web.archive.org/web/20250521174133/https://mattari-an.net/shu-kai/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            Medium(
                "shirakawa_Gq_F_OXaoAEXDOA.jpg",
                [
                    Source(
                        "https://x.com/kimono228/status/1922973295235764490",
                        (RT.Reliable, OT.OfficialExt),
                    )
                ],
            ),
            Medium(
                "shirakawa_map.png",
                [
                    Source(
                        "https://web.archive.org/web/20260214223311/https://mattari-an.net/shu-kai/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "shirakawa_Hinamizawa_Doujinshi_Convention_cover.webp",
                [
                    Source(
                        "https://07th-expansion.fandom.com/wiki/Hinamizawa_Village_Assembly",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "shirakawa_1500x500.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20250628093254/https://pbs.twimg.com/profile_banners/1337735537046646787/1750460093/1500x500",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(36.2581721, 136.904264),
                address="796-1 Ogimachi, Shirakawa, Ono District, Gifu 501-5627, Japan",
                description="白川郷　荻町公民館",
                sources=[
                    Source(
                        "https://web.archive.org/web/20250521174133/https://mattari-an.net/shu-kai/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/grass-cs/AABkmLfj-JFP6v1IOJqAa7rLiQoJjBApx--juoFyewYbZ-HeJ5MV4bt3d0rpQvGz29ofCiQICE0qgWT7pm5FxGfxirohf0oshyIPYEV8wqcpYuCfZhYFBSA5SkY_r-Duf2jksPFP8QJ8=s0?imgmax=0",
                url="https://maps.app.goo.gl/vfu6ukHkYpXQ36Ck7",
            ),
        ]
        event = Event(
            aliases=[
                "雛見沢村民集会in白川郷",
                "Hinamizawa Village Assembly in Shirakawa-gou",
            ],
            dates="2025.06.22",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20250521174133/https://mattari-an.net/shu-kai/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20261025141548/https://mattari-an.net/shu-kai/cutlist/cutlist.html",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles (alt): https://web.archive.org/web/20260214223311/https://mattari-an.net/shu-kai/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2018.10.25",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    # i =   # ==== hinamizawa_sonmin_shuukai ====
    # if i not in disabled_events:
    #     event_name = f"hinamizawa_sonmin_shuukai{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=["雛見沢村民集会", "Hinamizawa Sonmin Shuukai "],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source("Date: ", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         last_edited="2018.10.25",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # ==== event group ====
    media = [
        Medium(
            "eg_20130325094641_titlelogo.gif",
            [
                Source(
                    "https://web.archive.org/web/20130325094641/http://shu-kai.hinamizawa.info:80/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                )
            ],
        )
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
    ]
    links = [
        "https://shu-kai.hinamizawa.info/",
        "https://mattari-an.net/shu-kai/",
        "https://x.com/Villagerrally",
    ]

    event_group = EventGroup(
        aliases=[
            "雛見沢村民集会",
            "Hinamizawa Sonmin Shuukai",
            "Hinamizawa Village Assembly",
        ],
        events=events,
        media=media,
        links=links,
        sources=[
            Source(
                'Alias "Hinamizawa Village Assembly" (non-official): https://07th-expansion.fandom.com/wiki/Hinamizawa_Village_Assembly',
                (ReliabilityTypes.Doubtful, OriginTypes.External),
            ),
        ],
        comments=None,
        description=None,
        last_edited="2026.10.25",
    )

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")

    # TODO: they are planning a new event in 2026 or 2027! https://x.com/Villagerrally/status/2102031344239054862
