"""
_____________________________________
                                     |
ALL SONGS IS SUBJECTED TO COPYRIGHT  |
COPYRIGHTS MUST INCLUDED HERE!       |
_____________________________________|

FIX FORMATS OF*
- I HEARD THE VOICE OF JESUS SAY

BUGS*
- TEXT SIZE (MUST AUTO RESIZE, REFERENCE TO SCREEN)
- USER CAN ACCESS SECOND SCREEN (WHICH SHOULD NOT)

FEATURES TO ADD*
- MUCH STRONGER SEARCH ENGINE (EX: KEYWORD: "AND" FILTER EVERY SONG TITLE WITH "AND" WILL APPEAR)
- BIG FONT FOR TITLE ONLY
- SCHEDULER
- ADD, EDIT, DELETE (DATABASE NEEDED)

NOTES*
- DOUBLE CHECK TYPO 
- CHECK THE LYRICS FORMAT
- SEARCH ABOUT HOW TO MAKE THE .EXE FILE MUCH SMALLER FILE SIZE
- MAKE THGE FONT OF LIVE SCREEN IN PRIMARY SMALLER
- ADD WINDOW TITLE AND ICON TO SECOND WINDOW

THE LILY OF THE VALLEY 
TIS SO SWEET TO TRUST IN JESUS
"""
from primary_screen import *
from second_screen import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QAction, QFrame, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QSpacerItem, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
import re
import sys
import os


class Ui_MainWindow(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        finish = QAction('Quit', self)
        finish.triggered.connect(self.closeEvent)

        self.lyrics_listwidget.setDragEnabled(False)

        # live button
        self.live_btn.clicked.connect(self.go_live)
        self.islive = False

        # clear button
        self.clear_btn.clicked.connect(self.clear_live_screen)
        self.isclear = False

        # set-up second window
        self.app = QApplication(sys.argv)
        self.second_window = Ui_UI_second()

        # lyrics selected in lyrics_listwidget
        self.lyrics = None

        # init some empty list
        self.list_of_all_songs = []
        self.filtered_song_list = []

        # getting song_listwiget items and assigning it to empty list
        for row in range(self.song_listwidget.count()):
            items = self.song_listwidget.item(row).text()
            items = items.upper()
            self.list_of_all_songs.append(items)
            self.filtered_song_list.append(items)

        # re-input songs in song_listwidget
        self.song_listwidget.clear()
        for i in range(len(self.list_of_all_songs)):
            self.song_listwidget.addItem(self.list_of_all_songs[i])

        self.search_engine.textChanged.connect(self.filter_search)
        self.song_listwidget.itemActivated.connect(self.what_song_selected)

        #  display lyrics ing primary live screen
        self.lyrics_listwidget.itemPressed.connect(self.go_in_live_screen)

        # list of songs
        self.song_0 = ["Title",
                       "A NEW NAME IN GLORY\nPage 161",
                       "Chorus",
                       "THERE'S A NEW NAME\n"
                       "WRITTEN DOWN IN GLORY,\n"
                       "AND ITS MINE, O YES ITS MINE\n"
                       "AND THE WHITE-ROBED\n"
                       "ANGELS SING THE STORY,\n"
                       "A SINNER HAS COME HOME.\n",
                       "FOR THERE'S A NEW NAME\n"
                       "WRITTEN DOWN IN GLORY,\n"
                       "AND IT'S MINE, O YES ITS MINE\n"
                       "WITH MY SINS FORGIVEN\n"
                       "I AM BOUND FOR HEAVEN,\n"
                       "NEVER MORE TO ROAM.",
                       "Stanza-1",
                       "I WAS ONCE A SINNER,\n"
                       "BUT I CAME PARDON TO RECEIVE\n"
                       "FROM MY LORD:\n"
                       "THIS WAS FREELY GIVEN,\n"
                       "AND I SAW THAT MY NAME\n"
                       "WAS WRITTEN DOWN",
                       "Stanza-2",
                       "I WAS HUMBLY KNEELING\n"
                       "AT THE CROSS,\n"
                       "FEARING NAUGHT BUT\n"
                       "GOD'S ANGRY FROWN;\n"
                       "WHEN THE HEAVENS OPENED\n"
                       "AND I SAW THAT MY NAME\n"
                       "WAS WRITTEN DOWN",
                       "Stanza-3",
                       "IN THE BOOK TIS' WRITTEN\n"
                       "SAVED BY GRACE,\n"
                       "O THE JOY THAT CAME\n"
                       "TO MY SOUL!\n"
                       "NOW I AM FORGIVEN,\n"
                       "AND I KNOW BY THE BLOOD\n"
                       "I AM MADE WHOLE"]
        self.song_1 = ["Title",
                       "A PASSION FOR SOULS\nPage 252",
                       "Chorus",
                       "JESUS, I LONG,\n"
                       "I LONG TO BE WINNING\n"
                       "MEN WHO ARE LOST,\n"
                       "AND CONSTANTLY SIN-NING;\n"
                       "O MAY THIS HOUR\n"
                       "BE ONE OF BEGINNING\n"
                       "THE STORY OF PARDON TO TELL.",
                       "Stanza-1",
                       "GIVE ME A PASSION FOR SOULS,\n"
                       "DEAR LORD,\n"
                       "A PASSION TO SAVE THE LOST;\n"
                       "O THAT THY LOVE\n"
                       "WERE BY ALL ADORED,\n"
                       "AND WELCOME AT ANY COST.",
                       "Stanza-2",
                       "THOUGH THERE ARE\n"
                       "DANGERS UNTOLD AND STERN\n"
                       "CONFRONTING ME IN THE WAY\n"
                       "WILLINGLY STILL WOULD I GO,\n"
                       "NOR TURN, BUT TRUST THEN\n"
                       "FOR GRACE EACH DAY.",
                       "Stanza-3",
                       "HOW SHALL THIS PASSION\n"
                       "FOR SOULS BE MINE?\n"
                       "LORD, MAKE THE ANSWER CLEAR;\n"
                       "HELP ME TO THROW OUT\n"
                       "THE OLD LIFE-LINE\n"
                       "TO THOSE WHO ARE\n"
                       "STRUGGLING NEAR."]
        self.song_2 = ["Title",
                       "A SHELTER IN THE TIME OF STORM\nPage 34",
                       "Chorus",
                       "OH, JESUS IS A ROCK\n"
                       "IN A WEARY LAND, A WEARY LAND,\n"
                       "A WEARY LAND;\n"
                       "OH JESUS IN A ROCK\n"
                       "IN A WEARY LAND, A SHELTER\n"
                       "IN THE TIME OF STORM",
                       "Stanza-1",
                       "THE LORD’S OUR ROCK\n"
                       "IN HIM WE HIDE,\n"
                       "A SHELTER IN THE\n"
                       "TIME OF STORM;\n"
                       "SECURE WHAT EVER\n"
                       "ILL BETIDE, A SHELTER\n"
                       "IN THE TIME OF STORM.",
                       "Stanza-2",
                       "A SHADE BY DAY\n"
                       "DEFENSE BY NIGHT,\n"
                       "A SHELTER IN THE\n"
                       "TIME OF STORM;\n"
                       "NO FEARS ALARM, NO\n"
                       "FOES AFFRIGHT, A SHELTER\n"
                       "IN THE TIME OF STORM.",
                       "Stanza-3",
                       "THE RAGING STORMS\n"
                       "MAY ROUND US BEAT,\n"
                       "A SHELTER IN THE\n"
                       "TIME OF STORM;\n"
                       "WE'LL NEVER LEAVE OUR\n"
                       "SAFE RETREAT, A SHELTER\n"
                       "IN THE TIME OF STORM.",
                       "Stanza-4",
                       "O ROCK DIVINE\n"
                       "O REFUGE DEAR,\n"
                       "A SHELTER IN THE\n"
                       "TIME OF STORM;\n"
                       "BE THOU OUR HELPER\n"
                       "EVER NEAR, A SHELTER\n"
                       "IN THE TIME OF STORM."]
        self.song_3 = ["Title",
                       "ALL HAIL THE POWER\nPage 1",
                       "Stanza-1",
                       "ALL HAIL THE POWER OF JESUS NAME\nLET ANGELS PROSTRATE FALL\n"
                       "BRING FORT THE ROYAL DIADEM\nAND CROWN HIM LORD OF ALL\nBRING "
                       "FORT THE ROYAL DIADEM\nAND CROWN HIM LORD OF ALL",
                       "Stanza-2",
                       "YE CHOSEN SEED OF ISRAEL'S RACE\nYE RANSOMED FROM THE FALL\n"
                       "HAIL HIM WHO SAVES YOU BY HIS GRACE\nAND CROWN HIM LORD OF ALL\n"
                       "HAIL HIM WHO SAVES YOU BY HIS GRACE\nAND CROWN HIM LORD OF ALL",
                       "Stanza-3",
                       "LET EVERY KINDRED EVERY TRIBE\nON THIS TERRESTRIAL BALL\n"
                       "TO HIM ALL MAJESTY ASCRIBE\nAND CROWN HIM LORD OF ALL\n"
                       "TO HIM ALL MAJESTY ASCRIBE\nAND CROWN HIM LORD OF ALL",
                       "Stanza-4",
                       "O THAT WITH YONDER SACRED THRONG\nWE AT HIS FEET MAY FALL\n"
                       "WE'LL JOIN THE EVERLASTING SONG\nAND CROWN HIM LORD OF ALL\n"
                       "WE'LL JOIN THE EVERLASTING SONG\nAND CROWN HIM LORD OF ALL"]
        self.song_4 = ["Title",
                       "AM I A SOLDIER OF THE CROSS\nPage 230",
                       "Stanza-1",
                       "AM I A SOLDIER OF THE CROSS,\n"
                       "A FOLLOWER OF THE LAMB?\n"
                       "AND SHALL I FEAR TO OWN HIS CAUSE,\n"
                       "OR BLUSH TO SPEAK HIS NAME?",
                       "Stanza-2",
                       "MUST I BE CARRIED TO THE SKIES\n"
                       "ON FLOWRY BEDS OF EASE,\n"
                       "WHILE OTHERS FOUGHT TO WIN THE PRIZE,\n"
                       "AND SAILED THRO' BLOODY SEAS?",
                       "Stanza-3",
                       "ARE THERE NO FOES FOR ME TO FACE?\n"
                       "MUST I NOT STEM THE FLOOD?\n"
                       "IS THUS VILE WORLD A FRIEND TO GRACE,\n"
                       "TO HELP ME ON TO GOD?",
                       "Stanza-4",
                       "SURE I MUST FIGHT, I WOULD REIGN;\n"
                       "INCREASE MY COURAGE, LORD\n"
                       "I'LL BEAR THE TOIL, ENDURE THE PAIN,\n"
                       "SUPPORTED BY THY WORD."]
        self.song_5 = ["Title",
                       "AMAZING GRACE\nPage 86",
                       "Stanza-1",
                       "AMAZING GRACE!\nHOW SWEET THE SOUND,\n"
                       "THAT SAVED A WRETCH LIKE ME!\n"
                       "I ONCE WAS LOST, BUT NOW AM FOUND,\n"
                       "WAS BLIND, BUT NOW I SEE.",
                       "Stanza-2",
                       "'TWAS GRACE THAT TAUGHT\nMY HEART TO FEAR\n"
                       "AND GRACE MY FEARS RELIEVED;\n"
                       "HOW PRECIOUS DID THAT GRACE, APPEAR\n"
                       "THE HOUR I FIRST BELIEVED!",
                       "Stanza-3",
                       "THRO' MANY DANGERS,\nTOILS AND SNARES,\n"
                       "I HAVE ALREADY COME;\n"
                       "'TIS GRACE HATH BRO'T ME SAFE THUS FAR,\n"
                       "AND GRACE WILL LEAD ME HOME.",
                       "Stanza-4",
                       "WHEN WE'VE BEEN THERE\nTEN THOUSAND YEARS,\n"
                       "BRIGHT SHINNING AS THE SUN,\n"
                       "WE'VE NO LESS DAYS TO SING GOD'S PRAISE\n"
                       "THAN WHEN WE FIRST BEGUN."]
        self.song_6 = ["Title",
                       "ARE YOU WASHED IN THE BLOOD\nPage 126",
                       "Chorus",
                       "ARE YOU WASHED IN THE BLOOD,\n"
                       "IN THE SOUL CLEANSING\nBLOOD OF THE LAMB?\n"
                       "ARE YOUR GARMENTS SPOTLESS?\n"
                       "ARE THEY WHITE AS SNOW?\n"
                       "ARE YOU WASHED IN THE\nBLOOD OF THE LAMB?",
                       "Stanza-1",
                       "HAVE YOU BEEN TO JESUS\n"
                       "FOR THE CLEANSING POWER?\n"
                       "ARE YOU WASHED IN THE\nBLOOD OF THE LAMB?\n"
                       "ARE YOU FULLY TRUSTING\nIN HIS GRACE THIS HOUR?\n"
                       "ARE YOU WASHED IN THE\nBLOOD OF THE LAMB?",
                       "Stanza-2",
                       "ARE YOU WALKING DAILY\nBY THE SAVIOR SIDE?\n"
                       "ARE YOU WASHED IN THE\nBLOOD OF THE LAMB?\n"
                       "DO YOU REST EACH MOMENT\nIN THE CRUCIFIED?\n"
                       "ARE YOU WASHED IN THE\nBLOOD OF THE LAMB?",
                       "Stanza-3",
                       "WHEN THE BRIDEGROOM COMETH\nWILL YOUR ROBES BE WHITE?\n"
                       "ARE YOU WASHED IN THE\nBLOOD OF THE LAMB?\n"
                       "WILL YOUR SOUL BE READY\nFOR THE MANSIONS BRIGHT,\n"
                       "ARE YOU WASHED IN THE\nBLOOD OF THE LAMB?",
                       "Stanza-4",
                       "LAY ASIDE THE GARMENTS\nTHAT ARE STAINED WITH SIN,\n"
                       "AND BE WASHED IN THE\nBLOOD OF THE LAMB;\n"
                       "THERE'S A FOUNTAIN FLOWING\nFOR THE SOUL UNCLEAN,\n"
                       "O BE WASHED IN THE\nBLOOD OF THE LAMB?"]
        self.song_7 = ["Title",
                       "AT CALVARY\nPage 65",
                       "Chorus",
                       "MERCY THERE WAS GREAT,\nAND GRACE WAS FREE;\n"
                       "PARDON THERE WAS\nMULTIPLIED TO ME;\n"
                       "THERE MY BURDENED SOUL\nFOUND LIBERTY, AT CALVARY.",
                       "Stanza-1",
                       "YEARS I SPENT\nIN VANITY AND PRIDE,\n"
                       "CARING NOT MY LORD\nWAS CRUCIFIED.\n"
                       "KNOWING NOT IT WAS\nFOR ME HE DIED\n"
                       "ON CAL-VA-RY!",
                       "Stanza-2",
                       "BY GOD'S WORD AT LAST\nMY SIN I LEARNED;\n"
                       "THEN I TREMBLED AT THE\nLAW I'D SPURNED,\n"
                       "TILL MY GUILTY SOUL\nIMPLORING TURNED\n"
                       "TO CAL-VA-RY!",
                       "Stanza-3",
                       "NOW I'VE GIV'N\nTO JESUS EVERYTHING,\n"
                       "NOW I GLADLY OWN\nHIM AS MY KING,\n"
                       "NOW MY RAPTURED SOUL\nCAN ONLY SING\n"
                       "OF CAL-VA-RY!",
                       "Stanza-4",
                       "OH, THE LOVE THAT DREW\nSALVATION'S PLAN!\n"
                       "OH, THE GRACE THAT BRO'T IT\nDOWN TO MAN!\n"
                       "OH THE MIGHTY GULF\nTHAT GOD DID SPAN\n"
                       "AT CAL-VA-RY!"]
        self.song_8 = ["Title",
                       "AT THE CROSS\nPage 77",
                       "Chorus",
                       "AT THE CROSS, AT THE CROSS\n"
                       "WHERE I FIRST SO THE LIGHT,\n"
                       "AND THE BURDENED OF MY HEART\n"
                       "ROLLED AWAY (ROLLED AWAY),\n"
                       "IT WAS THERE BY FAITH\n"
                       "I RECEIVE MY SIGHT,\n"
                       "AND NOW I AM HAPPY ALL THE DAY!",
                       "Stanza-1",
                       "ALAS AND DID MY SAVIOR BLEED?\n"
                       "AND DID MY SOVEREIGN DIE?\n"
                       "WOULD HE DEVOTE THAT SACRED HEAD\n"
                       "FOR SUCH A WORN AS I?",
                       "Stanza-2",
                       "WAS IT FOR CRIMES THAT I HAVE DONE,\n"
                       "HE GROANED UPON THE TREE?\n"
                       "AMAZING PITY! GRACE UNKNOWN!\n"
                       "AND LOVE BEYOND DEGREE!",
                       "Stanza-3",
                       "WELL MIGHT THE SUN IN DARKNESS HIDE,\n"
                       "AND SHUT HIS GLORIES IN,\n"
                       "WHEN CHRIST THE MIGHTY MAKER DIED\n"
                       "FOR MAN THE CREATURE'S SIN.",
                       "Stanza-4",
                       "BUT DROPS OF GRIEF CAN NE'ER REPAY\n"
                       "THE DEBT OF LOVE I OWE;\n"
                       "HERE, LORD I GIVE MYSELF AWAY,\n"
                       "'TIS ALL THAT I CAN DO!"]
        self.song_9 = ["Title",
                       "BEAULAH LAND\nPage 75",
                       "Chorus",
                       "O BEAULAH LAND, SWEET BEAULAH LAND,\n"
                       "AS ON THY HIGHEST MOUNT I STAND.\n"
                       "I LOOK AWAY ACROSS THE SEA\n"
                       "WHERE MANSIONS ARE PREPARED FOR ME,\n"
                       "AND VIEW THE SHINNING GLORY SHORE,\n"
                       "MY HEAVEN, MY HOME FOREVERMORE.",
                       "Stanza-1",
                       "I'VE REACHED THE LAND OF JOY DIVINE,\n"
                       "AND ALL ITS BEAUTY NOW IS MINE;\n"
                       "HERE SHINES UNDIMMED ONE BLISSFUL DAY,\n"
                       "FOR ALL MY NIGHT HAS PASSED AWAY.",
                       "Stanza-2",
                       "THE SAVIOUR COMES AND WALKS IN ME,\n"
                       "AND SWEET COMMUNION HERE HAVE WE;\n"
                       "HE GENTLY LEADS ME WITH HIS HAND,\n"
                       "FOR THIS IS HEAVEN'S BORDER LAND.",
                       "Stanza-3",
                       "A SWEET PERFUME UPON THE BREEZE\n"
                       "IS BORNE FROM EVER VERNAL TREES,\n"
                       "AND FLOWERS THAT NEVER FADING GROW\n"
                       "WHERE STREAMS OF LIFE FOREVER FLOW.",
                       "Stanza-4",
                       "THE ZEPHYRS SEEM TO FLOAT TO ME,\n"
                       "SWEET SOUNDS OF HEAVEN'S MELODY,\n"
                       "AS ANGELS, WITH THE WHITE-ROBED\nTHRONG, "
                       "JOIN IN THE SWEET\nREDEMPTION SONG."]
        self.song_10 = ["Title",
                        "BLESSED ASSURANCE\nPage 114",
                        "Chorus",
                        "THIS IS MY STORY,\nTHIS IS MY SONG,\n"
                        "PRAISING MY SAVIOR\nALL THE DAY LONG; (2X)",
                        "Stanza-1",
                        "BLESSED ASSURANCE\nJESUS IS MINE!\n"
                        "O WHAT A FORETAST\nOF GLORY DIVINE!\n"
                        "HEIR OF SALVATION,\nPURCHASE OF GOD,\n"
                        "BORN OF HIS SPIRIT\nWASHED IN HIS BLOOD.",
                        "Stanza-2",
                        "PERFECT SUBMISSION,\nPERFECT DELIGHT,\n"
                        "VISIONS OF RAPTURE\nNOW BURST ON MY SIGHT,\n"
                        "ANGELS, DECENDING,\nBRING FROM ABOVE,\n"
                        "ECHOES OF MERCY,\nWHISPERS OF LOVE.",
                        "Stanza-3",
                        "PERFECT SUBMISSION,\nALL IS AT REST\n"
                        "I IN MY SAVIOR\nAM HAPPY AND BLEST,\n"
                        "WATCHING AND WAITING,\nLOOKING ABOVE,\n"
                        "FILLED WITH HIS GOODNESS,\nLOST IN HIS LOVE."]
        self.song_11 = ["Title",
                        "BLESSED BE THE NAME\nPage 250",
                        "Chorus",
                        "BLESSED BE THE NAME,\nBLESSED BE THE NAME,\n"
                        "BLESSED BE THE NAME\nOF THE LORD; (2X)",
                        "Stanza-1",
                        "ALL PRAISE TO HIM WHO REIGNS ABOVE\n"
                        "IN MAJESTY SUPREME,\n"
                        "WHO GAVE HIS SON FOR MAN TO DIE,\n"
                        "THAT HE MIGHT MAN REDEEM!",
                        "Stanza-2",
                        "HIS NAME ABOVE\nALL NAMES SHALL STAND,\n"
                        "EXALTED MORE AND MORE,\n"
                        "AT GOD THE FATHER'S\nOWN RIGHT HAND,\n"
                        "WHERE ANGEL HOST ADORE.",
                        "Stanza-3",
                        "REDEEMER, SAVIOR, FRIEND OF MAN\n"
                        "ONCE RUINED BY THE FALL,\n"
                        "THOU HAST DEVISED SALVATION'S PLAN\n"
                        "FOR THOU HAST DIED FOR ALL",
                        "Stanza-4",
                        "HIS NAME SHALL BE THE COUNSELOR,\n"
                        "THE MIGHTY PRINCE OF PEACE,\n"
                        "OF ALL EARTH'S KINGDOM CONQUER,\n"
                        "WHOSE REIGHN SHALL NEVER CEASE."]
        self.song_12 = ["Title",
                        "BRING THE IN\nPage 199",
                        "Chorus",
                        "BRING THEM IN, BRING THEM IN,\n"
                        "BRING THEM IN FROM THE FIELDS OF SIN;\n"
                        "BRING THEM IN, BRING THEM IN,\n"
                        "BRING THE WANDRING ONES TO JESUS.",
                        "Stanza-1",
                        "HARK! TIS THE SHEPHERD'S VOICE I HEAR,\n"
                        "OUT IN THE DESERT DARK AND DREAR,\n"
                        "CALLING THE SHEEP WHO'VE GONE ASTRAY\n"
                        "FAR FROM THE SHEPHERD'S FOLD AWAY",
                        "Stanza-2",
                        "WHO'LL GO AND HELP THIS SHEPHERD KIND,\n"
                        "HELP HIM THE WANDRING ONES TO FIND?\n"
                        "WHO'LL BRING THE LOST ONES TO THE FOLD,\n"
                        "WHERE THEY'LL FIND BE SHELTERED\nFROM THE COLD?",
                        "Stanza-3",
                        "OUT IN THE DESERT HEAR THEIR CRY,\n"
                        "OUT ON THE MOUNTAINS WILD AND HIGH;\n"
                        "HARK! TIS THE MASTER SPEAKS TO THEE,\n"
                        "GO FIND MY SHEEP WHERE 'ER THEY BE."]
        self.song_13 = ["Title",
                        "BRINGING IN THE SHEAVES\nPage 6",
                        "Chorus",
                        "BRINGING IN THE SHEAVES,\n"
                        "BRINGING IN THE SHEAVES;\n"
                        "WE SHALL COME REJOICING\n"
                        "BRINGING IN THE SHEAVES. (2X)",
                        "Stanza-1",
                        "SOWING IN THE MORNING,\n"
                        "SOWING SEEDS OF KINDNESS,\n"
                        "SOWING IN THE NOON-TIDE\n"
                        "AND THE DEWY EVE;\n"
                        "WAITING FOR THE HARVEST\n"
                        "AND THE TIME OF REAPING,\n"
                        "WE SHALL COME REJOICING\n"
                        "BRINGING IN THE SHEAVES.",
                        "Stanza-2",
                        "SOWING IN THE SUNSHINE,\n"
                        "SOWING IN THE SHADOWS,\n"
                        "FEARING NEITHER CLOUDS\n"
                        "NOR WINTER CHILLING BREEZE;\n"
                        "BY AND BY THE HARVEST\n"
                        "AND THE LABOR ENDED\n"
                        "WE SHALL COME REJOICING\n"
                        "BRINGING IN THE SHEAVES",
                        "Stanza-3",
                        "GOING FORTH WITH WEEPING,\n"
                        "SOWING FOR THE MASTER,\n"
                        "THO' THE LOSS SUSTAINED\n"
                        "OUR SPIRIT OFTEN GRIEVES;\n"
                        "WHEN OUR WEEPING'S OVER,\n"
                        "HE WILL BID US WELCOME,\n"
                        "WE SHALL COME REJOICING\n"
                        "BRINGING IN THE SHEAVES."]
        self.song_14 = ["Title",
                        "CALVARY COVERS IT ALL\nPage 274",
                        "Chorus",
                        "CALVARY COVERS IT ALL,\n"
                        "MY PAST WITH ITS SIN AND STAIN;\n"
                        "MY GUILT AND DESPAIR\n"
                        "JESUS TOOK IN HIM THERE,\n"
                        "AND CALVARY COVERS IT ALL.",
                        "Stanza-1",
                        "FAR DEARER THAN ALL THAT\n"
                        "THE WORLD CAN IMPART,\n"
                        "WAS THE MESSAGE THAT CAME\n"
                        "TO MY HEARTS (TO MY HEART);\n"
                        "HOW THAT JESUS ALONE\n"
                        "FOR MY SIN DID ATONE,\n"
                        "AND CALVARY COVERS IT ALL.",
                        "Stanza-2",
                        "THE STRIPES THAT HE BORE\n"
                        "AND THE THORNS THAT HE WORE\n"
                        "TOLD HIS MERCY AND LOVE\n"
                        "EVERMORE (EVERMORE);\n"
                        "AND MY HEART BOWED IN SHAME\n"
                        "AS I CALLED HIS NAME,\n"
                        "AND CALVARY COVERS IT ALL.",
                        "Stanza-3",
                        "HOW MATCHLESS THE GRACE,\n"
                        "WHEN I LOOKED IN THE FACE\n"
                        "OF THIS JESUS, MY CRUCIFIED\n"
                        "LORD (OF MY LORD);\n"
                        "MY REDEMPTION COMPLETE\n"
                        "I THEN FOUND AT HIS FEET,\n"
                        "AND CALVARY COVERS IT ALL.",
                        "Stanza-4",
                        "HOW BLESSED THE THOUGHT,\n"
                        "THAT MY SOUL BY HIM BOUGHT,\n"
                        "SHALL BE HIS IN THE\n"
                        "GLORY ON HIGH (HIS ON HIGH);\n"
                        "WHERE WITH GLADNESS AND SONG\n"
                        "I'LL BE ONE OF THE THRONG,\n"
                        "AND CALVARY COVERS IT ALL."]
        self.song_15 = ["Title",
                        "CHRIST AROSE\nPage 35",
                        "Chorus",
                        "UP FROM THE GRAVE\nHE AROSE (HE AROSE)\n"
                        "WITH A MIGHTY TRIUMPH\nO'ER HIS FOES;\n"
                        "HE AROSE A VICTOR\nFROM THE DARK DOMAIN,\n"
                        "AND HE LIVES FOREVER\nWITH HIS SAINTS TO REIGN.\n"
                        "HE AROSE! HE AROSE!\nHALLELUJAH! CHRIST AROSE!",
                        "Stanza-1",
                        "LOW IN THE GRAVE HE LAY\n"
                        "JESUS MY SAVIOUR!\n"
                        "WAITING THE COMING DAY\n"
                        "JESUS MY LORD!",
                        "Stanza-2",
                        "VAINLY THEY WATCH HIS BED\n"
                        "JESUS MY SAVIOUR!\n"
                        "VAINLY THEY SEAL THE DEAD\n"
                        "JESUS MY LORD!",
                        "Stanza-3",
                        "DEATH CANNOT KEEP HIS PREY\n"
                        "JESUS MY SAVIOUR!\n"
                        "HE TORE THE BARS AWAY\n"
                        "JESUS MY LORD!"]
        self.song_16 = ["Title",
                        "CHRIST LIVETH IN ME\nPage 235",
                        "Chorus",
                        "CHRIST LIVETH IN ME,\n"
                        "CHRIST LIVETH IN ME,\n"
                        "OH WHAT A SALVATION THIS,\n"
                        "THAT CHRIST LIVETH IN ME.",
                        "Stanza-1",
                        "ONCE FAR FROM GOD\nAND DEAD IN SIN,\n"
                        "NO LIGHT MY HEART COULD SEE;\n"
                        "BUT IN GOD'S WORD\nTHE LIGHT I FOUND,\n"
                        "NOW CHRIST LIVETH IN ME.",
                        "Stanza-2",
                        "AS RAYS OF LIGHT\nFROM YONDER SUN.\n"
                        "THO FLOW'RS OF EARTH SET FREE,\n"
                        "SO LIFE AND LIGHT\nAND LOVE CAME FORTH\n"
                        "FROM CHRIST LIVETH IN ME.",
                        "Stanza-3",
                        "AS LIVES OF FLOW'R\nWITHIN THE SEED,\n"
                        "AS IN THE CONE OF TREE,\n"
                        "SO PRAISE THE GOD\nOF TRUTH AND GRACE\n"
                        "HIS SPIRIT DWELLETH IN ME.",
                        "Stanza-4",
                        "WITH LONGING ALL\nMY HEART IS FILLED,\n"
                        "THAT LIKE HIM I MAY BE.\n"
                        "AS ON THE WONDROUS\nTHO'T I DWELL\n"
                        "THAT CHRIST LIVETH IN ME."]
        self.song_17 = ["Title",
                        "COME UNTO ME\nPage 113",
                        "Chorus",
                        "COME UNTO ME;\nI WILL GIVE YOU REST;\n"
                        "TAKE MY YOKE UPON YOU,\nHEAR ME AND BE BLEST;\n"
                        "I AM MEEK AND LOWLY,\nCOME AND TRUST MY MIGHT;\n"
                        "COME, MY YOKE IS EASY,\nAND MY BURDEN'S LIGHT.",
                        "Stanza-1",
                        "HEAR THE BLESSED SAVIOR\n"
                        "CALLING THE OPPRESSED,\n"
                        "O YE HEAVY LADEN,\nCOME TO ME AND REST;\n"
                        "COME, NO LONGER TARRY,\n"
                        "I YOUR LOAD WILL BEAR.\nBRING ME EVERY BURDEN,\n"
                        "BRING ME EVERY CARE.",
                        "Stanza-2",
                        "ARE YOU DISAPPOINTED,\nWANDRING HERE AND THERE,\n"
                        "DRAGGING CHAINS OF DOUBT AND\nLOADED DOWN WITH CARE?\n"
                        "DO UN-HOLY FEELINGS\nSTRUGGLE IN YOUR BREAST?\n"
                        "BRING YOUR CASE TO JESUS,\nHE WILL GIVE YOU REST.",
                        "Stanza-3",
                        "STUMBLING ON THE MOUNTAINS\nDARK WITH SIN AND SHAME,\n"
                        "STUMBLING TOW'RD THE PIT OF\nHELL'S CONSUMING FLAME,\n"
                        "BY THE POW'RS OF SIN DE-\nLUDED AND OPPRESSED,\n"
                        "HEAR THE TENDER SHEPHERD,\nCOME TO ME AND REST.",
                        "Stanza-4",
                        "HAVE YOU BY TEMPTATION\nOFTEN CONQUERED BEEN,\n"
                        "HAS A SENSE OF WEAKNESS\nBROUGHT DISTRESS WITHIN?\n"
                        "CHRIST WILL SANCTIFY YOU,\nIF YOU'LL CLAIM HIS BEST,\n"
                        "IN THE HOLY SPIRIT,\nHE WILL GIVE YOU REST."]
        self.song_18 = ["Title",
                        "CONSTANTLY ABIDING\nPage 44",
                        "Chorus",
                        "CONSTANTLY ABIDING JESUS IS MINE;\n"
                        "CONSTANTLY ABIDING, RAPTURE DIVINE;\n"
                        "HE NEVER LEAVES ME LONELY,\n"
                        "WHISPERS, OH SO KIND;\n"
                        "I WILL NEVER LEAVE THEE.\n"
                        "JESUS IS MINE.",
                        "Stanza-1",
                        "THERE'S A PEACE IN MY HEART\n"
                        "THAT THE WORLD NEVER GAVE,\n"
                        "A PEACE IT CANNOT TAKE AWAY,\n"
                        "THO' THE TRIALS OF LIFE\n"
                        "MAY SURROUND LIKE A CLOUD,\n"
                        "I'VE A PEACE THAT HAS COME\n"
                        "THERE TO STAY!",
                        "Stanza-2",
                        "ALL THE WORLD SEEMED TO SING\n"
                        "OF A SAVIOR AND KING\n"
                        "WHEN PEACE SWEETLY CAME TO MY HEART;\n"
                        "TROUBLES ALL FLED AWAY\n"
                        "AND MY NIGHT TURN TO DAY.\n"
                        "BLESSED JESUS, HOW GLORIOUS\n"
                        "THOU ART!",
                        "Stanza-3",
                        "THIS TREASURE I HAVE\n"
                        "IN THE TEMPLE OF CLAY,\n"
                        "WHILE HERE ON HIS FOOTSTOOL I ROAM;\n"
                        "BUT HE'S COMMING TO TAKE\n"
                        "ME SOME GLORIOUS DAY\n"
                        "OVER THERE TO MY\n"
                        "HEAVENLY HOME!"]
        self.song_19 = ["Title",
                        "COUNT YOUR BLESSINGS\nPage 52",
                        "Chorus",
                        "COUNT YOUR BLESSINGS,\n"
                        "NAME THEM ONE BY ONE\n"
                        "COUNT YOUR BLESSINGS,\n"
                        "SEE WHAT GOD HATH DONE;\n"
                        "COUNT YOUR BLESSINGS...\n"
                        "NAME THEM ONE BY ONE;\n"
                        "COUNT YOUR MANY BLESSINGS,\n"
                        "SEE WHAT GOD HATH DONE.",
                        "Stanza-1",
                        "WHEN UPON LIFES BILLOWS\n"
                        "YOU ARE TEMPEST TOSSED,\n"
                        "WHEN YOU ARE DISCOURAGED,\n"
                        "THINKING ALL IS LOST,\n"
                        "COUNT YOUR MANY BLESSINGS,\n"
                        "NAME THEM ONE BY ONE,\n"
                        "AND IT WILL SUPRISE YOU\n"
                        "WHAT THE LORD HATH DONE.",
                        "Stanza-2",
                        "ARE YOU EVER BURDENED\n"
                        "WITH A LOAD OF CARE?\n"
                        "DOES THE CROSS SEEM HEAVY\n"
                        "YOU ARE CALLED TO BEAR?\n"
                        "COUNT YOUR MANY BLESSINGS\n"
                        "EV'RY DOUBT WILL FLY,\n"
                        "AND YOU WILL BE SINGING\n"
                        "AS THE DAYS GO BY.",
                        "Stanza-3",
                        "WHEN YOU LOOK AT OTHERS\n"
                        "WITH THEIR LAND AND GOLD,\n"
                        "THINK THAT CHRIST HAS PROMISED YOU\n"
                        "HIS WEALTH UN-TOLD;\n"
                        "COUNT YOUR MANY BLESSINGS,\n"
                        "MONEY CANNOT BUY\n"
                        "YOUR REWARD ON HEAVEN,\n"
                        "NOR YOUR HOME ON HIGH.",
                        "Stanza-4",
                        "SO, AMID THE CONFLICT,\n"
                        "WHETHER GREAT OR SMALL,\n"
                        "DO NOT BE DISCOURAGED,\n"
                        "GOD IS OVER ALL;\n"
                        "COUNT YOUR MANY BLESSINGS,\n"
                        "ANGELS WILL ATTEND,\n"
                        "HELP AND COMFORT GIVE YOU\n"
                        "TO YOUR JOURNEY'S END."]
        self.song_20 = ["Title",
                        "DAY BY DAY\nPage 240",
                        "Stanza-1",
                        "DAY BY DAY AND\n"
                        "WITH EACH PASSING MOMENT,\n"
                        "STRENGTH I FIND TO MEET MY TRIALS HERE;\n"
                        "TRUSTING IN MY FATHER’S WISE BESTOWMENT\n"
                        "I’VE NO CAUSE FOR WEARY OR FOR FEAR,\n"
                        "HE WHOSE HEART\n"
                        "IS KIND BEYOND ALL MEASURE\n"
                        "GIVES UNTO EACH DAY WHAT HE DEEMS BEST\n"
                        "LOVINGLY IST PART OF PAIN AND PLEASURE\n"
                        "MINGLING TOIL, WITH PEACE AND REST.",
                        "Stanza-2",
                        "EVERY DAY MY LORD HIMSELF IS NEAR ME\n"
                        "WITH THE SPECIAL MERCY FOR EACH HOUR;\n"
                        "ALL MY CARES HE FAIN\nWOULD BEAR, AND CHEER ME,\n"
                        "HE WHOSE NAME IS COUNSELOR AND POW'R.\n"
                        "THE PROTECTION OF\nHIS CHILD AND TREASURE\n"
                        "IS A CHARGE THAT ON HIMSELF HE LAID,\n"
                        "AS THY DAYS THY STRENGTH\nSHALL BE IN MEASURE,\n"
                        "THIS THE PLEDGE TO ME HE MADE.",
                        "Stanza-3",
                        "HELP ME THEN IN EV'RY TRIBULATION\n"
                        "SO TO TRUST THY PROMISES O LORD,\n"
                        "THAT I LOSE NOT FAITH'S\nSWEET CONSOLATION\n"
                        "OFFERED ME WITH WITHIN THY HOLY WORD.\n"
                        "HELP ME LORD, WHEN TOIL\nAND TROUBLE MEETING.\n"
                        "E'ER TO TAKE, AS FROM A FATHER’S HAND,\n"
                        "ONE BY ONE, THE DAYS\nTHE MOMENTS FLEETING\n"
                        "TILL I REACH THE PROMISED LAND."]
        self.song_21 = ["Title",
                        "DOXOLOGY\nPage 154",
                        "Stanza-1",
                        "PRAISE GOD FROM ALL\nBLESSINGS FLOW,\n"
                        "PRAISE HIM ALL CREATURE\nHERE BELOW;\n"
                        "PRAISE HIM ABOVE,\nYE HEAV'NLY HOST;\n"
                        "PRAISE FATHER, SON\nAND HOLY GHOST. AMEN."]
        self.song_22 = ["Title",
                        "DWELLING IN BEAULAH LAND\nPage 174",
                        "Chorus",
                        "I'M LIVING ON THE MONTAIN, UNDER-NEATH\n"
                        "A CLOUDLESS SKY, (PRAISE GOD!)\n"
                        "I'M DRINKING AT THE FOUNTAIN\n"
                        "THAT NEVER SHALL RUN DRY;\n"
                        "O YES! I'M FEASTING ON THE MANNA\n"
                        "FROM A BOUNTIFUL SUPPLY,\n"
                        "FOR I AM DWELING IN BEAULAH LAND.",
                        "Stanza-1",
                        "FAR AWAY THE NOISE OF STRIFE\n"
                        "UPON MY EAR IS FALLING\n"
                        "THEN I KNOW THE SINS OF EARTH\n"
                        "BE-SET ON EVERY HAND;\n"
                        "DOUBT AND FEAR AND THNGS OF EARTH\n"
                        "IN VAIN TO ME ARE CALLING;\n"
                        "NONE OF THESE SHALL MOVE ME\n"
                        "FROM BEAULAH LAND.",
                        "Stanza-2",
                        "FAR BELOW THE STROM OF DOUBT\n"
                        "UPON THE WORLD IS BEATING,\n"
                        "SONS OF MEN IN BATTLE LONG\n"
                        "THE ENEMY WITH STAND;\n"
                        "SAFE AM I WITHIN THE CASTLE\n"
                        "OF GOD'S WORD RETREATING,\n"
                        "NOTHING THEN CAN REACH ME\n"
                        "'TIS BEAULAH LAND.",
                        "Stanza-3",
                        "LET STORMY BREEZES BLOW,\n"
                        "THEIR CRY CANNOT ALARM ME;\n"
                        "I AM SAFELY SHELTERED HERE\n"
                        "PROTECTED BY GODS HAND:\n"
                        "HERE THE SUN IS ALWAYS SHINNING\n"
                        "HERE THERE'S NAUGHT CAN HARM ME\n"
                        "I AM SAFE FOREVER\n"
                        "IN BEAULAH LAND.",
                        "Stanza-4",
                        "VIEWING HERE THE WORKS OF GOD,\n"
                        "I SINK IN CONTEMPLATION,\n"
                        "HEARING NOW HIS BLESSED VOICE,\n"
                        "I SEE THE WAY HE PLANNED;\n"
                        "DWELLING IN THE SPIRIT HERE,\n"
                        "I LEARN OF FULL SALVATION\n"
                        "GLADLY WILL I TARRY\n"
                        "IN BEAULAH LAND."]
        self.song_23 = ["Title",
                        "EACH STEP I TAKE\nPage 182",
                        "Chorus",
                        "EACH STEP I TAKE\n"
                        "I KNOW THAT HE WILL GUIDE ME;\n"
                        "TO HIGHER GROUND\nHE EVER LEADS ME ON.\n"
                        "UNTIL SOMEDAY\nTHE LAST STEP WILL BE TAKEN.\n"
                        "EACH STEP I TAKE\nJUST LEAD ME CLOSER HOME.",
                        "Stanza-1",
                        "EACH STEP I TAKE\n"
                        "MY SAVIOUR GOES BEFORE ME,\n"
                        "AND WITH HIS LOVING HAND\nHE LEADS THE WAY.\n"
                        "AND WITH EACH BREATH\nI WHISPER I ADORE THEE;\n"
                        "OH, WHAT JOY\nTO WALK WITH HIM EACH DAY...",
                        "Stanza-2",
                        "AT TIMES I FEEL\nMY FAITH BEGIN TO WAVER,\n"
                        "WHEN UP AHEAD\nI SEE A CHASM WIDE.\n"
                        "IT'S THEN I TURN\nAND I LOOK UP TO MY SAVIOUR,\n"
                        "I AM STRONG\nWHEN HE IS BY MY SIDE...",
                        "Stanza-3",
                        "I TRUST IN GOD,\nNO MATTER COME WHAT MAY,\n"
                        "FOR LIFE ETERNAL\nIS IN HIS HAND.\n"
                        "HE HOLDS THE KEY\nTHAT OPENS UP THE WAY.\n"
                        "THAT WILL LEAD\nME TO THE PROMISED LAND..."]
        self.song_24 = ["Title",
                        "FAITH IS THE VICTORY\nPage 159",
                        "Chorus",
                        "FAITH IS THE VICTORY!\n"
                        "FAITH IS THE VICTORY!\n"
                        "OH, GLORIOUS VICTORY,\n"
                        "THAT OVERCOMES THE WORDL.",
                        "Stanza-1",
                        "ENCAMPED ALONG THE HILLS OF LIGHT\n"
                        "YE CHRISTIAN SOLDIERS, RISE,\n"
                        "AND PRESS THE BATTLE ERE THE NIGHT\n"
                        "SHALL VEIL THE GLOWING SKIES,\n"
                        "AGAINST THE FOE IN VALES BELOW\n"
                        "LET ALL OUR STRENGTH BE HURLED;\n"
                        "FAITH IS THE VICTORY WE KNOW,\n"
                        "THAT OVERCOMES THE WORLD.",
                        "Stanza-2",
                        "HIS BANNER OVER US IS LOVE,\n"
                        "OUR SWORD THE WORD OF GOD;\n"
                        "WE TREAD THE ROAD THE SAINTS ABOVE\n"
                        "WITH SHOUTS OF TRIUMPH TROD.\n"
                        "BY FAITH, THEY LIKE\nA WHIRLWIND'S BREATH,\n"
                        "SWEPT ON O'ER EVERY FIELD;\n"
                        "THE FAITH BY WHICH\nTHEY CONQUERED DEATH\n"
                        "IS STILL OUR SHINNING SHIELD.",
                        "Stanza-3",
                        "ON EVERY HAND THE FOE WE FIND\n"
                        "DRAW UP IN DREAD ARRAY;\n"
                        "LET TENTS OF EASE BE LEFT BE HIND,\n"
                        "AND ONWARD TO THE FRAY,\n"
                        "SALVATION'S HELMET ON EACH HEAD,\n"
                        "WITH TRUTH ALL GIRT ABOUT,\n"
                        "THE EARTH SHALL TREMBLE'\nNEATH OUR TREAD,\n"
                        "AND ECHO WITH OUR SHOUT.",
                        "Stanza-4",
                        "TO HIM THAT OVERCOMES THE FOE,\n"
                        "WHITE RAIMENT SHALL BE GIV'N;\n"
                        "BEFORE THE ANGELS HE SHALL KNOW\n"
                        "HIS NAME CONFESSED IN HEAV'N\n"
                        "THEN ONWARD FROM THE HILLS OF LIGHT,\n"
                        "OUR HEARTS WITH LOVE A FLAME;\n"
                        "WE'LL VANQUISH ALL THE HOSTS OF NIGHT,\n"
                        "IN JESUS CONQU'RING NAME."]
        self.song_25 = ["Title",
                        "GLORY TO HIS NAME\nPage 153",
                        "Chorus",
                        "GLORY TO HIS NAME,...\n"
                        "GLORY TO HIS NAME;...\n"
                        "THERE TO MY HEART\nWAS A BLOOD APPLIED;\n"
                        "GLORY TO HIS NAME.",
                        "Stanza-1",
                        "DOWN AT THE CROSS\nWHERE MY SAVIOR DIED,\n"
                        "DOWN WHERE FOR CLEANSING\nFROM SIN I CRIED,\n"
                        "THERE TO MY HEART\nWAS THE BLOOD APPLIED;\n"
                        "GLORY TO HIS NAME.",
                        "Stanza-2",
                        "I AM SO WONDROUSLY\nSAVED FROM SIN,\n"
                        "JESUS SO SWEETLY\nABIDES WITHIN,\n"
                        "THERE AT THE CROSS\nWHERE HE TOOK ME IN;\n"
                        "GLORY TO HIS NAME.",
                        "Stanza-3",
                        "OH, PRECIOUS FOUNTAIN\nTHAT SAVES FROM SIN\n"
                        "I AM SO GLAD\nI HAVE ENTERED IN;\n"
                        "THERE JESUS SAVES ME\nAND KEEPS ME CLEAN;\n"
                        "GLORY TO HIS NAME.",
                        "Stanza-4",
                        "COME TO THIS FOUNTAIN\nSO RICH AND SWEET;\n"
                        "CAST THY POOR SOUL\nAT THE SAVIOR'S FEET;\n"
                        "PLUNGE IN TODAY,\nAND BE MADE COMPLETE;\n"
                        "GLORY TO HIS NAME."]
        self.song_26 = ["Title",
                        "GOD WILL TAKE CARE OF YOU\nPage 253",
                        "Chorus",
                        "GOD WILL TAKE CARE OF YOU,\n"
                        "THRU EVERY DAY, O'ER ALL THE WAY'\n"
                        "HE WILL TAKE CARE OF YOU,\n"
                        "GOD WILL TAKE CARE OF YOU.",
                        "Stanza-1",
                        "BE NOT DISMAYED WHAT E'ER BETIDE,\n"
                        "GOD WILL TAKE CARE OF YOU;\n"
                        "BENEATH HIS WINGS OF LOVE ABIDE,\n"
                        "GOD WILL TAKE CARE OF YOU.",
                        "Stanza-2",
                        "THRU DAYS OF TOIL WHEN HEART DOTH FAIL,\n"
                        "GOD WLL TAKE CARE OF YOU;\n"
                        "WHEN DANGERS FIERCE YOUR PATH ASAIL,\n"
                        "GOD WILL TAKE CARE OF YOU.",
                        "Stanza-3",
                        "ALL YOU MAY NEED HE WILL PROVIDE,\n"
                        "GOD WILL TAKE CARE OF YOU,\n"
                        "NOTHING YOU ASK WILL BE DENIED,\n"
                        "GOD WILL TAKE CARE OF YOU.",
                        "Stanza-4",
                        "NO MATTER WHAT MAY BE THE TEST,\n"
                        "GOD WILL TAKE CARE OF YOU,\n"
                        "LEAN, WEARY ONE, UPON HIS BREAST,\n"
                        "GOD WILL TAKE CARE OF YOU."]
        self.song_27 = ["Title",
                        "GRACE GREATER THAN OUR SINS\nPage 260",
                        "Chorus",
                        "GRACE, GRACE, GOD'S GRACE,\n"
                        "GRACE THAT WILL PARDON\nAND CLEANSE WITHIN\n"
                        "GRACE, GRACE GOD'S GRACE,\n"
                        "GRACE THAT IS GREATER\nTHAN ALL OUR SIN.",
                        "Stanza-1",
                        "MARVELOUS GRACE OF\nOUR LOVING LORD,\n"
                        "GRACE THAT EXCEEDS\nOUR SIN AND OUR GUILT,\n"
                        "YONDER ON CALVARY’S\nMOUNT OUT-POURED,\n"
                        "THERE WHERE THE BLOOD\nOF THE LAMB WAS SPLIT",
                        "Stanza-2",
                        "SIN AND DESPAIR LIKE\nTHE SEA WAVES COLD,\n"
                        "THREATEN THE SOUL\nWITH INFINITE LOSS;\n"
                        "GRACE THAT IS GREATER,\nYES GRACE UNTOLD,\n"
                        "POINTS TO THE REFUGE\nTHE MIGHTY CROSS",
                        "Stanza-3",
                        "DARK IS THE STAIN\nTHAT WE CANNOT HIDE,\n"
                        "WHAT CAN AVAIL\nTO WASH IT AWAY?\n"
                        "LOOK! THERE IS FLOWING\nA CRIMSON TIDE;\n"
                        "WHITER THAN SNOW\nYOU MAY BE TODAY.",
                        "Stanza-4",
                        "MARVELOUS, INFINITE\nMATCHLESS GRACE,\n"
                        "FREELY BESTOWED ON\nALL WHO BELIEVE;\n"
                        "YOU THAT ARE LONGING\nTO SEE HIS FACE;\n"
                        "WILL YOU THIS MOMENT\nHIS GRACE RECEIVE?"]
        self.song_28 = ["Title",
                        "GREAT IS THY FAITHFULNESS\nPage 12",
                        "Chorus",
                        "GREAT IS THY FAITHFULNESS!\n"
                        "GREAT IS THY FAITHFULNESS!\n"
                        "MORNING BY MORNING NEW MERCIES I SEE;\n"
                        "ALL I HAVE NEEDED THY HATH PROVIDED\n"
                        "GREAT IS THY FAITHFULNESS LORD UNTO ME!\n",
                        "Stanza-1",
                        "GREAT IS THY FAITHFULNESS,\nO GOD MY FATHER,\n"
                        "THERE IS NO SHADOW OF\nTURNING WITH THEE;\n"
                        "THOU CHANGEST NOT,\nTHY COMPASSIONS THEY FAIL NOT\n"
                        "AS THOU HAST BEEN\nTHOU FOREVER WILT BE.",
                        "Stanza-2",
                        "SUMMER AND WINTER,\nAND SPRING TIME AND HARVEST,\n"
                        "SUN MOON AND STARS\nIN THEIR COURSES ABOVE,\n"
                        "JOIN WITH ALL NATURE\nIN MANIFOLD WITNESS,\n"
                        "TO THY GREAT FAITHFULNESS,\nMERCY AND LOVE.",
                        "Stanza-3",
                        "PARDON FOR SIN AND A\nPEACE THAT ENDURETH,\n"
                        "THY OWN DEAR PRESENCE\nTO CHEER AND TO GUIDE;\n"
                        "STRENGTH FOR TODAY\nAND BRIGHT HOPE FOR TOMRROW,\n"
                        "BLESSINGS ALL MINE\nWITH TEN THOUSAND BESIDE!"]
        self.song_29 = ["Title",
                        "HAVE THINE OWN WAY LORD\nPage 15",
                        "Stanza-1",
                        "HAVE THINE OWN WAY LORD!\n"
                        "HAVE THINE OWN WAY!\n"
                        "THOU ART THE POTTER\n"
                        "I AM THE CLAY\n"
                        "MOLD ME AND MAKE ME\n"
                        "AFTER THY WILL\n"
                        "WHILE I AM WAITING\n"
                        "YIELDED AND STILL.",
                        "Stanza-2",
                        "HAVE THINE OWN WAY LORD!\n"
                        "SEARCH ME AND TRY ME\n"
                        "MASTER TO-DAY!\n"
                        "WHITER THAN SNOW, LORD\n"
                        "WASH ME JUST NOW,\n"
                        "AS IN THY PRESENCE\n"
                        "HMBLY I BOW.",
                        "Stanza-3",
                        "HAVE THINE OWN WAY LORD!\n"
                        "HAVE THINE OWN WAY\n"
                        "WOUNDED AND WEARY,\n"
                        "HELP ME, I PRAY!\n"
                        "POWER ALL POWER\n"
                        "SURELY IS THINE\n"
                        "TOUCH ME AND HEAL ME,\n"
                        "SAVIOUR DIVINE!",
                        "Stanza-4",
                        "HAVE THINE OWN WAY LORD!\n"
                        "HAVE THINE OWN WAY\n"
                        "HOLD O'ER MY BEING\n"
                        "ABSOLUTE SWAY!\n"
                        "FILL WITH THY SPIRIT\n"
                        "TILL ALL SHALL SEE\n"
                        "CHRIST ONLY, ALWAYS,\n"
                        "LIVING IN ME."]
        self.song_30 = ["Title",
                        "HAVE YOU ANY ROOM FOR JESUS\nPage 219",
                        "Chorus",
                        "ROOM FOR JESUS, KING OF GLORY\nHASTEN NOW HIS WORD OBEY\nSWING THE HEART’S\nDOOR WIDELY OPEN\nBID HIM ENTER WHILE YOU MAY.",
                        "Stanza-1",
                        "HAVE YOU ANY ROOM JESUS,\nHE WHO BORE YOUR LOAD OF SIN?\n"
                        "AS HE KNOCKS AND ASK MISSION,\nSINNER WILL YOU LET HIM IN?",
                        "Stanza-2",
                        "ROOM FOR PLEASURE, ROOM FOR BUSINESS,\nBUT FOR CHRIST THE CRUCIFIED\n"
                        "NOT A PLACE THAT LIE CAN ENTER,\nIN THE HEART FOR WHICH HE DIED?",
                        "Stanza-3",
                        "HAVE YOU ANY ROOM FOR JESUS,\nAS IN GRACE HE CALLS  AGAIN?\n"
                        "O TODAY IS TIME ACCEPTED,\nTOMORROW YOU MAY CALL IN VAIN,",
                        "Stanza-4",
                        "ROOM AND TIME NOW GIVE TO JESUS,\nSOON WILL PASS GOD’S DAY OF GRACE;\n"
                        "SOON THY HEART LEFT COULD AND SILENT,\nAND THY SAVIOR’S PLEADING CASE."]
        self.song_31 = ["Title",
                        "HE ABIDES\nPage 95",
                        "Chorus",
                        "HE ABIDES, HE ABIDES,\n"
                        "HALLELUJAH, HE ABIDES WITH ME!\nIM REJOICING NIGHT AND DAY,\n"
                        "AS I WALK THE NARROW WAY,\nFOR THE COMFORTER ABIDES WITH ME.",
                        "Stanza-1",
                        "I’M REJOICING NIGHT AND DAY,\nAS I WALK THE PILGRIM WAY\n"
                        "FOR THE HAND OF GOD\nIN ALL MY LIFE I SEE,\n"
                        "AND THE REASON OF MY BLISS,\nYES, THE SECRET ALL IS THIS:\nTHAT THE COMFORTER ABIDES WITH ME,",
                        "Stanza-2",
                        "ONCE MY HEART WAS FULL OF SIN,\nONCE I HAD NO PEACE WITH IN,\n"
                        "TILL I HEARD HOW JESUS DIED\nUPON THE TREE;\nTHEN I"
                        "FELL DOWN AT HIS FEET,\nAND THERE CAME A PEACE SO SWEET,\nNOW THE COMFORTER ABIDES WITH ME.",
                        "Stanza-3",
                        "HE IS WITH ME EVERY WHERE,\nAND HE KNOWN MY EVERY CARE,\n"
                        "I’M AS HAPPY AS A BIRD\nAND JUST AS FREE;\nFOR THE"
                        "SPIRIT HAS CONTROL,\nJESUS SATISFIES MY SOUL,\nSINCE THE COMFORTER ABIDES WITH ME.",
                        "Stanza-4",
                        "THERE’S NO THIRSTING FOR THE THINGS\nOF THE WORLD THEY’VE TAKEN WINGS;\n"
                        "LONG AGO I GAVE THEM UP,\nAND INSTANTLY ALL MY\n"
                        "NIGHT WAS TURNED TODAY,\nALL MY BURDENS ROLLED AWAY,\nNOW THE COMFORTER ABIDES WITH ME."]
        self.song_32 = ["Title",
                        "HE HIDETH MY SOUL\nPage 29",
                        "Chorus",
                        "HE HIDETH MY SOUL\nIN THE CLEFT OF THE ROCK\n"
                        "THAT SHADOWS A DRY, THIRSTY LAND;\nHE HIDETH MY LIFE\nIN THE DEPTHS OF HIS LOVE,\n"
                        "AND COVERS ME THERE WITH HIS HAND,\nAND COVERS ME THERE WITH HIS HAND.",
                        "Stanza-1",
                        "A WONDERFUL SAVIOR IS JESUS MY LORD,\nA WONDERFUL"
                        "SAVIOR TO ME,\nHE HIDETH MY SOUL\nIN THE CLEFT OF THE ROCK,\nWHERE"
                        " RIVERS OF PLEASURE I SEE",
                        "Stanza-2",
                        "A WONDERFUL SAVIOR IS JESUS MY LORD,\nHE TAKETH MY "
                        "BURDEN AWAY,\nHE HOLDETH ME UP,\nAND I SHALL NOT BE MOVED,\nHE "
                        "GIVETH ME STRENGTH AS MY DAY.",
                        "Stanza-3",
                        "WITH NUMBER LESS BLESSING\nEACH MOMENT HE CROWNS,\nAND FILLED WITH HIS "
                        "FULLNESS DIVINE,\nI SING IN MY RAPTURE, OH, GLORY TO GOD\nFOR "
                        "SUCH A REDEEMER AS MINE!",
                        "Stanza-4",
                        "WHEN CLOTHED IN HIS BRIGHTNESS,\nTRANSPORTED I RISE\nTO MEET HIM IN\n"
                        "CLOUDS OF THE SKY,\nHIS PERFECT SALVATION,\nHIS WONDERFUL LOVE,\nI’LL "
                        "SHOUT WITH THE\nMILLIONS ON HIGH."]
        self.song_33 = ["Title",
                        "HE KEEPS ME SINGING\nPage 32",
                        "Chorus",
                        "JESUS, JESUS, JESUS\nSWEETEST "
                        "NAME I KNOW,\nFILLS MY EVERY LONGING,\nKEEPS ME SINGING AS I GO,",
                        "Stanza-1",
                        "THERE’S WITHIN MY HEART A MELODY,\nJESUS WHISPERS "
                        "SWEET AND LOW:\nFEAR NOT, I AM WITH THEE, PEACE, BE STILL,\n"
                        "IN ALL OF LIFE’S EBB AND FLOW.",
                        "Stanza-2",
                        "ALL MY LIFE WAS WRECKED\nBY SIN AND STRIFE,\n"
                        "DISCORD FILLED MY HEART WITH PAIN,\nJESUS SWEPT ACROSS THE BROKEN STRINGS,\n"
                        "STIRRED THE SLUMBERING CHORDS AGAIN.",
                        "Stanza-3",
                        "FEASTING ON THE RICHES OF HIS GRACE,\nRESTING ‘NEATH HIS "
                        "SHELTERING WING,\nALWAYS LOOKING ON HIS SMILLING FACE,\n"
                        "THAT IS WHY I SHOUT AND SING.",
                        "Stanza-4",
                        "THOUGH SOMETIMES HE LEADS\nTHROUGH WATERS DEEP,\nTRIALS FALL "
                        "ACROSS THE WAY,\nTHOUGH SOMETIMES THE PATH\nSEEMS ROUGH AND STEEP,\n"
                        "SEE HIS FOOTPRINTS ALL THE WAY.",
                        "Stanza-5",
                        "SOON HE’S COMING BACK TO WELCOME ME\nFAR BEYOND THE "
                        "STARRY SKY;\nI SHALL WING MY FLIGHT\nTO WORLDS UNKNOWN\n"
                        "I SHALL REIGN WITH HIM ON HIGH."]
        self.song_34 = ["Title",
                        "HE LEADETH ME\nPage 55",
                        "Chorus",
                        "HE LEADETH ME, HE LEADETH ME!\nBY HIS OWN HANDS HE LEADETH ME!\n"
                        "HIS FAITHFUL FOLL’WER I WOULD BE,\nFOR BY HIS HAND HE LEADETH ME.",
                        "Stanza-1",
                        "HE LEADETH, ME O BLESSED THO’T!\nO WORDS WITH HEAVENLY\nCOMFORT FRAUGHT!\n"
                        "WHATE’ER I DO, WHERE’ER I BE,\nSTILL ‘TIS GOD’S HAND THAT LEADETH ME.",
                        "Stanza-2",
                        "SOMETIMES’MID SCENES OF DEEPEST GLOOM,\nSOMETIMES WHERE EDEN’S BOWERS BLOOM,\n"
                        "BY WATERS STILL, O’ER TROUBLED SEA,\nSTILL ‘TIS HIS HAND THAT LEADETH ME!",
                        "Stanza-3",
                        "LORD, I WOULD CLASP THY HAND IN MINE\nNOR EVER MURMUR NOR REPINE,\n"
                        "CONTENT, WHAT EVER LOT I SEE,\nSINCE’ TIS MY GOD THAT LEADETH ME!",
                        "Stanza-4",
                        "AND WHEN MY TASK ON EARTH IS DONE,\nWHEN, BY THY GRACE, THE VICT’RY’S WON,\n"
                        "E’EN DEATH’S COLD WAVE I WILL NOT FLEE,\nSINCE GOD THRO’ JORDAN LEADETH ME."]
        self.song_35 = ["Title",
                        "HE LIVES\nPage 66",
                        "Chorus",
                        "HE LIVES, HE LIVES\nCHRIST JESUS LIVES TODAY!\nHE WALKS WITH ME AND "
                        "TALKS WITH ME\nALONG LIFE’S NARROW WAY.\nHE LIVES, HE LIVES SALVATION "
                        "TO IMPART!\nYOU ASK ME HOW I KNOW HE LIVES?\nHE LIVES WITHIN MY HEART",
                        "Stanza-1",
                        "I SERVE A RISEN SAVIOR,\nHE’S IN THE WORLD TODAY;\nI KNOW THAT HE IS "
                        "LIVING,\nWHATEVER MEN MAY SAY;\nI SEE HIS HAND OF MERCY,\nI "
                        "HEAR HIS VOICE OF CHEER,\nAND JUST THE TIME I NEED\nHIM HE’S ALWAYS NEAR",
                        "Stanza-2",
                        "IN ALL THE WORLD AROUND ME\nI SEE HIS LOVING CARE,\nAND THO’ MY HEART GROWS "
                        "WEARY\nI NEVER WILL DESPAIR\nI KNOW THAT HE IS LEADING,\nTHRO’ "
                        "ALL THE STORMY BLAST,\nTHE DAY OF HIS APPEARING\nWILL COME AT LAST",
                        "Stanza-3",
                        "REJOICE, REJOICE, O CHRISTIAN\nLIFT UP YOUR VOICE AND SING\nETERNAL "
                        "HALLELUJAHS TO\nJESUS CHRIST THE KING!\nTHE HOPE OF ALL WHO SEEK HIM,\nTHE "
                        "HELP OF ALL WHO FIND,\nNONE OTHER IS SO LOVING,\nSO GOOD AND KIND.", ]
        self.song_36 = ["Title",
                        "HEAVENLY SUNLIGHT\nPage 92",
                        "Chorus",
                        "HEAVENLY SUNLIGHT, HEAVENLY SUNLIGHT,\nFLOODING MY SOUL WITH GLORY DIVINE:\n"
                        "HALLELUJAH, I AM REJIOCING,\nSINGING HIS PRAISES, JESUS IS MINE.",
                        "Stanza-1",
                        "WALKING IN SUNLIGHT,\nALL OF MY JOURNEY;\nOVER THE MOUNTAINS,\n"
                        "THRO’ THE DEEP VALE;\nJESUS HAS SAID “I’LL\nNEVER FORSAKE THEE,\n"
                        "PROMISE DIVINE THAT\nNEVER CAN FAIL.",
                        "Stanza-2",
                        "SHADOWS AROUND ME,\nSHADOWS ABOVE ME,\nNEVER CONCEAL MY\n"
                        "SAVIOUR AND GUIDE;\nHE IS THE LIGHT,\nIN HIM IS NO DARKNESS;\n"
                        "EVER I’M WALKING\nCLOSE TO HIS SIDE.",
                        "Stanza-3",
                        "IN THE BRIGHT SUNLIGHT,\nEVER REJOICING,\nPRESSING MY WAY TO\n"
                        "MANSIONS ABOVE,\nSINGING HIS PRAISES\nGLADLY I’M WALKING,\n"
                        "WALKING IN SUNLIGHT,\nSUNLIGHT OF LOVE."]
        self.song_37 = ["Title",
                        "HIGHER GROUND\nPage 67",
                        "Chorus",
                        "LORD, LIFT ME UP AND LET ME STAND,\n"
                        "BY FAITH, ON HEAVEN’S TABLE LAND\n"
                        "A HIGHER PLANE THAN I HAVE FOUND\n"
                        "LORD, PLANT MY FEET ON HIGHER GROUND.",
                        "Stanza-1",
                        "I’M PRESSING ON THE UPWARD WAY,\n"
                        "NEW HEIGHTS I’M GAINING EVERYDAY\n"
                        "STILL PRAYING AS I ONWARD BOUND,\n"
                        "LORD, PLANT MY FEET ON HIGHER GROUND.",
                        "Stanza-2",
                        "MY HEART HAS NO DESIRE TO STAY\n"
                        "WHERE DOUBTS ARISE AND FEARS DISMAY;\n"
                        "THO’ SOME MAY DWELL\nWHERE THESE ABOUND,\n"
                        "MY PRAYER, MY AIM, IS HIGHER GROUND",
                        "Stanza-3",
                        "I WANT TO LIVE ABOVE THE WORLD,\n"
                        "THO’ SATAN’S DARTS AT ME ARE HURLED;\n"
                        "FOR FAITH HAS CAUGHT THE JOYFUL SOUND,\n"
                        "THE SONG OF SAINTS ON HIGHER GROUND",
                        "Stanza-4",
                        "I WANT TO SCALE THE UTMOST HEIGHT,\n"
                        "AND CATCH THE GLEAM OF GLORY BRIGHT;\n"
                        "BUT STILL I’LL PRAY\nTILL HEAVEN I’VE FOUND\n"
                        "LORD, LEAD ME ON TO HIGHER GROUND"]
        self.song_38 = ["Title",
                        "HOLD THE FORT\nPage 162",
                        "Chorus",
                        "HOLD THE FORT, FOR I AM COMING,\n"
                        "JESUS SIGNALS STILL;\n"
                        "WAVE THE ANSWER BACK TO HEAVEN,\n"
                        "BY THY GRACE WE WILL.",
                        "Stanza-1",
                        "HO, MY COMRADES! SEE THE SIGNAL,\n"
                        "WAVING THE SKY!\n"
                        "REINFORCEMENTS NOW APPEARING\n"
                        "VICTORY IS NIGH.",
                        "Stanza-2",
                        "SEE THE MIGHTY HOST AND ADVANCING,\nSATAN LEADING ON;\n"
                        "MIGHTY MEN AROUND US FALLING,\nCOURAGE ALMOST GONE!",
                        "Stanza-3",
                        "SEE THE GLORIUS BANNER WAVING!\nHEAR THE TRUMPET BLOW!\n"
                        "IN OUR LEADER’S NAME WE’LL\nTRIUMPH OVER EV’RY FOE.",
                        "Stanza-4",
                        "FIERCE AND LONG THE BATTLE RAGES,\nBUT OUR HELP IS NEAR;\n"
                        "ONWARD COMES OUR GREAT COMMANDER,\nCHEER, MY COMRADES, CHEER."]
        self.song_39 = ["Title",
                        "HOLY, HOLY, HOLY\nPage 205",
                        "Stanza-1",
                        "HOLY, HOLY, HOLY,\nLORD GOD ALMIGHTY!\nEARLY IN THE "
                        "MORNING\nOUR SONG SHALL RISE TO THEE;\nHOLY, HOLY, HOLY\n"
                        "MERCIFUL AND MIGHTY!\nGOD IN THREE PERSONS,\nBLESSED TRINITY!",
                        "Stanza-2",
                        "HOLY, HOLY, HOLY!\nALL THE SAINTS ADORE THEE,\nCASTING DOWN THEIR"
                        "GOLDEN CROWNS\nAROUND THE GLASSY SEA;\nCHERUBIM AND SERAPHIM\n"
                        "FALLING DOWN BEFORE THEE,\nWHICH WERT, AND ART,\nAND EVERMORE SHALT BE.",
                        "Stanza-3",
                        "HOLY, HOLY, HOLY!\nTHO’ THE DARKNESS HIDE THEE,\nTHO’ THE EYE OF"
                        "SINFUL MAN\nTHY GLORY MAY NOT SEE;\nONLY THOU ART HOLY;\n"
                        "THERE IS NONE BESIDE THEE\nPERFECT IN POW’R,\nIN LOVE, AND PURITY.",
                        "Stanza-4",
                        "HOLY, HOLY, HOLY,\nLORD GOD ALMIGHTY!\nALL THY WORKS SHALL\n"
                        "PRAISE THY NAME,\nIN EARTH, AND SKY, AND SEA;\nHOLY, HOLY, HOLY!"
                        "MERCIFUL AND MIGHTY!\nGOD IN THREE PERSONS,\nBLESSED TRINITY!"]
        self.song_40 = ["Title",
                        "HOW GREAT THOU ART\nPage 166",
                        "Chorus",
                        "THEN SINGS MY SOUL,\n"
                        "MY SAVIOUR GOD TO THEE;\n"
                        "HOW GREAT THOU ART,\nHOW GREAT THOU ART! (2X)",
                        "Stanza-1",
                        "O LORD MY GOD!\nWHEN I IN AWESOME WONDER\n"
                        "CONSIDER ALL THE WORLDS\nTHY HANDS HAVE MADE,\n"
                        "I SEE THE STARS,\nI HEAR THE ROLLING THUNDER,\n"
                        "THY POW’R THROUGH OUT\nTHE UNIVERSE DISPLAYED,",
                        "Stanza-2",
                        "WHEN THROUGH THE WOODS\n"
                        "AND FOREST GLADES I WANDER\n"
                        "AND HEAR THE BIRDS\nSING SWEETLY IN THE TREES\n"
                        "WHEN I LOOK DOWN,\n"
                        "FROM LOFTY MOUNTAIN GRANDEUR\n"
                        "AND HEAR THE BROOK\nAND FEEL THE GENTLE BREEZE;",
                        "Stanza-3",
                        "AND WHEN I THINK\n"
                        "THAT GOD, HIS SON NOT SPARRING,\n"
                        "SENT HIM TO DIE,\nI SCACRE CAN TAKE IT IN;\n"
                        "THAT ON THE CROSS,\nMY BURDENS GLADLYBEARING,\nHE BLED AND DIED\nTO TAKE AWAY MY SIN;",
                        "Stanza-4",
                        "WHEN CHRIST SHALL COME\nWITH SHOUT OF ACCLAMATION\nAND TAKE ME HOME,\nWHAT JOY SHALL MY HEART\n"
                        "THEN I SHALL BOW\nIN HUMBLE ADORATION\nAND THERE PROCLAIM,\nMY GOD, HOW GREAT THOU ART!"]
        self.song_41 = ["Title",
                        "I AM RESOLVED\nPage 48",
                        "Chorus",
                        "I WILL HASTEN TO HIM,\nHASTEN SO GLAD AND FREE,\n"
                        "JESUS, GREATEST, HIGHEST,\nI WILL COME TO THEE",
                        "Stanza-1",
                        "I AM RESOLVED\nNO LONGER TO LINGER,\nCHARMED BY THE WORLD’S DELIGHT;\n"
                        "THINGS THAT HIGHER,\nTHINGS THAT ARE NOBLER,\nTHESE HAVE ALLURED MY SIGHT.",
                        "Stanza-2",
                        "I AM RESOLVED\nTO GO TO THE SAVIOR,\nLEAVING MY SIN AND STRIFE;\n"
                        "HE IS THE TRUE ONE,\nHE IS THE JUST ONE,\nHE HATH THE WORDS OF LIFE.",
                        "Stanza-3",
                        "I AM RESOLVED\nTO FOLLOW THE SAVIOR,\nFAITHFUL AND TRUE EACH DAY;\n"
                        "HEED WHAT HE SAYETH,\nDO WHAT HE WILLETH,\nHE IS THE LIVING WAY.",
                        "Stanza-4",
                        "I AM RESOLVED\nTO ENTER THE KINGDOM,\nLEAVING THE PATHS OF SIN;\n"
                        "FRIENDS MAY OPPOSE ME,\nFOES MAY BESET ME,\nSTILL WILL I ENTER IN.",
                        "Stanza-5",
                        "I AM RESOLVED,\nAND WHO WILL GO WITH ME?\nCOME, FRIENDS, WITHOUT DELAY,\n"
                        "TAUGHT BY THE BIBLE,\nLED BY THE SPIRIT,\nWE’LL WALK THE HEAVENLY WAY."]
        self.song_42 = ["Title",
                        "I AM THINE, O LORD\nPage 42",
                        "Chorus",
                        "DRAW ME NEARER, NEARER, BLESSED LORD,\nTO THE CROSS WHERE THOU HAST DIED;\n"
                        "DRAW ME NEARER, NEARER,\nNEARER, BLESSED LORD,\nTO THY PRECIOUS, BLEEDING SIDE.",
                        "Stanza-1",
                        "I AM THINE, O LORD,\nI HAVE HEARD THY VOICE,\nAND IT TOLD THY"
                        "LOVE TO ME;\nBUT I LONG TO RISE\nIN THE ARMS OF FAITH,\nAND BE CLOSER DRAWN TO THEE.",
                        "Stanza-2",
                        "CONSECRATE ME NOW\nTO THY SERVICE, LORD,\nBY THE POWER OF GRACE DIVINE;\n"
                        "LET MY SOUL LOOK UP\nWITH A STEADFAST HOPE.\nAND MY WILL BE LOST IN THINE.",
                        "Stanza-3",
                        "O THE PURE DELIGHT\nOF A SINGLE HOUR THAT BEFORE\nTHY THRONE "
                        "I SPEND,\nWHEN I KNEEL IN PRAYER,\nAND WITH THEE MY GOD,\nI COMMUNE AS FRIEND WITH FRIEND!",
                        "Stanza-4",
                        "THERE ARE DEPTHS OF LOVE\nTHAT I CANNOT KNOW\nTILL I CROSS THE "
                        "NARROW SEA;\nTHERE ARE HEIGHTS OF JOY\nTHAT I MAY NOT REACH\nTILL I REST IN PEACE WITH THEE."]
        self.song_43 = ["Title",
                        "I BELONG TO THE KING\nPage 188",
                        "Chorus",
                        "I BELONG TO THE KING,\nI’M A CHILD OF HIS LOVE,\n"
                        "AND HE NEVER FOR SAKETH HIS OWN;\nHE WILL CALL ME SOME"
                        "DAY\nTO HIS PALACE ABOVE,\nA SHALL DWELL BY HIS GLORIFIED THRONE.",
                        "Stanza-1",
                        "I BELONG TO THE KING,\nI’M A CHILD OF HIS LOVE,\nI SHALL DWELL IN HIS "
                        "PALACE SO FAIR,\nFOR HE TELLS OF ITS BLISS\nIN YOU HEAVEN ABOVE,\nAND HIS "
                        "CHILDREN ITS\nSPLENDOR SHALL SHARE.",
                        "Stanza-2",
                        "I BELONG TO THE KING,\nAND HE LOVES ME I KNOW,\nFOR HIS MERCY AND "
                        "KINDNESS, SO FREE,\nARE UNCEASINGLY MINE,\nWHERESOEVER I GO,\nAND MY "
                        "REFUGE UNFAILING IS HE.",
                        "Stanza-3",
                        "I BELONG TO THE KING,\nAND HIS PROMISE IS SURE,\nTHAT WE ALL SHALL BE\n"
                        "GATHERED AT LAST\nIN HIS KINGDOM ABOVE,\nBY LIFE’S WATERS SO PURE,\nWHEN THIS "
                        "LIFE\nWITH ITS TRIALS IS PAST."]
        self.song_44 = ["Title",
                        "I HEARD THE VOICE OF JESUS SAY\nPage 203",
                        "Chorus",
                        "I HEARD THE VOICE OF JESUS SAY, “COME UNTO ME AND REST; "
                        "LAY DOWN, THOU WEART ONE, LAY DOWN THE HEAD UPON MY BREAST.” "
                        "I CAME TO JESUS AS I WAS, WEARY AND WORN AND SAD, "
                        "I FOUND HIM A RESTING PLACE, AND HE HAS MADE ME GLAD.",
                        "Stanza-1",
                        "I HEARD THE VOICE OF JESUS SAY, “BEHOLD, I FREELY GIVE "
                        "THE LIVING WATER; THIRSTY ONE, STOOP DOWN AND DRINK, AND LIVE.” "
                        "I CAME TO JESUS AND I DRANK OF THAT LIFE GIVING STREAM; "
                        "MY THIRST WAS QUENCHED, MY SOUL REVIVED, AND NOW I LIVE IN HIM. ",
                        "Stanza-2",
                        "I HEARD THE VIOCE OF JESUS SAY, “I AM THIS DARK WORLD’S LIGHT; "
                        "LOOK UNTO ME, THY MORN SHALL RISE, AND ALL THY DAY BE BRIGHT.” "
                        "I LOOKED TO JESUS AND I FOUND IN HIM MY STAR, MY SUN; "
                        "AND IN THAT LIGHT OF LIFE I’LL WALK, TILL TRAVELING DAYS ARE DONE."]
        self.song_45 = ["Title",
                        "I KNOW WHO HOLDS TOMORROW\nPage 163",
                        "Chorus",
                        "MANY THINGS ABOUT TOMORROW,\nI DON’T SEEM TO UNDERSTAND\n"
                        "BUT I KNOW WHO HOLDS TOMORROW,\nAND I KNOW WHO HOLDS MY HAND.",
                        "Stanza-1",
                        "I DON’T KNOW ABOUT TOMORROW,\nI JUST LIVE FROM DAY TODAY.\n"
                        "I DON’T BORROW FROM ITS SUNSHINE,\nFOR ITS SKIES MAY TURN TO GRAY.\n"
                        "I DON’T WORRY O’ER THE FUTURE,\nFOR I KNOW WHAT JESUS SAID,\n"
                        "AND TODAY I’LL WALK BESIDE HIM,\nFOR HE KNOWS WHAT IS AHEAD.",
                        "Stanza-2",
                        "EV’RY STEP IS GETTING BRIGHTER,\nAS THE GOLDEN STAIRS I CLIMB;\n"
                        "EV’RY BURDEN’S GETTING LIGHTER;\nEV’RY CLOUD IS SILVER LINED.\n"
                        "THERE THE SUN IS ALWAYS SHINING,\nTHERE NO TEAR WILL DIM THE EYE,\n"
                        "AT THE ENDING OF THE RAINBOW\nWHERE THE MOUNTAINS TOUCH THE SKY.",
                        "Stanza-3",
                        "I DON’T KNOW ABOUT TOMORROW,\nIT MAY BRING ME POVERTY;\n"
                        "BUT THE ONE WHO FEEDS THE SPARROW.\nIS THE ONE WHO STANDS BY ME.\n"
                        "AND THE PATH THAT BE MY PORTION,\nMAY BE THROUGH THE FLAME OR FLOOD,\n"
                        "BUT HIS PRESENCE GOES BEFORE ME,\nAND I’M COVERED WITH HIS BLOOD."]
        self.song_46 = ["Title",
                        "I KNOW WHOM I HAVE BELIEVED\nPage 49",
                        "Chorus",
                        "BUT I KNOW WHOM I HAVE BELIEVED,\nAND AM PERSUADED\nTHAT HE IS "
                        "ABLE\nTO KEEP THAT WHICH I’VE COMMITTED\nUNTO HIM AGAINST THAT DAY.",
                        "Stanza-1",
                        "I KNOW NOT WHY GOD’S WONDROUS GRACE\nTO ME HE HATH MADE KNOWN,\n"
                        "NOR WHY, UNWORTHY, CHRIST IN LOVE\nREDEEMED ME FOR HIS OWN.",
                        "Stanza-2",
                        "I KNOW NOT HOW THIS SAVING FAITH\nTO ME HE DID IMPART,\n"
                        "NOR HOW BELIEVING IN HIS WORD\nWROUGHT PEACE WITHIN MY HEART.",
                        "Stanza-3",
                        "I KNOW NOT HOW THE SPIRIT MOVES,\nCONVINVING MEN OF SIN,\n"
                        "REVEALING JESUS THRO’ THE WORD,\nCREATING FAITH IN HIM.",
                        "Stanza-4",
                        "I KNOW NOT WHAT OF GOOD OR ILL\nMAY BE RESERVED FOR ME,\n"
                        "OF WEARY WAYS OR GOLDEN DAYS,\nBEFORE HIS FACE I SEE.",
                        "Stanza-5",
                        "I KNOW NOT WHEN MY LORD MAY COME,\nAT NIGHT OR NOON DAY FAIR,\n"
                        "NOR IF I’ll WALK THE VALE WITH HIM,\nOR “MEET HIM IN THE AIR.”"]
        self.song_47 = ["Title",
                        "I LOVE TO TELL THE STORY\nPage 60",
                        "Chorus",
                        "I LOVE TO TELL THE STORY ,\n‘TWILL BE MY THEME IN GLORY\nTO TELL THE OLD, OLD "
                        "STORY\nOF JESUS AND HIS LOVE.",
                        "Stanza-1",
                        "I LOVE TO TELL THE STORY,\nOF UNSEEN THINGS ABOVE,\nOF "
                        "JESUS AND HIS GLORY,\nOF JESUS AND HIS LOVE,\nI LOVE TO "
                        "TELL THE STORY,\nBECAUSE I KNOW ‘TIS TRUE;\nIT SATISFIES MY "
                        "LONGINGS\nAS NOTHING ELSE CAN DO.",
                        "Stanza-2",
                        "I LOVE TO TELL THE STORY,\nMORE WONDERFUL IT SEEMS\nTHAN "
                        "ALL THE GOLDEN FANCIES\nOF ALL OUR GOLDEN DREAMS.\nI LOVE TO "
                        "TELL THE STORY,\nIT DID SO MUCH FOR ME;\nAND THAT IS JUST THE REASON\nI TELL "
                        "IT NOW TO THEE.",
                        "Stanza-3",
                        "I LOVE TO TELL THE STORY,\n‘TIS PLEASANT TO REPEAT\nWHAT "
                        "SEEMS, EACH TIME I TELL IT,\nMORE WONDERFULLY SWEET.\nI LOVE TO "
                        "TELL THE STORY,\nFOR SOME HAVE NEVER HEARD,\nTHE MESSAGE OF "
                        "SALVATION\nFROM GOD’S OWN HOLY WORD.",
                        "Stanza-4",
                        "I LOVE TO TELL THE STORY,\nFOR THOSE WHO KNOW IT BEST\nSEEM "
                        "HUNGERING AND THIRSTING\nTO HEAR IT LIKE THE REST.\n"
                        "AND WHEN, IN SCENES OF GLORY,\nI SING THE NEW, NEW SONG,\n‘TWILL BE THE OLD, "
                        "OLD  STORY\nTHAT I HAVE LOVED SO LONG."]
        self.song_48 = ["Title",
                        "I NEED THEE EVERY HOUR\nPage 223",
                        "Chorus",
                        "I NEED THEE, OH! I NEED THEE;\nEV’RY HOUR I NEED THEE!\nO "
                        "BLESS ME NOW, MY SAVIOUR,\nI COME TO THEE!",
                        "Stanza-1",
                        "I NEED THEE EV’RY HOUR,\nMOST GRACIOUS LORD;\nNO "
                        "TENDER VOICE LIKE THINE\nCAN PEACE AFFORD",
                        "Stanza-2",
                        "I NEED THEE EV’RY HOUR,\nSTAY THOU NEARBY;\nTEMPTATIONS "
                        "LOSE THEIR POW’R\nWHEN THOU ART NIGH",
                        "Stanza-3",
                        "I NEED THEE EV’RY HOUR,\nIN JOY OR PAIN:\nCOME "
                        "QUICKLY AND ABIDE,\nOR LIFE IS VAIN",
                        "Stanza-4",
                        "I NEED THEE EV’RY HOUR,\nMOST HOLY ONE;\n"
                        "O MAKE ME THINE INDEED,\nTHOU BLESSED SON!", ]
        self.song_49 = ["Title",
                        "I SHALL NOT BE MOVED\nPage 41",
                        "Chorus",
                        "I SHALL NOT BE, I SHALL NOT BE MOVED;\n"
                        "I SHALL NOT BE, I SHALL NOT BE MOVED;\nJUST LIKE A TREE THAT’S\n"
                        "PLANTED BY THE WATERS,\nLORD, I SHALL NOT BE MOVED",
                        "Stanza-1",
                        "JESUS IS MY SAVIOUR,\nI SHALL NOT BE MOVED;\nIN HIS LOVE AND FAVOR,\n"
                        "I SHALL NOT BE MOVED;\nJUST LIKE A TREE THAT’S\n"
                        "PLANTED BY THE WATERS,\nLORD, I SHALL NOT BE MOVED.",
                        "Stanza-2",
                        "IN MY CHRIST ABIDING,\nI SHALL NOT BE MOVED;\nIN HIS LOVE I’M HIDING,\n"
                        "I SHALL NOT BE MOVED;\nJUST LIKE A TREE THAT’S\n"
                        "PLANTED BY THE WATERS,\nLORD, I SHALL NOT BE MOVED",
                        "Stanza-3",
                        "IF I TRUST HIM EVER,\nI SHALL NOT BE MOVED;\nHE WILL FAIL ME NEVER,\n"
                        "I SHALL NOT BE MOVED;\nJUST LIKE A TREE THAT’S\n"
                        "PLANTED BY THE WATERS,\nLORD, I SHALL NOT BE MOVED",
                        "Stanza-4",
                        "ON HIS WORD I’M FEEDING,\nI SHALL NOT BE MOVED;\nHE’S THE ONE THAT’S LEADING\n"
                        "I SHALL NOT BE MOVED;\nJUST LIKE A TREE THAT’S\n"
                        "PLANTED BY THE WATERS,\nLORD, I SHALL NOT BE MOVED"]
        self.song_50 = ["Title",
                        "I SURRENDER ALL\nPage 147",
                        "Chorus",
                        "I SURREDER ALL, I SURRENDER ALL\n"
                        "ALL TO THEE, MY BLESSED SAVIOUR,\nI SURRENDER ALL.",
                        "Stanza-1",
                        "ALL TO JESUS I SURRENDER, ALL\nTO HIM I FREELY GIVE;\n"
                        "I WILL EVER LOVE\nAND TRUST HIM, IN\nHIS PRESSENCE DAILY LIVE.",
                        "Stanza-2",
                        "ALL TO JESUS I SURRENDER,\nHUMBLY AT HIS FEET I BOW;\n"
                        "WORDLY PLEASURES ALL\nFORSAKEN, TAKE\nME, JESUS, TAKE ME NOW.",
                        "Stanza-3",
                        "ALL TO JESUS I SURRENDER, MAKE\nME, SAVIOUR, WHOLY THINE;\n"
                        "LET ME FEEL THE HOLY\nSPIRIT, TRULY\nKNOW THAT THOU ART MINE.",
                        "Stanza-4",
                        "ALL TO JESUS I SURRENDER, LORD,\nI GIVE MYSELF TO THEE;\n"
                        "FILL ME WITH THY LOVE\nAND POWER, LET\nTHY BLESSING FALL ON ME."]
        self.song_51 = ["Title",
                        "I’LL BE TRUE, PRECIOUS JESUS\nPage 119",
                        "Chorus",
                        "THERE’S A RACE TO BE RUN,\nTHERE’S A "
                        "VICT’RY TO BE WON\nEV’RY HOUR, BY THY POWER\nI’LL BE TRUE.",
                        "Stanza-1",
                        "I’LL BE TRUE PRECIOUS JESUS,\nI’LL BE TRUE, (2X)",
                        "Stanza-2",
                        "I’LL GO THROUGH PRECIOUS JESUS,\nI’LL GO THROUGH (2X)"]
        self.song_52 = ["Title",
                        "IS YOUR ALL IN THE ALTAR\nPage 146",
                        "Chorus",
                        "IS YOUR ALL ON THE ALTAR\nOF "
                        "SACRIFICE LAID?\nYOUR HEART, DOES\nTHE SPIRIT CONTROL?\nYOU CAN ONLY BE "
                        "BLEST\nAND HAVE PEACE AND SWEET REST,\nAS YOU YIELD HIM\nYOUR BODY AND SOUL.",
                        "Stanza-1",
                        "YOU HAVE LONGED FOR SWEET PEACE,\nAND FOR FAITH TO INCREASE,\nHAVE EARNESTLY, "
                        "FERVENTLY PRAYED;\nBUT YOU CANNOT HAVE REST\nOR BE PERFECTLY BLEST\n"
                        "UNTIL ALL ON THE ALTAR IS LAID.",
                        "Stanza-2",
                        "WOULD YOU WALK WITH LORD,\nIN THE LIGHT OF HIS WORD,\nAND HAVE PEACE AND\nCONTENTMENT "
                        "ALWAYS,\nYOU MUST DO HIS SWEET WILL,\nTO BE FREE FROM ALL ILL,\n"
                        "ON THE ALTAR YOUR ALL YOU MUST LAY.",
                        "Stanza-3",
                        "OH, WE NEVER CAN KNOW\nWHAT THE LORD WILL BESTOW\nOF THE BLESSINGS FOR\n"
                        "WHICH WE HAVE PRAYED,\nTILL OUR BODY AND SOUL\nHE DOTH FULLY CONTROL,\n"
                        "AND OUR ALL ON\nTHE ALTAR IS LAID.",
                        "Stanza-4",
                        "WHO CAN TELL ALL THE LOVE\nHE WILL SEND FROM ABOVE,\nAND HOW UNHAPPY\nOUR "
                        "HEARTS WILL BE MADE,\nOF THE FELLOWSHIP SWEET\nWE SHALL SHARE AT HIS FEET,\n"
                        "WHEN OUR ALL ON\nTHE ALTAR IS LAID."]
        self.song_53 = ["Title",
                        "IT IS WELL WITH MY SOUL\nPage 145",
                        "Chorus",
                        "IT IS WELL WITH MY SOUL,\n"
                        "IT IS WELL, IT IS WELL WITH MY SOUL.",
                        "Stanza-1",
                        "WHEN PEACE, LIKE A RIVER,\nATTENDETH MY WAY,\nWHEN SORROW LIKE "
                        "SEA BILLOWS ROLL;\nWHAT EVER MY LOT,\nTHOU HAST TAUGHT ME TO STAY,\n"
                        "IT IS WELL, IT IS WELL WITH MY SOUL.",
                        "Stanza-2",
                        "THOUGH SATAN SHOULD BUFFET,\nTHO’ TRIALS SHOULD COME,\nLET THIS BLEST ASSURANCE "
                        "CONTROL,\nTHAT CHRIST HAS REGARDED\nMY HELPLESS ESTATE, "
                        "AND HATH SHED\nHIS OWN BLOOD FOR MY SOUL.",
                        "Stanza-3",
                        "MY SIN OH, THE BLISS\nOF THIS GLORIOUS THO’T\nMY SIN NOT IN PART,\n"
                        "BUT THE WHOLE\nIS NAILED TO THE CROSS\nAND I BEAR IT NO MORE,\n"
                        "PRAISE THE LORD,\nPRAISE THE LORD, O MY SOUL!",
                        "Stanza-4",
                        "AND, LORD, HASTE THE DAY\nWHEN THE FAITH SHALL BE SIGHT,\nTHE CLOUDS BE ROLLED"
                        "BACK AS A SCROLL,\nTHE TRUMP SHALL RESOUND\nAND THE LORD SHALL DESCEND,\n"
                        "“EVEN SO” IT IS WELL WITH MY SOUL."]
        self.song_54 = ["Title",
                        "JESUS PAID IT ALL,\nPage 211",
                        "Chorus",
                        "JESUS PAID IT ALL,\nALL TO HIM I OWE:\nSIN HAD LEFT "
                        "A CRIMSON STAIN,\nHE WASHED IT WHITE AS SNOW.",
                        "Stanza-1",
                        "I HEAR THE SAVIOUR SAY,\n“ THY STRENGHT INDEED IS SMALL,\nCHILD OF "
                        "WEAKNESS, WATCH AND PRAY,\nFIND IN ME THINE IN ALL.”",
                        "Stanza-2",
                        "LORD, NOW INDEED I FIND\nTHY POWER, AND THINE ALONE,\nCAN CHANGE "
                        "THE LEPER’S SPOTS,\nAND MELT THE HEART OF STONE.",
                        "Stanza-3",
                        "FOR NOTHING GOOD HAVE I\nWHERE BY THY GRACE TO CALM\nI’LL "
                        "WASH MY GARMENTS WHITE\nIN THE BLOOD OF CALVARY’S LAMB.",
                        "Stanza-4",
                        "AND WHEN, BEFORE THE THRONE,\nI STAND IN HIM COMPLETE,\n“JESUS "
                        "DIED MY SOUL TO SAVE,”\nMY LIPS SHALL STILL REPEAT."]
        self.song_55 = ["Title",
                        "JESUS SAVES\nPage 8",
                        "Stanza-1",
                        "WE HAVE HEARD THE JOYFUL SOUND:\nJESUS SAVES! JESUS SAVES!\n"
                        "SPRED THE TIDINGS ALL AROUND:\nJESUS SAVES! JESUS SAVES!\n"
                        "BEAR THE NEWS TO EV’RY LAND,\nCLIMB THE STEEPS AND\nCROSS THE WAVES;\n"
                        "ONWARD! ‘TIS OUR LORD’S COMMAND;\nJESUS SAVES! JESUS SAVES!",
                        "Stanza-2",
                        "WAFT IT ON THE ROLLING TIDE;\nJESUS SAVES! JESUS SAVES!\n"
                        "SPRED THE TIDINGS ALL AROUND;\nJESUS SAVES! JESUS SAVES!\n"
                        "SING, YE ISLANDS OF THE SEA;\nECHO BACK, YE OCEAN CAVES;\n"
                        "EARTH SHALL KEEP HER JUBILEE:\nJESUS SAVES! JESUS SAVES!",
                        "Stanza-3",
                        "SING ABOVE THE BATTLE STRIFE,\nJESUS SAVES! JESUS SAVES!\n"
                        "BY HIS DEATH AND ENDLESS LIFE,\nJESUS SAVES! JESUS SAVES!\n"
                        "SING IT SOFTLY THROUGH THE GLOOM,\nWHEN THE HEART FOR MERCY CRAVES;\n"
                        "SING IN TRIUMPH O’ER THE TOMB,\nJESUS SAVES! JESUS SAVES!",
                        "Stanza-4",
                        "GIVE THE WINDS A MIGHTY VOICE,\nJESUS SAVES! JESUS SAVES!\n"
                        "LET THE NATIONS NOW REJOICE,\nJESUS SAVES! JESUS SAVES!\n"
                        "SHOUT SALVATION FULL AND FREE;\nHIGHEST HILLS AND DEEPEST CAVES;\n"
                        "THIS OUR SONG OF VICTORY,\nJESUS SAVES! JESUS SAVES!"]
        self.song_56 = ["Title",
                        "JESUS, LOVER OF MY SOUL\nPage 124"
                        "Chorus",
                        "Stanza-1",
                        "Stanza-2",
                        "Stanza-3"]
        self.song_57 = ["Title",
                        "JOY IN SERVING JESUS\nPage 262",
                        "Chorus",
                        "THERE IS JOY, JOY,\nJOY IN SERVING JESUS,\nJOY THAT THROBS WITH"
                        "IN MY HEART;\nEV’RY MOMENT, EV’RY HOUR,\nAS I DRAW UPON "
                        "HIS POW’R,\nTHERE IS JOY, JOY,\nJOY THAT NEVER SHALL DEPART.",
                        "Stanza-1",
                        "THERE IS JOY IN SERVING JESUS,\nAS I JOURNEY ON MY WAY,\n"
                        "JOY THAT FILLS THE HEART WITH PRAISES,\nEV’RY HOUR EV’RY DAY.",
                        "Stanza-2",
                        "THERE IS JOY IN SERVING JESUS,\nJOY THAT TRIUMPS OVER PAIN;\n"
                        "FILLS MY SOUL WITH HEAVEN’S MUSIC,\nTILL I JOIN THE GLAD REFRAIN,",
                        "Stanza-3",
                        "THERE IS JOY IN SERVING JESUS,\nAS I WALK ALONE WITH GOD;\n"
                        "‘TIS THE JOY OF CHRIST, MY SAVIOUR,\nWHO THE PATH OF SUFF’RING TROD.",
                        "Stanza-4",
                        "THERE IS JOY IN SERVING JESUS,\nJOY AMID THE DARKEST NIGHT,\n"
                        "FOR I’VE LEARNED THE WONDROUS SECRET,\nAND I’M WALKING IN THE LIGHT.", ]
        self.song_58 = ["Title",
                        "JUST AS I AM\nPage 131",
                        "Stanza-1",
                        "JUST AS I AM, WITHOUT ONE PLEA,\nBUT THAT THY BLOOD WAS SHED FOR ME,\n"
                        "AND THAT BIDD’ST ME COME TO THEE,\nO LAMB OF GOD, I COME! I COME!",
                        "Stanza-2",
                        "JUST AS I AM, AND WAITING NOT\nTO RID MY SOUL OF ONE DARK BLOT,\n"
                        "TO THEE WHOSE BLOOD\nCAN CLEANSE EACH SPOT,\nO LAMB OF GOD, I COME! I COME!",
                        "Stanza-3",
                        "JUST AS I AM, THOUGH TOSSED ABOUT\nWITH MANY  A CONFLICT, MANY A DOUBT,\n"
                        "FIGHTINGS AND FEARS WITHIN, WITHOUT,\nO LAMB OF GOD OF GOD, I COME! I COME!",
                        "Stanza-4",
                        "JUST AS I AM POOR, WRATCHED, BLIND;\nSLIGHT, RICHES, HEALING OF MIND,\n"
                        "YES, ALL I NEED IN THEE TO FIND,\nO LAMB OF GOD, I COME! I COME!",
                        "Stanza-5",
                        "JUST AS I AM THOU WILT RECEIVE,\nWILT WELCOME, PARDON,\nCLEANSE, RELIEVE,\n"
                        "BECAUSE THY PROMISE I BELIEVE,\nO LAMB OF GOD, I COME! I COME!"]
        self.song_59 = ["Title",
                        "LEANING ON THE EVERLASTING ARMS\nPage 179",
                        "Chorus",
                        "LEANING, LEANING,\nSAFE AND SECURE\nFROM ALL ALARMS;\n"
                        "LEANING , LEANING, LEANING ON\nTHE EVERLASTING ARMS.",
                        "Stanza-1",
                        "WHAT A FELLOWSHIP,\nWHAT A JOY DIVINE,\nLEANING ON THE EVERLASTING ARMS;\n"
                        "WHAT A BLESSEDNESS,\nWHAT A PEACE IS MINE,\nLEANING ON THE EVERLASTING ARMS",
                        "Stanza-2",
                        "OH, HOW SWEET TO WALK\nIN THIS PILGRIM WAY,\nLEANING ON THE EVERLASTING ARMS;\n"
                        "OH, HOW BRIGHT THE PATH\nGROWS FROM DAY TO DAY,\nLEANING ON THE EVERLASTING ARMS.",
                        "Stanza-3",
                        "WHAT HAVE I TO DREAD,\nWHAT HAVE I TO FEAR,\nLEANING ON THE EVERLASTING ARMS;\n"
                        "I HAVE BLESSED PEACE\nWITH MY LORD SO NEAR,\nLEANING ON THE EVERLASTING ARMS."]
        self.song_60 = ["Title",
                        "LIVING FOR JESUS\nPage 282",
                        "Chorus",
                        "O JESUS, LORD AND SAVIOUR,\nI GIVE MYSELF TO THEE;\n"
                        "FOR THOU IN THY ATONEMENT,\nDIDST GIVE THYSELF FOR ME:\n"
                        "I OWN NO OTHER MASTER,\nMY HEART SHALL BE MY THRONE,\n"
                        "MY LIFE I GIVE, HENCEFORTH TO LIVE,\nO CHRIST FOR THEE ALONE.",
                        "Stanza-1",
                        "LIVING FOR JESUS\nA LIFE THAT IS TRUE,\n"
                        "STRIVING TO PLEASE HIM,\nIN ALL THAT I DO,\n"
                        "YIELDING ALLEGIANCE,\nGLAD-HEARTED AND FREE,\n"
                        "THIS IS THE PATHWAY\nOF BLESSING FOR ME.",
                        "Stanza-2",
                        "LIVING FOR JESUS\nWHO DIED IN MY PLACE,\n"
                        "BEARING ON CALV’RY\nMY SIN AND DISGRACE,\n"
                        "SUCH LOVE CONSTRAINS ME\nTO ANSWER HIS CALL,\n"
                        "FOLLOW HIS LEADING\nAND GIVE HIM MY ALL.",
                        "Stanza-3",
                        "LIVING FOR JESUS\nWHEREVER I AM,\n"
                        "DOING EACH DUTY\nIN HIS HOLY NAME,\n"
                        "WILLING TO SUFFER\nAFFLICTION OR LOSS,\n"
                        "DEEMING EACH TRIAL\nA PART OF MY CROSS.",
                        "Stanza-4",
                        "LIVING FOR JESUS\nTHRU EARTH’S LITTLE WHILE\n"
                        "MY DEAREST TREASURE,\nTHE LIGHT OF HIS SMILE\n"
                        "SEEKING THE LOST ONES\nHE DIED TO REDEEM,\n"
                        "BRINGING THE WEARY\nTO FIND REST IN HIM."]
        self.song_61 = ["Title",
                        "LOVE LIFTED ME\nPage 9",
                        "Chorus",
                        "LOVE LIFTED ME! LOVE LIFTED ME!\n"
                        "WHEN NOTHING ELSE COULD HELP,\nLOVE LIFTED ME. (2x)",
                        "Stanza-1",
                        "I WAS SINKING DEEP IN SIN,\nFAR FROM THE PEACEFUL SHORE,\n"
                        "VERY DEEPLY STAINED WITHIN,\nSINKING TO RISE NO MORE;\n"
                        "BUT THE MASTER OF THE SEA\nHEARD MY DESPAIRING CRY\n"
                        "FROM THE WATERS LIFTED ME,\nNOW SAFE AM I.",
                        "Stanza-2",
                        "ALL MY HEART TO HIM I GIVE,\nEVER TO HIM I’LL CLING,\n"
                        "IN HIS BLESSED PRESENCE LIVE,\nEVER HIS PRAISES SING.\n"
                        "LOVE SO MIGHTY AND SO TRUE\nMERITS MY SOULS BEST SONGS;\n"
                        "FAITHFUL, LOVING SERVICE, TOO,\nTO HIM BELONGS.",
                        "Stanza-3",
                        "SOULS IN DANGER, LOOK ABOVE,\nJESUS COMPLETELY SAVE;\n"
                        "HE WILL LIFT YOU BY HIS LOVE\nOUT OF THE ANGRY WAVES,\n"
                        "HIS THE MASTER OF THE SEA,\nBELOWS HIS WILL OBEY;\n"
                        "HE YOUR SAVIOUR WANTS TO BE-\nBE SAVE TODAY."]
        self.song_62 = ["Title",
                        "LOYALTY TO CHRIST\nPage 6",
                        "Chorus",
                        "ON TO VICTORY! ON TO VICTORY!\n"
                        "CRIES OUR GREAT COMMANDER ON!\n"
                        "WE’LL MOVE AT HIS COMMAND,\n"
                        "WE’LL SOON POSSESS THE LAND,\n"
                        "THRO’ LOYALTY, LOYALTY,\nYES LOYALTY TO CHRIST. AMEN",
                        "Stanza-1",
                        "FROM OVER HILL AND PLAIN,\nTHERE COMES THE SIGNAL STRAIN,\n"
                        "‘TIS LOYALTY, LOYALTY,\nLOYALTY TO CHRIST;\n"
                        "IT’S MUSIC ROLLS A LONG,\nTHE HILLS TAKE UP THE SONG,\n"
                        "OF LOYALTY, LOYALTY,\nYES, LOYALTY TO CHRIST.",
                        "Stanza-2",
                        "O HEAR,YE BRAVE, THE SOUND,\nTHAT MOVE THE EARTH AROUND,\n"
                        "‘TIS LOYALTY, LOYALTY,\nLOYALTY TO CHRIST;\n"
                        "ARISE TO DARE AND DO,\nRING OUT THE WATCH-WORD TRUE,\n"
                        "OF LOYALTY, LOYALTY,\nYES, LOYALTY TO CHRIST.",
                        "Stanza-3",
                        "COME JOIN OUR LOYAL THRONE,\nWELL ROUT THE GIANT WRONG,\n"
                        "‘TIS LOYALTY, LOYALTY,\nLOYALTY TO CHRIST;\n"
                        "WHERE SATAN’S BANNERS FLOAT,\nWE’LL SEND THE BUGLE NOTE,\n"
                        "OF LOYALTY, LOYALTY,\nYES, LOYALTY TO CHRIST.",
                        "Stanza-4",
                        "THE STRENGTH OF YOUTH WE LAY,\nAT JESUS FEET TODAY,\n"
                        "‘TIS LOYALTY, LOYALTY,\nLOYALTY TO CHRIST;\n"
                        "HIS GOSPEL WELL PROCLAIM,\nTHRO’-OUT THE WORLD’S DOMAIN,\n"
                        "OF LOYALTY, LOYALTY,\nYES, LOYALTY TO CHRIST."]
        self.song_63 = ["Title",
                        "MAKE ME A BLESSING\nPage 54",
                        "Chorus",
                        "MAKE ME A BLESSING,\nMAKE ME A BLESSING,\n"
                        "OUT OF MY LIFE,\nMAY JESUS SHINE;\n"
                        "MAKE ME A BLESSING,\nO SAVIOUR I PRAY\n"
                        "MAKE ME A BLESSING,\nTO SOMEONE TODAY.",
                        "Stanza-1",
                        "OUT IN THE HIGH-WAYS\nAND BY-WAYS OF LIFE,\n"
                        "MANY ARE WEARY AND SAD,\nCARRY THE SUNSHINE\nWHERE DARKNESS IS RIFE,\n"
                        "MAKING THE SORROWING GLAD.",
                        "Stanza-2",
                        "TELL THE SWEET STORY\nOF CHRIST AND HIS LOVE,\n"
                        "TELL OF HIS POW’R TO FORGIVE,\nOTHERS WILL TRUST HIM\nIF ONLY YOU PROVE,\n"
                        "TRUE, EVERY MOMENT YOU LIVE.",
                        "Stanza-3",
                        "GIVE AS ‘TWAS GIVEN\nTO YOU IN YOUR NEED,\n"
                        "LOVE AS THE MASTER LOVED YOU,\nBE TO THE HELPLESS A HELPER INDEED,\n"
                        "UNTO YOUR MISSION BE TRUE."]
        self.song_64 = ["Title",
                        "MAKE ME A CHANNEL OF BLESSING\nPage 307",
                        "Chorus",
                        "MAKE ME A CHANNEL\nOF BLESSING TODAY,\n"
                        "MAKE ME A CHANNEL\nOF BLESSING, I PRAY;\n"
                        "MY LIFE POSSESSING,\nMY SERVICE BLESSING,\n"
                        "MAKE ME A CHANNEL\nOF BLESSING TODAY.",
                        "Stanza-1",
                        "IS YOUR LIFE A\nCHANNEL OF BLESSING?\nIS THE LOVE OF GOD\nFLOWING THRO’ YOU?\n"
                        "ARE YOU TELLING THE\nLOST OF THE SAVIOUR?\nARE YOU READY FOR\nHIS SERVICE TO DO?",
                        "Stanza-2",
                        "IS YOUR LIFE A\nCHANNEL OF BLESSING?\nARE YOU BURDENED FOR\nTHOSE THAT ARE LOST?\n"
                        "HAVE YOU URGED UP-ON\nTHOSE WHO ARE STRAYING,\nTHE SAVIOUR WHO\nDIED ON THE CROSS?",
                        "Stanza-3",
                        "IS YOUR LIFE A\nCHANNEL OF BLESSING?\nIS IT DAILY TELLING FOR HIM?\n"
                        "HAVE YOU SPOKEN\nTHE WORD OF SALVATION\nTO THOSE WHO ARE DYING IN SIN?",
                        "Stanza-4",
                        "WE CANNOT BE\nCHANNELS OF BLESSING,\nIF OUR LIVES ARE NOT\nFREE FROM KNOWN SIN;\n"
                        "WE WILL BARRIERS\nBE AND A HINDRANCE\nTO THOSE WE ARE TRYING TO WIN."]
        self.song_65 = ["Title",
                        "MANSION OVER THE HILLTOP\nPage 82",
                        "Chorus",
                        "I’VE GOT A MANSION\nJUST OVER THE HILLTOP,\n"
                        "IN THAT BRIGHT LAND WHERE\nWE’LL NEVER GROW OLD.\n"
                        "AND SOMEDAY YONDER,\nWE WILL NEVER MORE WANDER,\n"
                        "BUT WALK ON STREETS\nTHAT ARE PUREST GOLD.",
                        "Stanza-1",
                        "I’M SATISFIED WITH\nJUST A COTTAGE BELOW,\n"
                        "A LITTLE SILVER,\nAND A LITTLE GOLD.\n"
                        "BUT IN THAT CITY, WHERE\nTHE RANSOMED WILL SHINE,\n"
                        "I WANT A GOLD ONE\nTHAT’S SILVER LINED.",
                        "Stanza-2",
                        "THO’ OFTEN TEMPTED,\nTORMENTED AND TESTED\n"
                        "AND LIKE THE PROPHET,\nMY PILLOW A STONE,\n"
                        "AND THO’ I FIND HERE,\nNO PERMANENT DWELLING,\n"
                        "I KNOW HE’LL GIVE ME\nA MANSION MY OWN.",
                        "Stanza-3",
                        "DON’T THINK ME POOR OR,\nDESERTED OR LONELY\n"
                        "I’M NOT DISCOURAGED,\nI’M HEAVEN BOUND.\n"
                        "I’M JUST A PILGRIM\nIN SEARCH OF THAT CITY\n"
                        "I WANT A MANSION,\nA HARP AND A CROWN."]
        self.song_66 = ["Title",
                        "MEET ME THERE\nPage 289",
                        "Chorus",
                        "MEET ME THERE, MEET ME THERE\n"
                        "WHERE THE TREE OF LIFE IS BLOOMING,\nMEET ME THERE;\n"
                        "WHEN THE STORMS OF LIFE ARE O’ER,\nON A HAPPY GOLDEN SHORE,\n"
                        "WHERE THE FAITHFUL PART NO MORE,\nMEET ME THERE. AMEN",
                        "Stanza-1",
                        "ON THE HAPPY GOLDEN SHORE,\nWHERE THE FAITHFUL PART NO MORE,\n"
                        "WHEN THE STORMS OF LIFE ARE O’ER\nMEET ME THERE;\n"
                        "WHERE THE NIGHT DISSOLVES AWAY,\nINTO PURE AND PERFECT DAY,\n"
                        "I AM GOING HOME TO STAY,\nMEET ME THERE.",
                        "Stanza-2",
                        "HERE OUR FONDEST HOPES ARE VAIN,\nDEAREST LINKS ARE RENT IN TWAIN;\n"
                        "BUT IN HEAV’N NO THROB OF PAIN,\nMEET ME THERE;\n"
                        "BY THE RIVER SPARKLING BRIGHT,\nIN THE CITY OF DELIGHT\n"
                        "WHERE OUR FAITH LOST IN SIGHT,\nMEET ME THERE.",
                        "Stanza-3",
                        "WHERE THE HARPS OF ANGELS RING,\nAND THE BLEST FOREVER SING,\n"
                        "IN THE PALACE OF THE KING,\nMEET ME THERE;\n"
                        "WHERE IN SWEET COMMUNION BLEND,\nHEART WITH HEART AND FRIEND\nWITH FRIEND,\n"
                        "IN A WORLD THAT NE’ER SHALL,\nEND MEET ME THERE."]
        self.song_67 = ["Title",
                        "MINE EYES HAVE SEEN THE GLORY\nPage 291",
                        "Stanza-1",
                        "MINE EYES HAVE SEEN THE GLORY\nOF THE COMING OF THE LORD;\n"
                        "HE IS TRAMPLING OUT THE VINTAGE\nWHERE THE GRAPES OF WRATH ARRE STORED;\n"
                        "HE HATH LOOSED THE FAITHFUL LIGHTNING\nOF HIS TERRIBLE SWIFT SWORD;\n"
                        "HIS TRUTH IS MARCHING ON.",
                        "Chorus-1",
                        "GLORY! GLORY, HALLELUJAH!\nGLORY! GLORY, HALLELUJAH!\n"
                        "GLORY! GLORY, HALLELUJAH!\nHIS TRUTH IS MARCHING ON.",
                        "Stanza-2",
                        "I HAVE SEEN HIM IN THE WATCH-FIRES\nOF A HUNDRED CIRCLING CAMPS;\n"
                        "THEY HAVE BUILDED HIM AN ALTAR\nIN THE EVENING DEWS AND DAMPS;\n"
                        "I CAN READ HIS RIGHTEOUS SENTENCE\nBY THE DIM AND FLAIRING LAMPS;\n"
                        "HIS DAY IS MARCHING ON.",
                        "Chorus-2",
                        "GLORY! GLORY, HALLELUJAH!\nGLORY! GLORY, HALLELUJAH!\n"
                        "GLORY! GLORY, HALLELUJAH!\nHIS DAY IS MARCHING ON.",
                        "Stanza-3",
                        "HE HAS SOUNDED FORTH THE TRUMPET\nTHAT SHALL NEVER SOUND RETREAT;\n"
                        "HE IS SIFTING OUT THE HEARTS OF MEN\nBEFORE HIS JUDGEMENT SEAT.\n"
                        "O BE SWIFT, MY SOUL, TO ANSWER HIM!\nBE JUBILANT MY FEET!\n"
                        "OUR GOD IS MARCHING ON",
                        "Chorus-3",
                        "GLORY! GLORY, HALLELUJAH!\nGLORY! GLORY, HALLELUJAH!\n"
                        "GLORY! GLORY, HALLELUJAH!\nOUR GOD IS MARCHING ON.",
                        "Stanza-4",
                        "IN THE BEAUTY OF THE LILIES\nCHRIST WAS BORN ACROSS THE SEA,\n"
                        "WITH THE GLORY IN HIS BOSOM\nTHAT TRANSFIGURES YOU AND ME;\n"
                        "AS HE DIED TP MAKE MEN HOLY,\nLET US DIE TO MAKE MEN FREE;\n"
                        "WHILE GOD IS MARCHING ON.",
                        "Chorus-4",
                        "GLORY! GLORY, HALLELUJAH!\nGLORY! GLORY, HALLELUJAH!\n"
                        "GLORY! GLORY, HALLELUJAH!\nWHILE GOD IS MARCHING ON."]
        self.song_68 = ["Title",
                        "MY FATHER PLANNED IT ALL\nPage 93",
                        "Chorus",
                        "I SING THRU THE SHADE AND THE SUNSHINE,\n"
                        "I’LL TRUST HIM WHATEVER BE FALL;\n"
                        "I SING FOR I CANNOT BE SILENT,\n"
                        "MY FATHER PLANNED IT ALL.",
                        "Stanza-1",
                        "WHAT THO THE PATHWAY BE LONELY,\n"
                        "AND DARK THE SHADOWS FALL;\n"
                        "I KNOW WHERE E’ER IT LEADETH,\n"
                        "MY FATHER PLANNED IT ALL",
                        "Stanza-2",
                        "THERE MAY BE SUNSHINE TOMORROW,\n"
                        "SHADOWS MAY BREAK AND FLEE;\n"
                        "‘TWILL BE THE WAY HE CHOOSES,\n"
                        "THE FATHER’S PLANNED FOR ME.",
                        "Stanza-3",
                        "HE GUIDES MY FALTERING FOOTSTEPS,\n"
                        "A LONG THE WEARY WAY,\n"
                        "FOR WELL HE KNOWS THE PATHWAY,\n"
                        "WILL LEAD TO ENDLESS DAY."]
        self.song_69 = ["Title",
                        "MY SAVIOR FIRST OF ALL\nPage 283",
                        "Chorus",
                        "I SHALL KNOW HIM, I SHALL KNOW HIM\n"
                        "AND REDEEMED BY HIS SIDE I SHALL STAND,\n"
                        "I SHALL KNOW HIM, I SHALL KNOW HIM\n"
                        "BY THE PRINT OF THE NAILS IN HIS HAND.",
                        "Stanza-1",
                        "WHEN MY LIFE-WORK IS ENDED,\nAND I CROSS THE SWELLING TIDE,\n"
                        "WHEN THE BRIGHT AND GLORIOUS\nMORNING I SHALL SEE;\n"
                        "I SHALL KNOW MY REDEEMER\nWHEN I REACH THE OTHER SIDE.\n"
                        "AND HIS SMILE WILL BE\nTHE FIRST TO WELCOME ME.",
                        "Stanza-2",
                        "OH THE SOUL THRILLING RAPTURE\nWHEN I VIEW HIS BLESSED FACE,\n"
                        "AND THE LUSTER OF HIS\nKINDLY BEAMING EYE;\n"
                        "HOW MY FULL HEART WILL PRAISE HIM\nFOR THE MERCY, LOVE, AND GRACE.\n"
                        "THAT PREPARE FOR ME\nA MANSION IN THE SKY.",
                        "Stanza-3",
                        "OH THE DEAR ONES IN GLORY,\nHOW THEY BECKON ME TO COME,\n"
                        "AND OUR PARTING AT THE RIVER I RECALL;\n"
                        "TO THE SWEET VALES OF EDEN\nTHEY WILL SING A WELCOME HOME;\n"
                        "BUT I LONG TO MEET\nMY SAVIOR FIRST OF ALL.",
                        "Stanza-4",
                        "THRO’ THE GATES TO THE CITY\nIN A ROBE OF SPOTLESS WHITE,\n"
                        "HE WILL LEAD ME WHERE NO\nTEARS WILL EVER FALL;\n"
                        "IN THE GLAD SONG OF AGES\nI SHALL MINGLE WITH DELIGHT;\n"
                        "BUT I LONG TO MEET\nMY SAVIOR FIRST OF ALL."]
        self.song_70 = ["Title",
                        "MY SAVIOR’S LOVE\nPage 70",
                        "Chorus",
                        "HOW MARVELOUS! HOW WONDERFUL!\nAND MY SONG SHALL EVER BE;\n"
                        "HOW MARVELOUS! HOW WONDERFUL!\nIS MY SAVIOR’S LOVE FOR ME!",
                        "Stanza-1",
                        "I STAND AMAZED IN THE PRESENCE\nOF JESUS THE NAZARENE,\n"
                        "AND WONDER HOW HE COULD LOVE ME,\nA SINNER, CONDEMNED, UNCLEAN.",
                        "Stanza-2",
                        "FOR ME IT WAS IN THE GARDEN,\nHE PRAYED: “NOT MY WILL BUT THINE;”\n"
                        "HE HAD NO TEARS FOR HIS OWN GRIEFS,\nBUT SWEET DROPS OF BLOOD FOR MINE.",
                        "Stanza-3",
                        "IN PITY ANGELS BEHELD HIM,\nAND CAME FROM THE WORLD OF LIGHT\n"
                        "TO COMFORT HIM IN THE SORROWS,\nHE BORE FOR MY SOUL THAT NIGHT.",
                        "Stanza-4",
                        "HE TOOK MY SINS AND MY SORROWS,\nHE MADE THEM HIS VERY OWN;\n"
                        "HE BORE THE BURDEN TO CALV’RY,\nAND SUFFERED, AND DIED ALONE.",
                        "Stanza-5",
                        "WHEN WITH THE RANSOMED IN GLORY\nHIS FACE I AT LAST SHALL SEE,\n"
                        "‘TWILL BE THE JOY THRO’ THE AGES\nTO SING OF HIS LOVE FOR ME."]
        self.song_71 = ["Title",
                        "MY SINS ARE GONE\nPage 23",
                        "Chorus",
                        "THEY’RE UNDERNEAT THE BLOOD,\nON THE CROSS OF CALVARY\n"
                        "AS FAR REMOVED AS DARKNESS\nIS FROM DAWN;\n"
                        "IN THE SEA OF GOD’S FORGETFULNESS,\nTHAT’S GOOD ENOUGH FOR ME\n"
                        "PRAISE GOD, MY SINS ARE GONE.",
                        "Stanza-1",
                        "YOU ASK WHY I AM HAPPY\nSO I’LL JUST TELL YOU WHY,\nBECAUSE MY SINS ARE GONE;\n"
                        "AND WHEN I MEET THE SCOFFERS\nWHO ASK ME WHERE THEY ARE,\nI SAY MY SINS ARE GONE.",
                        "Stanza-2",
                        "‘TWAS AT THE OLD TIME ALTAR\nWHERE GOD CAME IN MY HEART,\nAND NOW MY SINS ARE GONE;\n"
                        "THE LORD TOOK FULL POSSESSION,\nTHE DEVIL DID DEPART,\nI’M GLAD MY SINS ARE GONE.",
                        "Stanza-3",
                        "WHEN SATAN COMES TO TEMPT ME\nAND TRIES TO MAKE ME DOUBT,\nI SAY MY SINS ARE GONE;\n"
                        "YOU GOT ME INTO TROUBLE,\nBUT JESUS GOT ME OUT,\nI’M GLAD MY SINS ARE GONE.",
                        "Stanza-4",
                        "‘TWAS AT THE OLD TIME ALTAR\nWHERE GOD CAME IN MY HEART,\nAND NOW MY SINS ARE GONE;\n"
                        "THE LORD TOOK FULL POSSESSION,\nTHE DEVIL DID DEPART,\nI’M GLAD MY SINS ARE GONE."]
        self.song_72 = ["Title",
                        "NEAR THE CROSS\nPage 150",
                        "Chorus",
                        "IN THE CROSS, IN THE CROSS,\nBE MY GLORY EVER;\n"
                        "TILL MY RAPTURED SOUL, SHALL FIND\nREST BEYOND THE RIVER.",
                        "Stanza-1",
                        "JESUS KEEP ME NEAR THE CROSS,\nTHERE A PRECIOUS FOUNTAIN\n"
                        "FREE TO ALL A HEALING SCREAM,\nFLOWS FROM CALV’RY’S MOUNTAIN.",
                        "Stanza-2",
                        "NEAR THE CROSS, A TREMBILNG SOUL,\nLOVE AND MERCY FOUND ME;\n"
                        "THERE THE BRIGHT AND MORNING STAR,\nSHEDS IT’S BEAMS AROUND ME.",
                        "Stanza-3",
                        "NEAR THE CROSS, O LAMB OF GOD,\nBRING ITS SCENES BEFORE ME;\n"
                        "HELP ME WORK FROM DAY TO DAY,\nWITH ITS SHADOWS O’ER ME.",
                        "Stanza-4",
                        "NEAR THE CROSS, I’LL WATCH AND WAIT,\nHOPING, TRUSTING EVER,\n"
                        "TILL I REACH THE GOLDEN STRAND,\nJUST BEYOND THE RIVER."]
        self.song_73 = ["Title",
                        "NOTHING BUT THE BLOOD\nPage 132",
                        "Chorus",
                        "OH! PRECIOOUS IS THE FLOW\nTHAT MAKES ME WHITE AS SNOW;\n"
                        "NO OTHER FOUNT I KNOW,\nNOTHING BUT THE BLOOD OF JESUS.",
                        "Stanza-1",
                        "WHAT CAN WASH AWAY MY SIN?\nNOTHING BUT THE BLOOD OF JESUS;\n"
                        "WHAT CAN MAKE ME WHOLE AGAIN?\nNOTHING BUT THE BLOOD OF JESUS.",
                        "Stanza-2",
                        "FOR MY PARDON THIS I SEE,\nNOTHING BUT THE BLOOD OF JESUS;\n"
                        "FOR MY CLEANSING, THIS MY PLEA,\nNOTHING BUT THE BLOOD OF JESUS.",
                        "Stanza-3",
                        "NOTHING CAN FOR SIN ATONE,\nNOTHING BUT THE BLOOD OF JESUS;\n"
                        "NAUGHT OF GOOD THAT I HAVE DONE,\nNOTHING BUT THE BLOOD OF JESUS.",
                        "Stanza-4",
                        "THIS IS ALL MY HOPE AND PEACE,\nNOTHING BUT THE BLOOD OF JESUS;\n"
                        "THIS IS ALL MY RIGHTEOUSNESS,\nNOTHING BUT THE BLOOD OF JESUS."]
        self.song_74 = ["Title",
                        "NOW I BELONG TO JESUS\nPage 98",
                        "Chorus",
                        "NOW I BELONG TO JESUS,\nJESUS BELONGS TO ME.\n"
                        "NOT FOR THE YEARS OF TIME ALONE,\nBUT FOR ETERNITY.",
                        "Stanza-1",
                        "JESUS MY LORD WILL LOVE ME FOREVER,\nFROM HIM NO POW’R OF EVIL CAN SEVER,\n"
                        "HE GAVE HIS LIFE TO RANSOM MY SOUL,\nNOW I BELONG TO HIM:",
                        "Stanza-2",
                        "ONCE I WAS LOST IN SIN’S DEGRADATION,\nJESUS CAME DOWN TO BRING ME SALVATION,\n"
                        "LIFTED ME UP FROM SORROW AND SHAME,\nNOW I BELONG TO HIM:",
                        "Stanza-3",
                        "JOY FLOODS MY SOUL\nFOR JESUS HAS SAVED ME,\nFREED ME FROM SIN\nTHAT LONG HAD ENSLAVED ME,\n"
                        "HIS PRECIOUS BLOOD\nHE GAVE TO REDEEM,\nNOW I BELONG TO HIM."]
        self.song_75 = ["Title",
                        "OH, HOW I LOVE JESUS\nPage 229",
                        "Chorus",
                        "OH, HOW I LOVE JESUS,\nOH, HOW I LOVE JESUS,\n"
                        "OH, HOW I LOVE JESUS,\nBECAUSE HE FIRST LOVED ME!",
                        "Stanza-1",
                        "THERE IS A NAME I LOVE TO HEAR,\nI LOVE TO SING ITS WORTH;\n"
                        "ITS SOUNDS LIKE MUSIC IN MINE EAR,\nTHE SWEETEST NAME ON EARTH.",
                        "Stanza-2",
                        "IT TELLS ME OF A SAVIOR’S LOVE,\nWHO DIED TO SET ME FREE;\n"
                        "IT TELLS ME OF HIS PRECIOUS BLOOD,\nTHE SINNER’S PERFECT PLEA.",
                        "Stanza-3",
                        "IT TELLS ME WHAT MY FATHER HATH,\nIN STORE FOR EVERY DAY,\n"
                        "AND THO’ I TREAD A DARKSOME PATH,\nYIELDS SUNSHINE ALL THE WAY.",
                        "Stanza-4",
                        "IT TELLS OF ONE WHOSE LOVING HEART,\nCAN FEEL MY DEEPEST WOE,\n"
                        "WHO IN EACH SORROW BEARS A PART,\nTHAT NONE CAN BEAR BELOW."]
        self.song_76 = ["Title",
                        "ONE DAY\nPage 14",
                        "Chorus",
                        "LIVING, HE LOVED ME, HE SAVED ME,\nBURIED, HE CARIED MY SINS FAR AWAY\n"
                        "RISING, HE JUSTIFIED FREELY FOREVER:\nONE DAY HE’S COMING"
                        "OH, GLORIOUS DAY",
                        "Stanza-1",
                        "ONE DAY WHEN HEAVEN\nWAS FILLED WITH HIS PRAISES,\n"
                        "ONE DAY WHEN SIN WAS\nAS BLACK AS COULD BE,\n"
                        "JESUS CAME FORTH TO\nBE BORN OF A VIRGIN,\n"
                        "DWELT AMONGST MEN,\nMY EXAMPLE IS HE!",
                        "Stanza-2",
                        "ONE DAY THEY LED HIM\nUP CALVARY’S MOUNTAIN,\n"
                        "ONE DAY THEY NAILED HIM\nTO DIE ON THE TREE\n"
                        "SUFFERING ANGUISH,\nDESPISED AND REJECTED:\n"
                        "BEARING OUR SINS,\nMY REDEEMER IS HE!",
                        "Stanza-3",
                        "ONE DAY THEY LEFT HIM\nALONE IN THE GARDEN,\n"
                        "ONE DAY HE RESTED,\nFROM SUFFERING FREE,\n"
                        "ANGELS CAME DOWN O’ER\nHIS TOMB TO KEEP VIGIL;\n"
                        "HOPE OF HOPELESS,\nMY SAVIOR IS HE!",
                        "Stanza-4",
                        "ONE DAY THE GRAVE COULD\nCONCEAL HIM NO LONGER,\n"
                        "ONE DAY THE STONE ROLLED\nAWAY FROM THE DOOR,\n"
                        "THEN HE AROSE, OVER\nDEATH HE HAD CONQUERED;\n"
                        "NOW IS ASCENDED,\nMY LORD EVERMORE!",
                        "Stanza-5",
                        "ONE DAY THE TRUMPET\nWILL SOUND FOR HIS COMING,\n"
                        "ONE DAY THE SKIES WITH\nHIS GLORIES WILL SHINE;\n"
                        "WONDERFUL DAY, MY\nBELOVED ONES BRINGING;\n"
                        "GLORIOUS SAVIOR,\nTHIS JESUS IS MINE!"]
        self.song_77 = ["Title",
                        "ONWARD CHRISTIAN SOLDIERS\nPage 201",
                        "Chorus",
                        "ONWARD CHRISTIAN SOLDIERS!\nMARCHING AS TO WAR,\n"
                        "WITH THE CROSS OF JESUS\nGOING ON BEFORE.",
                        "Stanza-1",
                        "ONWARD CHRISTIAN SOLDIERS!\nMARCHING AS TO WAR,\n"
                        "WITH THE CROSS OF JESUS\nGOING ON BEFORE,\n"
                        "CHRIST THE ROYAL MASTER,\nLEADS AGAINST THE FOE\n"
                        "FORWARD INTO BATTLE,\nSEE HIS BANNERS GO!",
                        "Stanza-2",
                        "LIKE A MIGHTY ARMY,\nMOVES THE CHURCH OF GOD.\n"
                        "BROTHERS WE ARE TREADING,\nWHERE THE SAINTS HAVE THROD.\n"
                        "WE ARE NOT DIVIDED;\nALL ONE BODY WE:\n"
                        "ONE IN HOPE AND DOCTRINE,\nONE IN CHARITY.",
                        "Stanza-3",
                        "CROWNS AND THRONES MAY PERISH,\nKINGDOM RISE AND WANE;\n"
                        "BUT THE CHURCH OF JESUS,\nCONSTANT WILL REMAIN.\n"
                        "GATES OF HELL CAN NEVER,\n‘GAINST THAT CHURCH PREVAIL;\n"
                        "WE HAVE CHRIST OWN PROMISE,\nWHICH CAN NEVER FAIL.",
                        "Stanza-4",
                        "ONWARD THEN YE PEOPLE,\nJOIN OUR HAPPY THRONG;\n"
                        "BLEND WITH OURS YOUR VOICES,\nIN THE TRIUMPH SONG,\n"
                        "GLORY, LAUD AND HONOR,\nUNTO CHRIST THE KING;\n"
                        "THIS THRO’ COUNTLESS AGES,\nMEN AND ANGELS SING."]
        self.song_78 = ["Title",
                        "OPEN MY EYES, THAT I MAY SEE\nPage 192",
                        "Stanza-1",
                        "OPEN MY EYES, THAT I MAY SEE,\nGLIMPES OF TRUTH THOU HAST FOR ME;\n"
                        "PLACE IN MY HANDS THE WONDERFUL KEY,\nTHAT SHALL UN-CLASP, AND SET ME FREE.\n"
                        "SILENTLY NOW I WAIT FOR THEE,\nREADY, MY GOD, THY WILL TO SEE;\n"
                        "OPEN MY EYES, ILLUMINE ME,\nSPIRIT DIVINE!",
                        "Stanza-2",
                        "OPEN MY EARS, THAT I MAY HEAR,\nVOICES OF TRUTH THOU SENDEST CLEAR;\n"
                        "AND WHILE THE WAVE-NOTES\nFALL ON MY EAR,\nEVERYTHING FALSE WILL DISAPPER.\n"
                        "SILENTLY NOW I WAIT FOR THEE,\nREADY, MY GOD, THY WILL TO SEE;\n"
                        "OPEN MY EYES, ILLUMINE ME,\nSPIRIT DIVINE!",
                        "Stanza-3",
                        "OPEN MY MOUTH, AND LET ME BEAR,\nGLADLY THE WARM TRUTH EVERYWHERE;\n"
                        "OPEN MY HEART, AND LET ME PREPARE,\nLOVE WITH THY CHILDREN THUS TO SHARE.\n"
                        "SILENTLY NOW I WAIT FOR THEE,\nREADY, MY GOD, THY WILL TO SEE;\n"
                        "OPEN MY EYES, ILLUMINE ME,\nSPIRIT DIVINE!"]
        self.song_79 = ["Title",
                        "OUR BEST\nPage 149",
                        "Chorus",
                        "EVERY WORK FOR JESUS WILL BE BLEST,\nBUT HE ASKS FROM EVERY ONE HIS BEST.\n"
                        "OUR TALENTS MAY BE FEW,\nTHESE MAY BE SMALL,\n"
                        "BUT UNTO HIM IS DUE\nOUR BEST OUR ALL.",
                        "Stanza-1",
                        "HEAR YE THE MASTER’S CALL,\n“GIVE ME THY BEST!”\n"
                        "FOR BE IT GREAT OR SMALL,\nTHAT IS HIS TEST.\n"
                        "DO THEN THE BEST YOU CAN,\nNOT FOR REWARD,\n"
                        "NOT FOR THE PRAISE OF MAN,\nBUT FOR THE LORD.",
                        "Stanza-2",
                        "WAIT NOT FOR MEN TO LAUD,\nHEED NOT THEIR SLIGHT;\n"
                        "WINNING THE SMILE OF GOD,\nBRINGS ITS DELIGHT!\n"
                        "AIDING THE GOOD AND TRUE,\nNE’ER GOES UNBLEST.\n"
                        "ALL THAT WE THINK OR DO,\nBE IT THE BEST.",
                        "Stanza-3",
                        "NIGHT SOON COMES ON A PACE,\nDAY HASTENS BY;\n"
                        "WORKMAN AND WORK MUST FACE,\nTESTING ON HIGH.\n"
                        "OH MAY WE IN THAT DAY,\nFIND REST, SWEET REST\n"
                        "WHICH GOD HAS PROMISED THOSE\nWHO DO THEIR BEST."]
        self.song_80 = ["Title",
                        "PASS ME NOT\nPage 202",
                        "Chorus",
                        "SAVIOUR, SAVIOUR, HEAR MY HUMBLE CRY;\n"
                        "WHILE ON OTHERS THOU ART CALLING\n"
                        "DO NOT PASS ME BY",
                        "Stanza-1",
                        "PASS ME NOT O GENTLE SAVIOUR,\n"
                        "HEAR MY HUMBLE CRY;\n"
                        "WHILE ON OTHERS THOU ART CALLING,\n"
                        "DO NOT PASS ME BY.",
                        "Stanza-2",
                        "LET ME AT A THRONE OF MERCY\n"
                        "FIND A SWEET RELIEF;\n"
                        "KNEELING THERE IN DEEP CONTRITION,\n"
                        "HELP MY UN BELIEF.",
                        "Stanza-3",
                        "TRUSTING ONLY IN THY MERIT,\n"
                        "WOULD I SEEK THY FACE;\n"
                        "HEAL MY WOUNDED BROKEN SPIRIT,\n"
                        "SAVE ME BY THY GRACE.",
                        "Stanza-4",
                        "THOU THE SPRING OF ALL MY COMFORT,\n"
                        "MORE THAN LIFE TO ME,\n"
                        "WHOM HAVE I ON EARTH BESIDE THEE?\n"
                        "WHOM IN HEAV'N BUT THEE."]
        self.song_81 = ["Title",
                        "PRAISE HIM! PRAISE HIM!\nPage 50",
                        "Chorus",
                        "PRAISE HIM! PRAISE HIM!\n"
                        "TELL OF HIS EXCELLENT GREATNESS:\n"
                        "PRAISE HIM! PRAISE HIM!\n"
                        "EVER IN JOYFUL SONG!",
                        "Stanza-1",
                        "PRAISE HIM! PRAISE HIM!\n"
                        "JESUS OUR BLESSED REDEEMER!\n"
                        "SING, O EARTH HIS\nWONDERFUL LOVE PROCLAIM!\n"
                        "HAIL HIM! HAIL HIM!\nHIGHEST ARCHANGELS IN GLORY;\n"
                        "STRENGTH AND HONOR\nGIVE TO HIS HOLY NAME!\n"
                        "LIKE A SHEPHERD,\nJESUS WILL GUARD HIL CHILDREN,\n"
                        "IN HIS ARMS HE CARRIES\nTHEM ALL DAY LONG:",
                        "Stanza-2",
                        "PRAISE HIM! PRAISE HIM!\n"
                        "JESUS OUR BLESSED REDEEMER!\n"
                        "FOR OUR SINS HE\nSUFFERED, AND BLED, AND DIED;\n"
                        "HE OUR ROCK, OUR\nHOPE OF ETERNAL SALVATION,\n"
                        "HAIL HIM! HAIL HIM!\nJESUS THE CRUCIFIED.\n"
                        "SOUND HIS PRAISES!\nJESUS WHO BORE OUR SORROWS,\n"
                        "LOVE UNBOUNDED,\nWONDERFUL, DEEP AND STRONG:",
                        "Stanza-3",
                        "PRAISE HIM! PRAISE HIM!\n"
                        "JESUS OUR BLESSED REDEEMER!\n"
                        "HEAVENLY PORTALS\nLOUD WITH HOSANAS RING!\n"
                        "JESUS, SAVIOUR,\nREIGNETH FOREVER AND EVER;\n"
                        "CROWN HIM! CROWN HIM!\nPROPHET, PRIEST AND KING!\n"
                        "CHRIST IS COMING!\nOVER THE WORLD VICTORIOUS,\n"
                        "POWER AND GLORY\nUNTO THE LORD BELONG:"]
        self.song_82 = ["Title",
                        "REDEEMED\nPage 76",
                        "Chorus",
                        "REDEEMED, REDEEMED,\n"
                        "REDEEMED BY THE BLOOD OF THE LAMB;\n"
                        "REDEEMED, REDEEMED,\n"
                        "HIS CHILD, AND FOREVER I AM.",
                        "Stanza-1",
                        "REDEEMED HOW I LOVE TO PROCLAIM IT!\n"
                        "REDEEMED BY THE BLOOD OF THE LAMB;\n"
                        "REDEEMED THRO' HIS INFINITE MERCY,\n"
                        "HIS CHILD, AND FOR EVER I AM.",
                        "Stanza-2",
                        "REDEEMED AND SO HAPPY IN JESUS,\n"
                        "NO LANGUAGE MY RAPTURE CAN TELL;\n"
                        "I KNOW THAT THE LIGHT OF HIS PRESENCE\n"
                        "WITH ME DOTH CONTINUALLY DWELL.",
                        "Stanza-3",
                        "I THINK OF MY BLESSED REDEEMER,\n"
                        "I THINK OF HIM ALL THE DAY LONG;\n"
                        "I SING, FOR I CANNOT BE SILENT;\n"
                        "HIS LOVE IS THE THEME OF MY SONG.",
                        "Stanza-4",
                        "I KNOW I SHALL SEE IN HIS BEAUTY\n"
                        "THE KING IN WHOSE LAW I DELIGHT;\n"
                        "WHO LOVINGLY, GUARDETH MY FOOTSTEPS,\n"
                        "AND GIVETH ME SONGS IN THE NIGHT."]
        self.song_83 = ["Title",
                        "RESCUE THE PERISHING\nPage 68",
                        "Chorus",
                        "RESCUE THE PERISHING,\n"
                        "CARE FOR THE DYING;\n"
                        "JESUS IS MERCIFUL,\n"
                        "JESUS WILL SAVE.",
                        "Stanza-1",
                        "RESCUE THE PERISHING,\n"
                        "CARE FOR THE DYING,\n"
                        "SNATCH THEM IN PITY\nFROM SIN AND THE GRAVE;\n"
                        "WEEP O'ER THE ERRING ONE,\n"
                        "LIFT UP THE FALLEN,\n"
                        "TELL THEM OF JESUS\nTHE MIGHTY TO SAVE.",
                        "Stanza-2",
                        "THO' THEY ARE SLIGHTING HIM,\n"
                        "STILL HE IS WAITING,\n"
                        "WAITING THE PENITENT\nCHILD TO RECEIVE;\n"
                        "PLEAD WITH THEM EARNESTLY,\n"
                        "PLEAD WITH THEM GENTLY,\n"
                        "HE WILL FORGIVE\nIF THEY ONLY BELIEVE.",
                        "Stanza-3",
                        "DOWN IN THE HUMAN HEART,\n"
                        "CRUSHED BY THE TEMPTER,\n"
                        "FEELINGS LIE BURIED\nTHAT GRACE CAN RESTORE;\n"
                        "TOUCHED BY A LOVING HEART\n"
                        "WAKEND BY KINDNESS,\n"
                        "CHORDS THAT ARE BROKEN,\n"
                        "WILL VIBRATE ONCE MORE",
                        "Stanza-4",
                        "RESCUE THE PERISHING,\n"
                        "DUTY DEMANDS IT;\n"
                        "STRENGTH FOR THY LABOR\nTHE LORD WILL PROVIDE;\n"
                        "BACK TO THE NARROW WAY\n"
                        "PATIENTLY WIN THEM;\n"
                        "TELL THE POOR WANDERER\n"
                        "A SAVIOR HAS DIED."]
        self.song_84 = ["Title",
                        "REVIVE US AGAIN\nPage 90",
                        "Chorus",
                        "HALLELUJAH! THINE THE GLORY,\n"
                        "HALLELUJAH! AMEN;\n"
                        "HALLELUJAH! THINE THE GLORY,\n"
                        "REVIVE US AGAIN.",
                        "Stanza-1",
                        "WE PRAISE THEE, O GOD!\n"
                        "FOR THE SON OF THY LOVE,\n"
                        "FOR JESUS WHO DIED,\n"
                        "AND IS NOW GONE ABOVE.",
                        "Stanza-2",
                        "WE PRAISE THEE, O GOD!\n"
                        "FOR THY SPIRIT OF LIGHT,\n"
                        "WHO HAS SHOWN US OUR SAVIOUR,\n"
                        "AND SCATTERED OUR NIGHT.",
                        "Stanza-3",
                        "ALL GLORY AND PRAISE\n"
                        "TO THE LAMB THAT WAS SLAIN,\n"
                        "WHO HAS BOURNE ALL OUR SINS,\n"
                        "AND HATH CLEANSED EVERY STAIN.",
                        "Stanza-4",
                        "REVIVE US AGAIN;\n"
                        "FILL EACH HEART WITH THY LOVE;\n"
                        "MAY EACH SOUL BE REKINDLED\n"
                        "WITH FIRE FROM ABOVE."]
        self.song_85 = ["Title",
                        "ROCK OF AGES\nPage 109",
                        "Stanza-1",
                        "ROCK OF AGES, CLEFT FOR ME,\n"
                        "LET ME HIDE MYSELF IN THEE;\n"
                        "LET THE WATER AND THE BLOOD,\n"
                        "FROM THY WOUNDED SIDE WHICH FLOWED,\n"
                        "BE OF SIN THE DOUBLE CURE,\n"
                        "SAVE FROM WRATH AND MAKE ME PURE.",
                        "Stanza-2",
                        "COULD MY TEARS FOREVER FLOW,\n"
                        "COULD MY SEAL NO LANGOUR KNOW,\n"
                        "THESE FOR SIN COULD NOT ATONE;\n"
                        "THOU MUST SAVE, AND THOU ALONE;\n"
                        "IN MY HAND NO PRICE I BRING,\n"
                        "SIMPLY TO THY CROSS I CLING.",
                        "Stanza-3",
                        "WHILE I DRAW THIS FLEETING DEATH,\n"
                        "WHEN MY EYES SHALL CLOSE IN DEATH,\n"
                        "WHEN I RISE TO WORDLS UNKNOWN,\n"
                        "AND BEHOLD THEE ON THY THRONE,\n"
                        "ROCK OF AGES CLEFT FOR ME,\n"
                        "LET ME HIDE MYSELF IN THEE."]
        self.song_86 = ["Title",
                        "SAVED, SAVED!\nPage 17",
                        "Chorus",
                        "SAVED BY HIS POWER DIVINE,\n"
                        "SAVED TO NEW LIFE SUBLIME!\n"
                        "LIFE NOW IS SWEET\n"
                        "AND MY JOY IS COMPLETE,\n"
                        "FOR I'M SAVED, SAVED, SAVED!",
                        "Stanza-1",
                        "I'VE FOUND A FRIEND\n"
                        "WHO IS ALL TO ME,\n"
                        "HIS LOVE IS EVER TRUE...\n"
                        "I LOVE TO TELL\n"
                        "HOW HE LIFTED ME\n"
                        "AND WHAT HIS GRACE\n"
                        "CAN DO FOR YOU...",
                        "Stanza-2",
                        "HE SAVES ME FROM\nEVERY SIN AND HARM\n"
                        "SECURES MY SOUL EACH DAY...\n"
                        "I'M LEANING STRONG\nON HIS MIGHTY ARM;\n"
                        "I KNOW HE'LL GUIDE ME\nALL THE WAY...",
                        "Stanza-3",
                        "WHEN POOR AND NEEDY\n"
                        "AND ALL ALONE,\n"
                        "IN LOVE HE SAID TO ME...\n"
                        "COME UNTO ME\n"
                        "AND I'LL LEAD YOU HOME,\n"
                        "TO LIVE WITH ME ETERNALLY..."]
        self.song_87 = ["Title",
                        "SAVED THROUGH JESUS' BLOOD\nPage 200",
                        "Chorus",
                        "I'LL BE PRESENT\nWHEN THE ROLL IS CALLED,\n"
                        "PURE AND SPOTLESS\nTHRO' THE CRIMSON FLOOD;\n"
                        "I WILL ANSWER WHEN\nTHEY CALL MY NAME;\n"
                        "SAVED THRO' JESUS' BLOOD.",
                        "Stanza-1",
                        "SOMETIME WE'LL STAND\nBEFORE THE JUDGEMENT BAR\n"
                        "THE QUICK, THE RISEN DEAD;\n"
                        "THE LORD WILL THEN\nMAKE KNOWN THE RECORED THERE;\n"
                        "OUR NAMES WILL ALL BE READ.",
                        "Stanza-2",
                        "I'LL THEN RECEIVE\nA BRIGHT AND STARY CROWN,\n"
                        "AS ONLY GOD CAN GIVE;\n"
                        "AND WHEN I'VE BEEN\nWITH HIM TEN THOUSAND YEARS\n"
                        "I'LL HAVE NO LESS TO LIVE.",
                        "Stanza-3",
                        "THEN WE SHALL MEET\nTO NEVER PART AGAIN\n"
                        "OUR TOIL WILL THEN BE O'ER;\n"
                        "WE'LL LAY OUR BURDENS\nDOWN AT JESUS FEET\n"
                        "AND REST FOREVER MORE."]
        self.song_88 = ["Title",
                        "SAVIOUR, LIKE A SHEPHERD LEAD US\nPage 304",
                        "Stanza-1",
                        "SAVIOR LIKE A SHEPHERD LEAD US,\n"
                        "MUCH WE NEED THY TENDER CARE;\n"
                        "IN THY PLEASANT PASTURES FEED US,\n"
                        "FOR OUR USE THY FOLDS PREPARE:",
                        "Chorus-1",
                        "BLESSED JESUS, BLESSED JESUS,\n"
                        "THOU HAST BROUGHT US, THINE WE ARE (2X)",
                        "Stanza-2",
                        "WE ARE THINE; DO THOU BE FRIEND US;\n"
                        "BE THE GUARDIAN OF OUR WAY;\n"
                        "KEEP THY FLOCK, FROM SIN DEFEND US,\n"
                        "SEEK US WHEN WE GO ASTRAY;",
                        "Chorus-2",
                        "BLESSED JESUS, BLESSED JESUS,\n"
                        "HEAR, O HEAR US WHEN WE PRAY; (2X)",
                        "Stanza-3",
                        "THOU HAS PROMISED TO RECEIVE US,\n"
                        "POOR AND SINFUL THOUGH WE BE;\n"
                        "THOU HAST MERCY TO RELIEVE US,\n"
                        "GRACE TO CLEANSE, AND POWER TO FREE;",
                        "Chorus-3",
                        "BLESSED JESUS, BLESSED JESUS,\n"
                        "EARLY LET US TURN TO THEE; (2X)",
                        "Stanza-4",
                        "EARLY LET US SEEK THY FAVOR;\n"
                        "EARLY LET US DO THY WILL;\n"
                        "BLESSED LORD AND ONLY SAVIOUR,\n"
                        "WITH THY LOVE OUR BOSOMS FILL;",
                        "Chorus-4",
                        "BLESSED JESUS, BLESSED JESUS,\n"
                        "THOU HAST LOVE US, LOVE US STILL; (2X)"]
        self.song_89 = ["Title",
                        "SEND THE LIGHT\nPage 28",
                        "Chorus",
                        "SEND THE LIGHT!\nTHE BLESSED GOSPEL LIGHT;\n"
                        "LET IT SHINE FROM SHORE TO SHORE!\n"
                        "SEND THE LIGHT!\nTHE BLESSED GOSPEL LIGHT;\n"
                        "LET IT SHINE FOREVERMORE.",
                        "Stanza-1",
                        "THERES A CALL COMES RINGING\n"
                        "O'ER THE RESTLESS WAVE,\n"
                        "SEND THE LIGHT! SEND THE LIGHT!\n"
                        "THERE ARE SOULS TO RESCUE,\n"
                        "THERE  ARE SOULS TO SAVE,\n"
                        "SEND THE LIGHT! SEND THE LIGHT!",
                        "Stanza-2",
                        "WE HAVE HEARD THE\n"
                        "MACEDONIAN CALL TO DAY,\n"
                        "SEND THE LIGHT! SEND THE LIGHT!\n"
                        "AND THE GOLDEN OFFERING\n"
                        "AT THE CROSS WE LAY,\n"
                        "SEND THE LIGHT! SEND THE LIGHT!",
                        "Stanza-3",
                        "LET US PRAY THAT GRACE\n"
                        "MAY EVERYWHERE ABOUND;\n"
                        "SEND THE LIGHT! SEND THE LIGHT!\n"
                        "AND A CHRIST LIKE SPIRIT\n"
                        "EVERYWHERE BE FOUND,\n"
                        "SEND THE LIGHT! SEND THE LIGHT!",
                        "Stanza-4",
                        "LET US NOT GROW WEARY\n"
                        "IN THE WORK OF LOVE,\n"
                        "SEND THE LIGHT! SEND THE LIGHT!\n"
                        "LET US GATHER JEWELS\n"
                        "FOR A CROWN ABOVE,\n"
                        "SEND THE LIGHT! SEND THE LIGHT!"]
        self.song_90 = ["Title",
                        "SHALL WE GATHER AT THE RIVER\nPage 103",
                        "Chorus",
                        "YES WE'LL GATHER AT THE RIVER,\n"
                        "THE BEAUTIFUL, THE BEAUTIFUL RIVER;\n"
                        "GATHER WITH THE SAINTS ATE THE RIVER\n"
                        "THAT FLOWS BY THE THRONE OF GOD.",
                        'Stanza-1',
                        "SHALL WE GATHER AT THE RIVER,\n"
                        "WHERE BRIGHT ANGEL FEET HAVE TROD;\n"
                        "WITH ITS CRYSTAL TIDE FOREVER,\n"
                        "FLOWING BY THE THRONE OF GOD.",
                        "Stanza-2",
                        "ON THE MARGIN OF THE RIVER,\n"
                        "WASHING UP IT SILVER SPRAY,\n"
                        "WE WILL WALK AND WORSHIP EVER,\n"
                        "ALL THE HAPPY GOLDEN DAY",
                        "Stanza-3",
                        "ERE WE REACH THE SHINNING RIVER,\n"
                        "LAY WE EVE BURDEN DOWN;\n"
                        "GRACE OUR SPIRITS WILL DELIVER,\n"
                        "AND PROVIDE A ROBE AND CROWN.",
                        "Stanza-4",
                        "SOON WE'LL REACH THE SHINNING RIVER,\n"
                        "SOON OUR PILGRIMAGE WILL CEASE,\n"
                        "SOON OUR HAPPY HEARTS WILL QUIVER\n"
                        "WITH THE MELODY OF PEACE."]
        self.song_91 = ["Title",
                        "SINCE JESUS CAME INTO MY HEART\nPage 33",
                        "Chorus",
                        "SINCE JESUS CAME INTO MY HEART,\n"
                        "SINCE JESUS CAME INTO MY HEART;\n"
                        "FLOODS OF JOY O'ER MY SOUL\n"
                        "LIKE THE SEA BILLOWS ROLL,\n"
                        "SINCE JESUS CAME INTO MY HEART.",
                        "Stanza-1",
                        "WHAT A WONDERFUL CHANGE\n"
                        "IN MY LIFE HAS BEEN WROUGHT\n"
                        "SINCE JESUS CAME INTO MY HEART,\n"
                        "I HAVE LIGHT IN MY SOUL\n"
                        "FOR WHICH LONG I HAVE SOUGHT\n"
                        "SINCE JESUS CAME INTO MY HEART",
                        "Stanza-2",
                        "I HAVE CEASED FROM MY WANDRING\n"
                        "AND GOING ASTRAY,\n"
                        "SINCE JESUS CAME INTO MY HEART'\n"
                        "AND MY SINS WHICH WERE MANY\n"
                        "ARE ALL WASHED AWAY,\n"
                        "SINCE JESUS CAME INTO MY HEART.",
                        "Stanza-3",
                        "I'M POSSESSED OF A HOPE\n"
                        "THAT IS STEADFAST AND SURE,\n"
                        "SINCE JESUS CAME INTO MY HEART'\n"
                        "AND NO DARK CLOUDS OF DOUBT\n"
                        "NOW MY PATHWAY OBSCURE,\n"
                        "SINCE JESUS CAME INTO MY HEART.",
                        "Stanza-4",
                        "THERE'S A LIGHT IN THE VALLEY\n"
                        "OF DEATH NOW FOR ME,\n"
                        "SINCE JESUS CAME INTO MY HEART\n"
                        "AND THE GATES OF THE CITY\n"
                        "BEYOND I CAN SEE,\n"
                        "SINCE JESUS CAME INTO MY HEART.",
                        "Stanza-5",
                        "I SHALL GO THERE TO DWELL\n"
                        "IN THE CITY I KNOW,\n"
                        "SINCE JESUS CAME INTO MY HEART\n"
                        "AND I'M HAPPY, SO HAPPY,\n"
                        "AS ONWARD I GO,\n"
                        "SINCE JESUS CAME INTO MY HEART."]
        self.song_92 = ["Title",
                        "SOFTLY AND TENDERLY\nPage 130",
                        "Chorus",
                        "COME HOME... COME HOME...\n"
                        "YE WHO ARE WEARY, COME HOME...\n"
                        "EARNESTLY, TENDERLY, JESUS IS CALLING,\n"
                        "CALLING, O SINNER COME HOME.!",
                        "Stanza-1",
                        "SOFTLY AND TENDERLY JESUS IS CALLING,\n"
                        "CALLING FOR YOU AND FOR ME;\n"
                        "SEE, ON THE PORTALS\nHE'S WAITING AND WATCHING,\n"
                        "WATCHING FOR YOU AND FOR ME.",
                        "Stanza-2",
                        "WHY SHOULD WE TARRY\nWHEN JESUS IS PLEADING,\n"
                        "PLEADING FOR YOU AND FOR ME?\n"
                        "WHY SHOULD WE LINGER\nAND HEED NOT HIS MERCIES,\n"
                        "MERCIES FOR YOU AND FOR ME?",
                        "Stanza-3",
                        "TIME IS NOW FLEETING,\nTHE MOMENTS ARE PASSING,\n"
                        "PASSING FROM YOU AND FROM ME;\n"
                        "SHADOWS ARE GATHERING,\nDEATH BEDS ARE COMING,\n"
                        "COMING FOR YOU AND FOR ME",
                        "Stanza-4",
                        "OH! FOR THE WONDERFUL LOVE\nHE HAS PROMISED,\n"
                        "PROMISED FOR YOU AND FOR ME;\n"
                        "THO' WE HAVE SINNED,\nHE HAS MERCY AND PARDON,\n"
                        "PARDON FOR YOU AND FOR ME."]
        self.song_93 = ["Title",
                        "SOUND THE BATTLE CRY\nPage 73",
                        "Chorus",
                        "ROUSE, THEN, SOLDIERS,\n"
                        "RALLY ROUND THE BANNER,\n"
                        "READY, STEADY,\nPASS THE WORD ALONG;\n"
                        "ONWARD, FORWARD,\n"
                        "SHOUT ALOUD HOSANA!\n"
                        "CHRIST IS CAPTAIN\nOF THE MIGHTY THRONG",
                        "Stanza-1",
                        "SOUND THE BATLLE CRY!\n"
                        "SEE, THE FOE IS NIGH,\n"
                        "RAISE THE STANDARD HIGH\nFOR THE LORD;\n"
                        "GIRD YOUR ARMOR ON,\n"
                        "STAND FIRM EVERYONE;\n"
                        "REST YOUR CAUSE UPON\nHIS HOLY WORD.",
                        "Stanza-2",
                        "STROMG TO MEET THE FOE,\n"
                        "MARCHING ON WE GO,\n"
                        "WHILE OUR CAUSE WE KNOW\n"
                        "MUST PREVAIL;\n"
                        "SHIELD AND BANNER BRIGHT;\n"
                        "GLEAMING IN THE LIGHT;\n"
                        "BATTLING FOR THE RIGHT\n"
                        "WE NE'ER CAN FAIL.",
                        "Stanza-3",
                        "O! THOU GOD OF ALL,\n"
                        "HEAR US WHEN WE CALL,\n"
                        "HELP US ONE AND ALL\n"
                        "BY THY GRACE;\n"
                        "WHEN THE BATTLE'S DONE,\n"
                        "AND THE VICTRY'S WON,\n"
                        "MAY WE WEAR THE CROWN\n"
                        "BEFORE THY FACE."]
        self.song_94 = ["Title",
                        "STAND UP FOR JESUS\nPage 104",
                        "Stanza-1",
                        "STAND UP, STAND UP FOR JESUS,\n"
                        "YE SOLDIERS OF THE CROSS,\n"
                        "LIFT HIGH HIS ROYAL BANNER,\n"
                        "IT NOT MUST SUFFER LOSS;\n"
                        "FROM VICT'RY UNTO VICT'RY\n"
                        "HIS ARMY SHALL HE LEAD,\n"
                        "TILL EVERY FOE IS VANQUISHED\n"
                        "AND CHRIST IS LORD INDEED.",
                        "Stanza-2",
                        "STAND UP, STAND UP FOR JESUS,\n"
                        "THE TRUMPET CALL OBEY;\n"
                        "FORTH TO THE MIGHTY CONFLICT,\n"
                        "IN THIS HIS GLORIOUS DAY.\n"
                        "YE THAT ARE MEN NOW SERVE HIM,\n"
                        "AGAINST UNNUMBERED FOES;\n"
                        "LET COURAGE RISE WITH DANGER,\n"
                        "AND STRENGTH TO STRENGTH OPPOSE.",
                        "Stanza-3",
                        "STAND UP, STAND UP, FOR JESUS,\n"
                        "STAND IN HIS STRENGTH ALONE;\n"
                        "THE ARM OF FLESH WILL FAIL YOU\n"
                        "YE DARE NOT TRUST YOUR OWN;\n"
                        "PUT ON THE GOSPEL ARMOR,\n"
                        "AND WATCHING UNTO PRAYER,\n"
                        "WHERE DUTY CALLS, OR DANGER\n"
                        "BE NEVER WANTING THERE."]
        self.song_95 = ["Title",
                        "STANDING ON THE PROMISES\nPage 7",
                        "Chorus",
                        "STANDING, STANDING,\n"
                        "STANDING ON THE PROMISES\n"
                        "OF GOD MY SAVIOR;\n"
                        "STANDING, STANDING...\n"
                        "I'M STANDING ON THE\n"
                        "PROMISES OF GOD",
                        "Stanza-1",
                        "STANDING ON THE PROMISES\nOF CHRIST THE KING,\n"
                        "THRO' ETERNAL AGES\nLET HIS PRAISES RING;\n"
                        "GLORY IN THE HIGHEST,\nI WILL SHOUT AND SING,\n"
                        "STANDING ON THE PROMISES OF GOD.",
                        "Stanza-2",
                        "STANDING ON THE PROMISES\nTHAT CANNOT FAIL,\n"
                        "WHEN THE HOWLING STORMS\nOF DOUBT AND FEAR ASAIL,\n"
                        "BY THE LIVING WORD OF GOD\nI SHALL PREVAIL,\n"
                        "STANDING ON THE PROMISES OF GOD.",
                        "Stanza-3",
                        "STANDING ON THE PROMISES\nOF CHRIST THE LORD\n"
                        "BOUND TO HIM ETERNALLY\nBY LOVE'S STRONG CORD,\n"
                        "OVERCOMING DAILY\nWITH THE SPIRIT SWORD,\n"
                        "STANDING ON THE PROMISES OF GOD.",
                        "Stanza-4",
                        "STANDING ON THE PROMISES\nI CANNOT FALL,\n"
                        "LISTENING EVERY MOMENT\nTO THE SPIRIT CALL,\n"
                        "RESTING IN MY SAVIOUR,\nAS MY ALL IN ALL\n"
                        "STANDING ON THE PROMISES OF GOD."]
        self.song_96 = ["Title",
                        "STEPPING IN THE LIGHT\nPage 63",
                        "Chorus",
                        "HOW BEAUTIFUL TO WALK\n"
                        "IN THE STEP OF THE SAVIOR,\n"
                        "STEPPING IN THE LIGHT,\n"
                        "STEPPING IN THE LIGHT;\n"
                        "HOW BEAUTIFUL TO WALK\n"
                        "IN THE STEPS OF THE SAVIOR,\n"
                        "LED IN PATHS OF LIGHT.",
                        "Stanza-1",
                        "TRYING TO WALK IN\nTHE STEPS OF THE SAVIOR,\n"
                        "TRYING TO FOLLOW\nOUR SAVIOR AND KING;\n"
                        "SHAPPING OUR LIVES\nBY HIS BLESSED EXAMPLE,\n"
                        "HAPPY, HOW HAPPY,\nTHE SONGS THAT WE BRING.",
                        "Stanza-2",
                        "PRESSING MORE CLOSELY\nTO HIM WHO IS LEADING,\n"
                        "WHEN WE ARE TEMPTED\nTO TURN FROM THE WAY;\n"
                        "TRUSTING THE ARM\nTHAT IS STRONG TO DEFEND US,\n"
                        "HAPPY HOW HAPPY,\nOUR PRAISES EACH DAY.",
                        "Stanza-3",
                        "WALKING IN FOOTSTEPS\nOF GENTLE FOR BEARANCE,\n"
                        "FOOTSTEPS OF FAITHFULNESS,\nMERCY AND LOVE,\n"
                        "LOOKING TO HIM FOR\nTHE GRACE FREELY PROMISED\n"
                        "HAPPY, HO HAPPY,\nOUR JOURNEY ABOVE.",
                        "Stanza-4",
                        "TRYING TO WALK IN\nTHE STEPS OF THE SAVIOR,\n"
                        "UPWARD, STILL UPWARD\nWE'LL FOLLOW OUR GUIDE;\n"
                        "WHEN WE SHALL SEE HIM,\nTHE KING IN HIS BEAUTY,\n"
                        "HAPPY, HOW HAPPY,\nOUR PLACE AT HIS SIDE."]
        self.song_97 = ["Title",
                        "STILL SWEETER EVERYDAY\nPage 311",
                        "Chorus",
                        "THE HALF CANNOT BE FANCIED\n"
                        "THIS SIDE THE GOLDEN SHORE;\n"
                        "OH, THERE HE'LL BE STILL SWEETER\n"
                        "THAN HE EVER WAS BEFORE.",
                        "Stanza-1",
                        "TO JESUS EVERY DAY I FIND\nMY HEART IN CLOSER DRAWN;\n"
                        "HE'S FAIRER THAN THE GLORY\nOF THE GOLD AND PURPLE DAWN;\n"
                        "HE'S ALL MY FANCY PICTURES\nIN ITS FAIREST DREAMS, AND MORE;\n"
                        "EACH DAY HE GROWS STILL SWEETER\nTHAN HE WAS THE DAY BEFORE.",
                        "Stanza-2",
                        "HIS GLORY BROKE UPON ME\nWHEN I SAW HIM FROM AFAR;\n"
                        "HE'S FAIRER THAN THE LILY,\nBRIGHTER THAN THE MORNING STAR;\n"
                        "HE FILLS AND SATISFIES\nMY LONGING SPIRIT O'ER AND O'ER;\n"
                        "EACH DAY HE GROWS STILL SWEETER\nTHAN HE WAS THE DAY BEFORE.",
                        "Stanza-3",
                        "MY HEART IS SOMETIMES HEAVY,\nBUT HE COMES WITH SWEET RELIEF;\n"
                        "HE FOLDS ME TO HIS BOSSOM\nWHEN I DROOP WITH BLIGHTING GRIEF;\n"
                        "I LOVE THE CHRIST WHO ALL\nMY BURDENS IN HIS BODY BORE;\n"
                        "EACH DAY HE GROWS STILL SWEETER\nTHAN HE WAS THE DAY BEFORE"]
        self.song_98 = ["Title",
                        "SUCH LOVE\nPage 22",
                        "Chorus",
                        "SUCH LOVE, SUCH WONDROUS LOVE,\n"
                        "SUCH LOVE, SUCH WONDROUS LOVE.\n"
                        "THAT GOD SHOULD LOVE A SINNER SUCH AS I\n"
                        "HOW WONDERFUL IS LOVE LIKE THIS!",
                        "Stanza-1",
                        "THAT GOD SHOULD LOVE\nA SINNER SUCH AS I,\n"
                        "SHOULD YEARN TO CHANGE\nMY SORROW INTO BLISS,\n"
                        "NOR REST TILL HE HAD\nPLANNED TO BRING ME NIGH,\n"
                        "HOW WONDERFUL IS LOVE LIKE THIS!",
                        "Stanza-2",
                        "THAT CHRIST SHOULD JOIN\nSO FREELY IN THE SCHEME,\n"
                        "ALTHOUGH IT MEANT\nHIS DEATH ON CALVARY,\n"
                        "DID EVER HUMAN\nTOUGUE FIND NOBLER THEME\n"
                        "THAN LOVE DIVINE THAT RANSOMED ME?",
                        "Stanza-3",
                        "THAT FOR A WILFUL\nOUTCAST SUCH AS I,\n"
                        "THE FATHER PLANNED,\nTHE SAVIOUR BLED AND DIED,\n"
                        "REDEMPTION FOR A\nWORTHLESS SLAVE TO BUY,\n"
                        "WHO LONG HAD LAW\nAND GRACE DEFIED.",
                        "Stanza-4",
                        "AND NOW HE TAKES ME\nTO HIS HEART A SON,\n"
                        "HE ASK ME NOT TO\nFILL A SERVANT'S PLACE\n"
                        "THE FAR OFF COUNTRY\nWANDRINGS ALL ARE DONE,\n"
                        "WIDE OPEN ARE HIS ARMS OF GRACE."]
        self.song_99 = ["Title",
                        "SWEET BY AND BY\nPage 120",
                        "Chorus",
                        "IN THE SWEET BY AND BY\n"
                        "WE SHALL MEET ON THAT\nBEAUTIFUL SHORE (2X)",
                        "Stanza-1",
                        "THERE'S A LAND\nTHAT IS FAIRER THAN DAY,\n"
                        "AND BY FAITH\nWE CAN SEE IT AFAR;\n"
                        "FOR THE FATHER\nWAITS OVER THE WAY,\n"
                        "TO PREPARE US\nA DWELLING PLACE THERE.",
                        "Stanza-2",
                        "WE SHALL SING\nON THAT BEAUTIFUL SHORE,\n"
                        "THE MELODIOUS\nSONGS OF THE BLEST,\n"
                        "AND OUR SPIRITS\nSHALL SORROW NO MORE,\n"
                        "NOT A SIGH FOR\nTHE BLESSING OF REST.",
                        "Stanza-3",
                        "TO OUR BOUNTIFUL\nFATHER ABOVE,\n"
                        "WE WILL OFFER\nTHE TRIBUTE OF PRAISE,\n"
                        "FOR THE GLORIOUS\nGIFT OF HIS LOVE,\n"
                        "AND THE BLESSINGS\nTHAT HALLOW OUR DAYS."]
        self.song_100 = ["Title",
                         "SWEET HOUR OF PRAYER\nPage 173",
                         "Stanza-1",
                         "SWEET HOUR OF PRAYER!\nSWEET HOUR OF PRAYER!\n"
                         "THAT CALLS ME FROM A WORLD OF CARE,\n"
                         "AND BIDS ME AT MY FATHER'S THRONE\n"
                         "MAKE ALL MY WANTS AND WISHES KNOWN\n"
                         "IN SEASONS OF DISTRESS AND GRIEF,\n"
                         "MY SOUL HAS OFTEN FOUND RELIEF.\n"
                         "AND OFT ESCAPED THE TEMPTER'S SNARE\n"
                         "BY THY RETURN, SWEET HOUR OF PRAYER.",
                         "Stanza-2",
                         "SWEET HOUR OF PRAYER!\nSWEET HOUR OF PRAYER!\n"
                         "THY WINGS SHALL MY PETITION BEAR\n"
                         "TO HIM WHOSE THRUTH AND FAITHFULNESS\n"
                         "ENGAGE THE WAITING SOUL TO BLESS;\n"
                         "AND SINCE HE BIDS ME SEEK HIS FACE,\n"
                         "BELIEVE HIS WORD AND TRUST HIS GRACE,\n"
                         "I'LL CAST ON HIM MY EVERY CARE,\n"
                         "AND WAIT FOR THEE,\nSWEET HOUR OF PRAYER.",
                         "Stanza-3",
                         "SWEET HOUR OF PRAYER!\nSWEET HOUR OF PRAYER!\n"
                         "MAY I THY CONSOLATION SHARE,\n"
                         "TILL, FROM MOUNT PISGAH'S LOFTY HEIGHT,\n"
                         "I VIEW MY HOME, AND TAKE MY FLIGHT:\n"
                         "THIS ROBE OF FLESH I'LL DROP AND RISE\n"
                         "TO SEIZE THE EVERLASTING PRIZE;\n"
                         "AND SHOUT, WHILE PASSING\nTHROUGH THE AIR,\n"
                         "FAIRWELL, FAIRWELL,\nSWEET HOUR OF PRAYER."]
        self.song_101 = ["Title",
                         "SWEET PEACE, THE GIFT OF GOD'S LOVE\nPage 112",
                         "Chorus",
                         "PEACE, PEACE SWEET PEACE!\n"
                         "WONDERFUL GIFT FROM ABOVE!\n"
                         "OH WONDEFUL, WONDERFUL PEACE!\n"
                         "SWEET PEACE THE GIFT OF GOD'S LOVE!",
                         "Stanza-1",
                         "THERE COMES TO MY HEART\n"
                         "ONE SWEET STRAIN (SWEET STRAIN)\n"
                         "A GLAD AND A JOYOUS REFRAIN;\n"
                         "I SING IT AGAIN AND AGAIN,\n"
                         "SWEET PEACE THE GIFT OF GOD'S LOVE,",
                         "Stanza-2",
                         "THROUGH CHRIST ON THE CROSS\nPEACE WAS MADE (WAS MADE)\n"
                         "MY DEBT BY HIS DEATH WA ALL PAID\n"
                         "NO OTHER FOUNDATION IS LAID\n"
                         "FOR PEACE THE GIFT OF GODS LOVE.",
                         "Stanza-3",
                         "WHEN JESUS AS LORD\nI HAD CROWNED (HAD CROWNED),\n"
                         "MY HEART WITH THIS PEACE DID ABOUND\n"
                         "IN HIM THE RICH BLESSING I FOUND,\n"
                         "SWEET PEACE THE GIFT OF GOD'S LOVE.",
                         "Stanza-4",
                         "IN JESUS FOR PEACE I ABIDE (ABIDE)\n"
                         "AND AS I KEEP CLOSE TO HIS SIDE\n"
                         "THERE'S NOTHING BUT PEACE DOTH BETIDE,\n"
                         "SWEET PEACE THE GIFT OF GOD'S LOVE."]
        self.song_102 = ["Title",
                         "TELL IT TO JESUS\nPage 125",
                         "Chorus",
                         "TELL IT TO JESUS, TELL IT TO JESUS,\n"
                         "HE IS A FRIEND THAT'S WELL KNOWN;\n"
                         "YOU HAVE NO OTHER\nSUCH A FRIEND OR BROTHER\n"
                         "TELL IT TO JESUS ALONE.",
                         "Stanza-1",
                         "ARE YOU WEARY, AR YOU HEAVY HEARTED\n"
                         "TELL IT TO JESUS, TELL IT TO JESUS;\n"
                         "ARE YOU GRIEVING OVER JOYS DEPARTED?\n"
                         "TELL IT TO JESUS ALONE.",
                         "Stanza-2",
                         "DO THE TEARS FLOW DOWN\nYOUR CHEEKS UNBIDDEN?\n"
                         "TELL IT TO JESUS, TELL IT TO JESUS;\n"
                         "HAVE YOU SINS THAT\nTO MEN'S EYES ARE HIDDEN?\n"
                         "TELL IT TO JESUS ALONE",
                         "Stanza-3",
                         "DO YOU FEAR THE\nGATHERING CLOUDS OF SORROW?\n"
                         "TELL IT TO JESUS, TELL IT TO JESUS;\n"
                         "ARE YOU ANXIOUS\nWHAT SHALL BE TOMORROW?\n"
                         "TELL IT TO JESUS ALONE.",
                         "Stanza-4",
                         "ARE YOU TROUBLED\nAT THE THOUGHT OF DYING?\n"
                         "TELL IT TO JESUS, TELL IT TO JESUS;\n"
                         "FOR CHRIST'S COMING\nKINGDOM ARE YOU SIGHING?\n"
                         "TELL IT TO JESUS ALONE."]
        self.song_103 = ["Title",
                         "THE BANNER OF THE CROSS\nPage 165",
                         "Chorus",
                         "MARCHING ON, MARCHING ON,\n"
                         "FOR CHRIST COUNT EVERYTHING BUT LOSS!\n"
                         "AND TO CROWN HIM KING, TOIL AND SING\n"
                         "'NEATH THE BANNER OF THE CROSS!",
                         "Stanza-1",
                         "THERE'S A ROYAL BANNER\n"
                         "GIVEN FOR DISPLAY\n"
                         "TO THE SOLDIERS OF THE KING;\n"
                         "AS AN ENSIGN FAIR WE\n"
                         "LIFT IT UP TODAY,\n"
                         "WHILE AS RANSOMED\n"
                         "ONES WE SING.",
                         "Stanza-2",
                         "THOUGH THE FOE MAY RAGE\n"
                         "AND GATHER AS THE FLOOD\n"
                         "LET THE STANDARD BE DISPLAYED;\n"
                         "AND BENEATH ITS FOLDS, AS\n"
                         "SOLDIERS OF THE LORD,\n"
                         "FOR THE TRUTH BE NOT DISMAYED!",
                         "Stanza-3",
                         "OVER LAND AND SEA,\n"
                         "WHERE-EVER MAN MAY DWELL,\n"
                         "MAKE THE GLORIOUS TIDINGS KNOWN;\n"
                         "OF THE CRIMSOM BANNER\n"
                         "NOW THE STORY TELL,\n"
                         "WHILE THE LORD SHALL CLAIM HIS OWN",
                         "Stanza-4",
                         "WHEN THE GLORY DAWN 'TIS\n"
                         "DRAWING VERY NEAR\n"
                         "IT IS HASTENING DAY BY DAY;\n"
                         "THEN BEFORE OUR KING\n"
                         "THE FOE SHALL DISAPPEAR AND\n"
                         "THE CROSS THE WORLD SHALL SWAY!"]
        self.song_104 = ["Title",
                         "THE BIBLE STAND\nPage 101",
                         "Chorus",
                         "THE BIBLE STAND THO'\n"
                         "THE HILLS MAY TUMBLE, IT WILL\n"
                         "FIRMLY STAND WHEN THE EARTH\n"
                         "SHALL CRUMBLE; I WILL PLANT\n"
                         "MY FEET ON ITS FIRM FOUNDATION,\n"
                         "FOR THE BIBLE STANDS.",
                         "Stanza-1",
                         "THE BIBLE STANDS LIKE A ROCK\n"
                         "UNDAUNTED WITH THE RAGING\n"
                         "'MID THE RAGING STORMS OF TIME\n"
                         "ITS PAGES BURN WITH THE TRUTH\n"
                         "ETERNAL, AND THEY GLOW\n"
                         "WITH A LIGHT SUBLIME",
                         "Stanza-2",
                         "THE BIBLE STAND LIKE A MOUNTAIN\n"
                         "TOWRING FAR ABOVE THE WORKS OF MEN;\n"
                         "HIS TRUTH BY NONE EVER WAS REPUTED,\n"
                         "AND DESTROY IT THEY NEVER CAN",
                         "Stanza-3",
                         "THE BIBLE STANDS. AND IT WILL FOREVER\n"
                         "WHEN THE WORLD HAS PASSED AWAY,\n"
                         "BY INSPIRATION IT HAS BEEN GIVEN,\n"
                         "ALL ITS PERCEPTS I WILL OBEY",
                         "Stanza-4",
                         "THE BIBLE STANDS EVERY TEST\n"
                         "WE GIVE IT, FOR ITS AUTHOR IS DIVINE;\n"
                         "BY GRACE ALONE I EXPECT TO LIVE IT,\n"
                         "AND TO PROVE IT AND MAKE IT MINE."]
        self.song_105 = ["Title",
                         "THE CHURCH'S ONE FOUNDATION\nPage 308",
                         "Stanza-1",
                         "THE CHURCH'S ONE FOUNDATION\nIS JESUS CHRIST HER LORD;\n"
                         "SHE IS HIS NEW CREATIIOON\nBY WATER AND THE WORD;\n"
                         "FROM HEAV'N HE CAME AND SOUGHT\nHER TO BE HIS HOLY BRIDE;\n"
                         "WITH HIS OWN BLOOD HE BOUGHT HER,\nAND FOR HER LIFE HE DIED.",
                         "Stanza-2",
                         "ELECT FROM EV'RY NATION,\nYET ONE O'ER ALL THE EARTH,\n"
                         "HER CHARTER OF SALVATION,\nONE LORD ONE FAITH, ONE BIRTH;\n"
                         "ONE HOLY NAME SHE BLESSES,\nPARTAKES ONE HOLY FOOD,\n"
                         "AND TO ONE HOPE SHE PRESSES,\nWITH EVERY GRACE ENDUED.",
                         "Stanza-3",
                         "'MID TOL AND TRIBULATION,\nAND TUMULT OF HER WAR,\n"
                         "SHE WAITS THE CONSUMMATION\nOF PEACE FOREVER-MORE\n"
                         "TILL, WITH THE VISION GLORIOUS,\nHER LONGING EYES ARE BLEST,\n"
                         "AND THE GREAT CHURCH VICTORIOUS\nSHALL BE THE CHURCH AT REST.",
                         "Stanza-4",
                         "YET SHE ON EARTH HATH UNION\nWITH GOD THE THREE IN ONE,\n"
                         "AND MYSTIC SWEET COMMUNION\nWITH THOSE WHOSE REST IS WON:\n"
                         "O HAPPY ONES AND HOLY! LORD,\nGIVE US GRACE THAT WE,\n"
                         "LIKE THEM, THE MEEK AND LOWLY,\nON HIGH MAY DWELL WITH THEE."]
        self.song_106 = ["Title",
                         "THE COMPORTER HAS COME\nPage 80",
                         "Chorus",
                         "THE COMPORTER HAS COME,\n"
                         "THE COMPORTER HAS COME!\n"
                         "THE HOLY GHOST HEAV'N,\n"
                         "THE FATHER’S PROMISE GIV'N;\n"
                         "OH, SPREAD THE TIDINGS ROUND,\n"
                         "WHERE-EVER MAN IS FOUND\n"
                         "THE COMPORTER HAS COME!",
                         "Stanza-1",
                         "OH, SPREAD THE TIDINGS ROUND,\n"
                         "WHERE-EVER MAN IS FOUND,\n"
                         "WHERE EVER HUMAN HEARTS\n"
                         "AND HUMAN WOES ABOUND;\n"
                         "LET EVERY CHRISTIAN TONGUE\n"
                         "PROCLAIM THE JOYFUL SOUND;\n"
                         "THE COMPORTER HAS COME!",
                         "Stanza-2",
                         "THE LONG, LONG NIGHT IS PAST,\n"
                         "THE MORNING BREAKS AT LAST;\n"
                         "AND HUSHED THE DREADFUL WALL\n"
                         "AND FURY OF THE BLAST,\n"
                         "AS O'ER THE GOLDEN HILLS\n"
                         "THE DAY ADVANCES FAST!\n"
                         "THE COMPORTER HAS COME!",
                         "Stanza-3",
                         "LO, THE GREAT KING OF KINGS,\n"
                         "WITH HEALING OF HIS WINGS,\n"
                         "TO EVERY CAPTIVE SOUL\n"
                         "A FULL DELIV'RANCE BRINGS;\n"
                         "AND THR'O THE VACANT CELLS\n"
                         "THE SONG OF TRIUMPH RINGS:\n"
                         "THE COMPORTER HAS COME!",
                         "Stanza-4",
                         "O BOUNDLESS LOVE DIVINE!\n"
                         "HOW SHALL THIS TONGUE OF MINE\n"
                         "TO WONDRING MORTALS TELL\n"
                         "THE MATCHLESS GRACE DIVINE\n"
                         "THAT I, A CHILD OF HELL,\n"
                         "SHOULD IN HIS IMAGE SHINE!\n"
                         "THE COMPORTER HAS COME!",
                         "Stanza-5",
                         "SING, TILL THE ECHOES FLY\n"
                         "ABOVE THE VAULTED SKY,\n"
                         "AND ALL THE SAINTS ABOVE\n"
                         "TO ALL BELOW REPLY,\n"
                         "IN STRAINS OF ENDLESS LOVE,\n"
                         "THE SONG THAT NE'ER WILL DIE:\n"
                         "THE COMPORTER HAS COME!"]
        self.song_107 = ["Title",
                         "THE FIGHT IS ON\nPage 228",
                         "Chorus",
                         "THE FIGHT IS ON, O CHRISTIAN SOLDIERS;\n"
                         "AND FACE TO FACE IN STERN ARRAY,\n"
                         "WITH ARMOR GLEAMING,\nAND COLORS STREAMING\n"
                         "THE RIGHT AND WRONG ENGAGED TODAY!\n"
                         "THE FIGHT IS ON BUT BE NOT WEARY;\n"
                         "BE STRONG AND IN HIS MIGHT HOLD FAST;\n"
                         "IF GOD BEFORE US, HIS BANNER O'ER US\n"
                         "WE'LL SING THE VICTOR'S SONG AT LAST!",
                         "Stanza-1",
                         "THE FIGHT IS ON,\n"
                         "THE TRUMPET SOUND\nIS RINGING OUT,\n"
                         "THE CRY TO ARMS!\nIS HEARD AFAR AND NEAR;\n"
                         "THE LORD OF HOSTS\nIS MARCHING UNTO VICTORY,\n"
                         "THE TRIUMPH OF\nTHE CHRIST WILL SOON APPEAR.",
                         "Stanza-2",
                         "THE FIGHT IS ON,\n"
                         "AROSE, YE SOLDIERS\nBRAVE AND TRUE!\n"
                         "JEHOVAH LEADS,\nAND VICTORY WILL ASSURE;\n"
                         "GO BUCKLE ON THE\nARMOR GOD HAS GIVEN YOU,\n"
                         "AND IN HIS STRENGTH\nUNTO THE END ENDURE.",
                         "Stanza-3",
                         "THE LORD IS LEADING\nON TO CERTAIN VICTORY;\n"
                         "THE BOW OF PROMISE\nSPANS THE EASTERN SKY;\n"
                         "HIS GLORIOUS NAME\nIN EVERY LAND SHALL HONORED BE;\n"
                         "THE MORN WILL BREAK,\nTHE DAWN OF PEACE IS NIGH."]
        self.song_108 = ["Title",
                         "THE LILY OF THE VALLEY\nPage 99",
                         "Chorus",
                         "HE’S THE LILY OF THE VALLEY,\nTHE BRIGHT AND MORNING STAR,\n"
                         "HE’S THE FAIREST OF\nTEN THOUDSAND TO MY SOUL.",
                         "Stanza-1",
                         "I HAVE FOUND A FRIEND IN JESUS,\n"
                         "HE'S EVERYTHING TO ME,\n"
                         "HE'S THE FAIREST OF\nTEN THOUSAND TO MY SOUL;\n"
                         "THE LILY OF THE VALLEY,\nIN HIM ALONE I SEE\n"
                         "ALL I NEED TO CLEANSE\nAND MAKE ME FULLY WHOLE.\n"
                         "IN SORROW HIS MY COMPORT,\nIN TROUBLE HIS MY STAY,\n"
                         "HE TELLS ME EVERY CARE\nON HIM TO ROLL:",
                         "Stanza-2",
                         "HE ALL MY GRIEFS HAS TAKEN\nAND ALL MY SORROWS BORNE;\n"
                         "IN TEMPTATION HE’S\nMY STRONG AND MIGHTY TOWER;\n"
                         "I HAVE ALL FOR HIM FORSAKEN\nAND ALL MY IDOLS TORN\n"
                         "FROM MY HEART AND NOW\nHE KEEPS ME BY HIS POWER.\n"
                         "THOUGH ALL THE WORLD FORSAKE ME,\nAND SATAN TEMPT ME SORE\n"
                         "THROUGH JESUS I SHALL SAFELY\nREACH THE GOAL:",
                         "Stanza-3",
                         "HE WILL NEVER, NEVER LEAVE ME,\nNOR YET FORSAKE ME HERE,\n"
                         "WHILE I LIVE BY FAITH AND\nDO HIS BLESSED WILL;\n"
                         "A WALL OF FIRE ABOUT ME,\nI'VE NOTHING NOW TO FEAR,\n"
                         "WITH HIS MANNA HE MY HUNRY\nSOUL SHALL FILL.\n"
                         "THEN SWEEPING UP TO GLORY\nTO SEE HIS BLESSED FACE,\n"
                         "WHERE RIVERS OF DELIGHT\nSHALL EVER ROLL:"]
        self.song_109 = ["Title",
                         "THE NAME OF JESUS\nPage 79",
                         "Chorus",
                         "JESUS, OH, HOW SWEET THE NAME!\n"
                         "JESUS, EVERY DAY THE SAME;\n"
                         "JESUS LET ALL SAINTS PROCLAIM\n"
                         "HIS WORTHY PRAISE FOREVER.",
                         "Stanza-1",
                         "THE NAME OF JESUS IS SO SWEET,\n"
                         "I LOVE ITS MUSIC TO REPEAT;\n"
                         "IT MAKES MY JOYS FUL AND COMPLETE\n"
                         "THE PRECIOUS NAME OF JESUS.",
                         "Stanza-2",
                         "I LOVE THE NAME OF HIM WHOSE HEART\n"
                         "KNOWS ALL MY GRIEFS AND BEARS A PART;\n"
                         "WHO BIDS ALL ANXIOUS FEARS DEPART\n"
                         "I LOVE THE NAME OF JESUS.",
                         "Stanza-3",
                         "THAT NAME I FONDLY LOVE TO HEAR,\n"
                         "IT NEVER FAILS MY HEART TO CHEER,\n"
                         "ITS MUSIC DRIES THE FALLING TEAR;\n"
                         "EXALT THE NAME OF JESUS.",
                         "Stanza-4",
                         "NO WORD OF MAN CAN EVER TELL\n"
                         "HOW SWEET THE NAME I LOVE TO TELL;\n"
                         "OH, LET ITS PRAISES EVER SWELL,\n"
                         "OH, PRAISE THE NAME OF JESUS."]
        self.song_110 = ["Title",
                         "THE OLD RUGGED CROSS\nPage 10",
                         "Chorus",
                         "SO I'LL CHERISH THE OLD RUGGED CROSS\n"
                         "TILL MY TROPHIES AT LAST I LAY DOWN;\n"
                         "I WILL CLING TO THE OLD RUGGED CROSS,\n"
                         "AND EXCHANGE IT SOMEDAY FOR A CROWN.",
                         "Stanza-1",
                         "ON A HILL FAR AWAY\nSTOOD AN OLD RUGGED CROSS,\n"
                         "THE EMBLEM OF SUFF’RING AND SHAME;\n"
                         "AND I LOVE THAT OLD CROSS\nWHERE THE DEAREST AND BEST\n"
                         "FOR A WORLD OF LOST\nSINNERS WA SLAIN.",
                         "Stanza-2",
                         "OH, THE OLD RUGGED CROSS,\nSO DESPIESED BY THE WORLD,\n"
                         "HAS THE WONDROUS ATTRACTION FOR ME;\n"
                         "FOR THE DEAR LAMB OF GOD\nLEFT HIS GLORY ABOVE\n"
                         "TO BEAR IT TO DARK CALVARY.",
                         "Stanza-3",
                         "IN THE OLD RUGGED CROSS,\n"
                         "STAINED WITH BLOOD SO DIVINE,\n"
                         "A WONDROUS BEAUTY I SEE;\n"
                         "FOR 'TWAS ON THAT OLD CROSS\n"
                         "JESUS SUFFERED AND DIED\n"
                         "TO PARDON AND SANCTIFY ME.",
                         "Stanza-4",
                         "TO THE OLD RUGGED CROSS\n"
                         "I WILL EVER BE TRUE,\n"
                         "ITS SHAME AND REPROACH GLADLY BEAR;\n"
                         "THEN HE'LL CALL ME SOMEDAY\nTO MY HOME FAR AWAY,\n"
                         "WHERE HIS GLORY\nFOREVER I'LL SHARE."]
        self.song_111 = ["Title",
                         "THE REGIONS BEYOND\nPage 181",
                         "Chorus",
                         "TO THE REGIONS BEYOND,\n"
                         "I MUST GO, I MUST GO,\n"
                         "TILL THE WORLD, ALL THE WORLD,\n"
                         "HIS SALVATION SHALL KNOW.",
                         "Stanza-1",
                         "TO THE REGIONS BEYOND\n"
                         "I MUST GO, I MUST GO,\n"
                         "WHERE THE STORY HAS NEVER BEEN TOLD\n"
                         "TO THE MILLIONS THAT NEVER\n"
                         "HAVE HEARD OF HIS LOVE,\n"
                         "I MUST TELL THE SWEET\n"
                         "STORY OF OLD (OF OLD).",
                         "Stanza-2",
                         "TO THE HARDEST OF PLACES\n"
                         "HE CALLS ME TO GO,\n"
                         "NOT THINGKING OF COMFORT OR EASE,\n"
                         "THE WORLD MAY PRONOUNCE ME\n"
                         "A DREAMER, A FOOL, ENOUGH IF\n"
                         "THE MASTER I PLEASE (I PLEASE).",
                         "Stanza-3",
                         "OH, YE THAT ARE SPENDING\n"
                         "YOUR LEISURE AND POWERS\n"
                         "IN PLEASURES SO FOOLISH AND FOND,\n"
                         "AWAKE FROM YOUR SELFISHNESS,\n"
                         "FOOLY AND SIN, AND GO TO THE\n"
                         "REGIONS BEYOND (DEYOND).",
                         "Stanza-4",
                         "THERE ARE OTHER LOST SHEEP\n"
                         "THAT THE MASTER MUST BRING,\n"
                         "AND THEY MUST THE MESSAGE BE TOLD,\n"
                         "HE SENDS ME TO GATHER\n"
                         "THEM OUT OF ALL LANDS,\n"
                         "AND WELCOME THEM BACK\n"
                         "TO HIS FOLD (HIS FOLD)."]
        self.song_112 = ["Title",
                         "THE SOLID ROCK\nPage 69",
                         "Chorus",
                         "ON CHRIST THE SOLID, ROCK I STAND;\n"
                         "ALL OTHER GROUND IS SINKING SAND,\n"
                         "ALL OTHER GROUND IS SINKING SAND.",
                         "Stanza-1",
                         "MY HOPE IS BUILT\nON NOTHING LESS\n"
                         "THAN JESUS BLOOD\nAND RIGHTEOUSNESS;\n"
                         "I DARE NOT TRUST\nTHE SWEETEST FRAME,\n"
                         "BUT WHOLY LEAN\nON JESUS NAME.",
                         "Stanza-2",
                         "WHEN DARKNESS SEEMS\nTO HIDE HIS FACE,\n"
                         "I REST ON HIS\nUNCHANGING GRACE;\n"
                         "IN EVERY HIGH\nAND STORMY GALE,\n"
                         "MY ANCHOR HOLDS\nWITHIN THE VALE.",
                         "Stanza-3",
                         "HIS OATH, HIS\nCOVENANT, HIS BLOOD,\n"
                         "SUPPORT ME IN\nTHE WHELMING FLOOD;\n"
                         "WHEN ALL AROUND\nMY SOUL GIVES WAY,\n"
                         "HE THEN IS ALL\nMY HOPE AND STAY.",
                         "Stanza-4",
                         "WHEN HE SHALL COME\nWITH TRUMPET SOUND,\n"
                         "OH, MAY I THEN\nIN HIM BE FOUND;\n"
                         "DRESSED IN HIS\nRIGHTEOUSNESS ALONE,\n"
                         "FAULTLESS TO STAND\nBEFORE THE THRONE."]
        self.song_113 = ["Title",
                         "THERE IS POWER IN THE BLOOD\nPage 43",
                         "Chorus",
                         "THERE IS POW'R, POW'R,\n"
                         "WONDER WORKING POW’R\n"
                         "IN THE BLOOD OF THE LAMB;\n"
                         "THERE IS POW'R, POW'R,\n"
                         "WONDER WORKING POW’R\n"
                         "IN THE PRECIOUS\nBLOOD OF THE LAMB;",
                         "Stanza-1",
                         "WOULD YOU BE FREE\n"
                         "FROM THE BURDEN OF SIN?\n"
                         "THERE'S POW’R IN THE BLOOD,\n"
                         "POW’R IN THE BLOOD;\n"
                         "WOULD YOU O'ER EVIL,\nA VICTORY WIN?\n"
                         "THERE'S WONDERFUL POW’R\n"
                         "IN THE BLOOD.",
                         "Stanza-2",
                         "WOULD YOU BE FREE\nFROM YOUR PASSION AND PRIDE?\n"
                         "THERE’S POW’R IN THE BLOOD,\n"
                         "POW’R IN THE BLOOD;\n"
                         "COME FOR A CLEANSING\n"
                         "TO CALVARY’S TIDE;\n"
                         "THERE’S WONDERFUL POW’R\n"
                         "IN THE BLOOD.",
                         "Stanza-3",
                         "WOULD YOU BE WHITER,\nMUCH WHITER THAN SNOW?\n"
                         "THERE'S POW’R IN THE BLOOD,\n"
                         "POW’R IN THE BLOOD;\n"
                         "SIN STAINS ARE LOST\n"
                         "IN ITS LIFE GIVING FLOW;\n"
                         "THERE’S WONDERFUL POW’R\n"
                         "IN THE BLOOD.",
                         "Stanza-4",
                         "WOULD YOU DO SERVICE\nFOR JESUS YOUR KING?\n"
                         "THERE’S POW’R IN THE BLOOD,\nPOW'R IN THE BLOOD;\n"
                         "WOULD YOU LIVE DAILY\nHIS PRAISES TO SING?\n"
                         "THERE’S WONDERFUL POW’R\nIN THE BLOOD."]
        self.song_114 = ["Title",
                         "THERE SHALL BE SHOWERS OF BLESSINGS\nPage 26",
                         "Chorus",
                         "SHOWERS OF BLESSING,\n"
                         "SHOWERS OF BLESSING WE NEED:\n"
                         "MERCY DROPS ROUND US ARE FALLING,\n"
                         "BUT FOR THE SHOWERS WE PLEAD.",
                         "Stanza-1",
                         "THERE SHALL BE SHOWERS OF BLESSING\n"
                         "THIS IS THE PROMISE OF LOVE;\n"
                         "THERE SHALL BE SEASONS REFRESHING,\n"
                         "SENT FROM THE SAVIOUR ABOVE.",
                         "Stanza-2",
                         "THERE SHALL BE SHOWERS OF BLESSING\n"
                         "PRECIOUS REVIVING AGAIN;\n"
                         "OVER THE HILLS AND THE VALLEYS,\n"
                         "SOUND OF ABUNDANCE OF RAIN.",
                         "Stanza-3",
                         "THERE SHALL BE SHOWERS OF BLESSING\n"
                         "SEND THEM UPON US, O LORD;\n"
                         "GRANT TO US NOW A REFRESHING,\n"
                         "COME, AND NOW HONOR THY WORD.",
                         "Stanza-4",
                         "THERE SHALL BE SHOWERS OF BLESSING\n"
                         "OH, THAT TODAY THEY MIGHT FALL.\n"
                         "NOW AS TO GOD WE'RE CONFESSING,\n"
                         "NOW AS ON JESUS WE CALL!"]
        self.song_115 = ["Title",
                         "THERES A GREAT DAY COMING\nPage 175",
                         "Chorus",
                         "ARE YOU READY? ARE YOU READY?\n"
                         "ARE YOU READY FOR THE JUDGEMENT DAY?\n"
                         "ARE YOU READY? ARE YOU READY?\n"
                         "FOR THE JUDGEMENT DAY?",
                         "Stanza-1",
                         "THERE’S A GREAT DAY COMING,\n"
                         "A GREAT DAY COMING,\n"
                         "THERE’S A GREAT DAY COMING BY AND BY;\n"
                         "WHEN THE SAINTS AND THE SINNERS\n"
                         "SHALL BE PARTED RIGHT AND LEFT,\n"
                         "ARE YOU READY FOR THAT DAY TO COME?",
                         "Stanza-2",
                         "THERE’S A BRIGHT DAY COMING,\n"
                         "A BRIGHT DAY COMING,\n"
                         "THERE’S A BRIGHT DAY COMING BY AND BY;\n"
                         "BUT ITS BRIGHTNESS SHALL ONLY\n"
                         "COME TO THEM THAT LOVE THE LORD,\n"
                         "ARE YOU READY FOR THAT DAY TO COME?",
                         "Stanza-3",
                         "THERE’S A SAD DAY COMING,\n"
                         "A SAD DAY COMING,\n"
                         "THERE'S A SAD DAY COMING BY AND BY;\n"
                         "WHEN THE SINNER SHALL HEAR HIS DOOM,\n"
                         "DEPART, IKNOW YE NOT,\n"
                         "ARE YOU READY FOR THAT DAY TO COME?"]
        self.song_116 = ["Title",
                         "THIS WORLD IS NOT MY HOME\nPage 193",
                         "Chorus",
                         "O LORD, YOU KNOW\n"
                         "I HAVE NO FRIEND LIKE YOU,\n"
                         "IF HEAVEN’S NOT MY HOME\n"
                         "THEN LORD, WHAT WILL I DO;\n"
                         "THE ANGELS BECKON ME\n"
                         "FROM HEAVEN’S OPEN DOOR\n"
                         "AND I CAN'T FEEL AT HOME\n"
                         "IN THIS WORLD ANYMORE.",
                         "Stanza-1",
                         "THIS WORLD IS NOT MY HOME,\n"
                         "I'M JUST A PASSING THRO,\n"
                         "MY TREASURES ARE LAID UP\n"
                         "SOMEWHERE BEYOND THE BLUE;\n"
                         "THE ANGELS BECKON ME FROM\n"
                         "HEAVEN’S OPEN DOOR\n"
                         "AND I CAN'T FEEL AT HOME\n"
                         "IN THIS WORLD ANYMORE",
                         "Stanza-2",
                         "THEY’RE ALL EXPECTING ME,\n"
                         "AND THAT’S ONE THING I KNOW,\n"
                         "MY SAVIOR PARDONED ME\n"
                         "AND NOW I ONWARD GO;\n"
                         "I KNOW HE'LL TAKE ME THRU\n"
                         "THO I AM WEAK AND POOR,\n"
                         "AND I CAN'T FEEL AT HOME\n"
                         "IN THIS WORLD ANYMORE",
                         "Stanza-3",
                         "I HAVE A LOVING MOTHER\n"
                         "UP IN GLORY LAND,\n"
                         "I DON'T EXPECT TO STOP\n"
                         "UNTIL I SHAKE HER HAND;\n"
                         "SHE'S WAITING NOW FOR ME\n"
                         "IN HEAVEN’S OPEN DOOR,\n"
                         "AND I CAN'T FEEL AT HOME\n"
                         "IN THIS WORLD ANYMORE",
                         "Stanza-4",
                         "JUST UP IN GLORY LAND\n"
                         "WE'LL LIVE ETERNALLY,\n"
                         "THE SAINTS ON EVERY HAND\n"
                         "ARE SHOUTING VICTORY;\n"
                         "THE SONG OF SWEETEST PRAISE\n"
                         "DRIFT BACK FROM HEAVEN’S SHORE,\n"
                         "AND I CAN'T FEEL AT HOME\n"
                         "IN THIS WORLD ANYMORE"]
        self.song_117 = ["Title",
                         "TILL THE WHOLE WORLD KNOWS\nPage 295",
                         "Chorus",
                         "TILL THE WHOLE WORLD KNOWS,\n"
                         "TILL THE WHOLE WORLD KNOWS,\n"
                         "I WILL SHOUT AND SING\n"
                         "OF CHRIST MY KING,\n"
                         "TILL THE WHOLE WORLD KNOWS.",
                         "Stanza-1",
                         "I'LL TEL TO ALL THAT GOD IS LOVE;\n"
                         "FOR THE WORLD HAS NEVER KNOWN\n"
                         "THE GREAT COMPASSION OF HIS HEART,\n"
                         "FOR THE WAYWARD AND THE LONE.",
                         "Stanza-2",
                         "I'LL TELL OF MERCY'S BOUNDLESS TIDE,\n"
                         "LIKE THE WATERS OF THE SEA,\n"
                         "THAT COVERS EVERY SIN OF MAN;\n"
                         "'TIS SALVATION FULL AND FREE.",
                         "Stanza-3",
                         "I'LL TELL OF GRACE THAT KEEPS THE SOUL,\n"
                         "OF ABIDING PEACE WITHIN,\n"
                         "OF FAITH THAT OVERCOMES THE WORLD,\n"
                         "WITH ITS TUMULT AND ITS DIN.",
                         "Stanza-4",
                         "ETERNAL GLORY IS THE GOAL\n"
                         "THAT AWAITS THE SONS OF LIGHT;\n"
                         "ETERNAL DARKNESS, BLACK AS DEATH,\n"
                         "FOR THE CHILDREN OF THE NIGHT."]
        self.song_118 = ["Title",
                         "TIS SO SWEET TO TRUST IN JESUS\nPage 152",
                         "Chorus",
                         "JESUS, JESUS, HOW I TRUST HIM,\n"
                         "HOW I PROVED HIM O'ER AND O'ER!\n"
                         "JESUS, JESUS, PRECIOUS JESUS!\n"
                         "O FOR GRACE TO TRUST HIM MORE!",
                         "Stanza-1",
                         "'TIS SO SWEET TO TRUST IN JESUS,\n"
                         "JUST TO TAKE HIM AT HIS WORD;\n"
                         "JUST TO REST UPON HIS PROMISE,\n"
                         "JUST TO KNOW THUS SAITH THE LORD.",
                         "Stanza-2",
                         "O HOW SWEET TO TRUST IN JESUS,\n"
                         "JUST TO TRUST HIS CLEANSING BLOOD;\n"
                         "JUST IN SIMPLE FAITH TO PLUNGE ME\n"
                         "'NEATH THE HEALING, CLEANSING FLOOD!",
                         "Stanza-3",
                         "YES, 'TIS SWEET TO TRUST IN JESUS,\n"
                         "JUST FROM SIN AND SELF TO CEASE;\n"
                         "JUST FROM JESUS SIMPLY TAKING\n"
                         "LIFE AND REST, AND JOY AND PEACE.",
                         "Stanza-4",
                         "I'M SO GLAD I LEARNED TO TRUST THEE,\n"
                         "PRECIOUS JESUS SAVIOUR, FRIEND;\n"
                         "AND I KNOW THAT THOU ART WITH ME,\n"
                         "WILT BE WITH ME TO THE END."]
        self.song_119 = ["Title",
                         "TO GOD BE THE GLORY\nPage 4",
                         "Chorus",
                         "PRAISE THE LORD, PRAISE THE LORD,\n"
                         "LET THE EARTH HEAR HIS VOICE!\n"
                         "PRAISE THE LORD, PRAISE THE LORD,\n"
                         "LET THE PEOPLE REJOICE!\n"
                         "O COME TO THE FATHER TO JESUS THE SON,\n"
                         "AND GIVE HIM THE GLORY\nGREAT THINGS HE HATH DONE.",
                         "Stanza-1",
                         "TO GOD BE THE GLORY\nGREAT THINGS HE HATH DONE,\n"
                         "SO LOVED HE THE WORLD\nTHAT HE GAVE US HIS SON,\n"
                         "WHO YIELDED HIS LIFE\nAN ATONEMENT FOR SIN.\n"
                         "AND OPENED THE LIFE GATE\nTHAT ALL MAY GO IN.",
                         "Stanza-2",
                         "O PERFECT REDEMTION,\nTHE PURCHASE OF BLOOD,\n"
                         "TO EVERY BELIEVER\nTHE PROMISE OF GOD;\n"
                         "THE VILEST OFFENDER\nWHO TRULY BELIEVES,\n"
                         "THAT MOMENT FROM JESUS\nA PARDON RECEIVES.",
                         "Stanza-3",
                         "GREAT THINGS HE HATH TAUGHT US,\nGREAT THINGS HE HATH DONE,\n"
                         "AND GREAT OUR REJOICING\nTHRO JESUS THE SON;\n"
                         "BUT PURER, AND HIGHER,\nAND GREATER WILL BE\n"
                         "OUR WONDER, OUR TRANSPORT,\nWHEN JESUS WE SEE."]
        self.song_120 = ["Title",
                         "TO THE WORK\nPage 294",
                         "Chorus",
                         "TOILING ON, TOILING ON,\n"
                         "TOILING ON, TOILONG ON;\n"
                         "LET US HOPE, LET US WATCH,\n"
                         "AND LABOR TILL THE MASTER COMES.",
                         "Stanza-1",
                         "TO THE WORK! TO THE WORK!\n"
                         "WE ARE SERVANTS OF GOD,\n"
                         "LET US FOLLOW THE PATH\n"
                         "THAT OUR MASTER HAS TROD;\n"
                         "WITH THE BALM OF HIS COUNSEL\n"
                         "OUR STRENGTH TO RENEW,\n"
                         "LET US DO WITH OUR MIGHT\n"
                         "WHAT OUR HANDS FIND TO DO.",
                         "Stanza-2",
                         "TO THE WORK! TO THE WORK!\n"
                         "LET THE HUNGRY BE FED;\n"
                         "TO THE FOUNTAIN OF LIFE\n"
                         "LET THE WEARY BE LED;\n"
                         "IN THE CROSS AND ITS BANNER\n"
                         "OUR GLORY SHALL BE,\n"
                         "WHILE WE HERALD THE TIDINGS,\n"
                         "SALVATION IS FREE!",
                         "Stanza-3",
                         "TO THE WORK! TO THE WORK!\n"
                         "THERE IS LABOR FOR ALL;\n"
                         "FOR THE KINGDOM OF DARKNESS\n"
                         "AND ERROR SHALL FALL;\n"
                         "AND THE NAME OF JEHOVAH\n"
                         "EXALTED SHALL BE,\n"
                         "IN THE LOUD SWELLING CHORUS,\n"
                         "SALVATION IS FREE!",
                         "Stanza-4",
                         "TO THE WORK! TO THE WORK!\n"
                         "IN THE STRENGTH OF THE LORD,\n"
                         "AND A ROBE AND A CROWN\n"
                         "SHALL OUR LABOR REWARD,\n"
                         "WHEN THE HOME OF THE FAITHFUL\n"
                         "OUR DWELLING SHALL BE,\n"
                         "AND WE SHOUT WITH THE RANSOMED,\n"
                         "SALVATION IS FREE!"]
        self.song_121 = ["Title",
                         "TRUST AND OBEY\nPage 38",
                         "Chorus",
                         "TRUST AND OBEY,\n"
                         "FOR THERE'S NO OTHER WAY\n"
                         "TO BE HAPPY IN JESUS,\n"
                         "BUT TO TRUST AND OBEY.",
                         "Stanza-1",
                         "WHEN WE WALK WITH THE LORD\n"
                         "IN THE LIGHT OF HIS WORD\n"
                         "WHAT A GLORY HE SHEDS ON OUR WAY!\n"
                         "WHILE WE DO HIS GOOD WILL,\n"
                         "HE ABIDES WITH US STILL,\n"
                         "AND WITH ALL WHO WILL\n"
                         "TRUST AND OBEY.",
                         "Stanza-2",
                         "NOT A SHADOW CAN RISE,\n"
                         "NOT A CLOUD IN THE SKIES,\n"
                         "BUT HIS SMILE QUICKLY DRIVES IT AWAY;\n"
                         "NOT A DOUBT OR A FEAR,\n"
                         "NOT A SIGH NOR A TEAR,\n"
                         "CAN ABIDE WHILE WE\n"
                         "TRUST AND OBEY.",
                         "Stanza-3",
                         "NOT A BURDEN WE BEAR,\n"
                         "NOT A SORROW WE SHARE,\n"
                         "BUT OUR TOIL HE DOTH RICHLY REPAY;\n"
                         "NOT A GRIEF NOR A LOSS,\n"
                         "NOT A FROWN OR A CROSS,\n"
                         "BUT IS BLEST IF WE\n"
                         "TRUST AND OBEY.",
                         "Stanza-4",
                         "BUT WE NEVER CAN PROVE\n"
                         "THE DELIGHTS OF HIS LOVE\n"
                         "UNTIL ALL ON THE ALTAR WE LAY;\n"
                         "FOR THE FAVOR HE SHOWS,\n"
                         "AND THE JOY HE BESTOWS,\n"
                         "ARE FOR THEM WHO WILL\n"
                         "TRUST AND OBEY.",
                         "Stanza-5",
                         "THEN IN FELLOWSHIP SWEET\n"
                         "WE WILL SIT AT HIS FEET,\n"
                         "OR WE'LL WALK BY HIS SIDE IN THE WAY;\n"
                         "WHAT HE SAYS WE WILL DO,\n"
                         "WHERE HE SENDS WE WILL GO,\n"
                         "NEVER FEAR, ONLY\n"
                         "TRUST AND OBEY."]
        self.song_122 = ["Title",
                         "TURN YOUR EYES UPON JESUS\nPage 140",
                         "Chorus",
                         "TURN YOUR EYES UPON JESUS,\n"
                         "LOOK FULL IN HIS WONDERFUL FACE;\n"
                         "AND THE THINGS OF EARTH\n"
                         "WILL GROW STRANGELY DIM\n"
                         "IN THE LIGHT OF HIS GLORY AND GRACE.",
                         "Stanza-1",
                         "O SOUL ARE YOU WEARY AND TROUBLED?\n"
                         "NO LIGHT IN THE DARKNESS YOU SEE?\n"
                         "THERE'S LIGHT FOR A LOOK AT THE SAVIOR,\n"
                         "AND LIFE MORE ABUNDANT AND FREE!",
                         "Stanza-2",
                         "THRO' DEATH INTO LIFE EVERLASTING\n"
                         "HE PASSED, AND WE FOLLOW HIM THERE;\n"
                         "OVER US SIN NO MORE HATH DOMINION\n"
                         "FOR MORE THAN CONQUERORS WE ARE!",
                         "Stanza-3",
                         "HIS WORD SHALL NOT\nFAIL YOU HE PROMISED;\n"
                         "BELIEVE HIM, AND ALL WILL BE WELL;\n"
                         "THEN GO TO A WORLD THAT IS DYING,\n"
                         "HIS PERFECT SALVATION TO TELL!"]
        self.song_123 = ["Title",
                         "VERILY, VERILY\nPage 284",
                         "Chorus",
                         "VERILY, VERILY,\nI SAY UNTO YOU\n"
                         "VERILY, VERILY,\nMESSAGE EVER NEW;\n"
                         "HE THAT BELIEVETH ON\nTHE SON, TIS TRUE\n"
                         "HATH EVERLASTING LIFE.",
                         "Stanza-1",
                         "OH WHAT A SAVIOR,\nTHAT HE DIED FOR ME!\n"
                         "FROM CONDEMNATION\nHE HATH MADE ME FREE;\n"
                         "HE THAT BELIEVETH\nON THE SON, SAITH HE.\n"
                         "HATH EVERLASTING LIFE.",
                         "Stanza-2",
                         "ALL MY INIQUITIES\nON HIM WERE LAID,\n"
                         "ALL MY INDEBTEDNESS\nBY HIM WAS PAID;\n"
                         "ALL WHO BELIEVE ON HIM,\nTHE LORD HATH SAID,\n"
                         "HATH EVERLASTING LIFE.",
                         "Stanza-3",
                         "THOUGH POOR AND NEEDY\nI CAN TRUST MY LORD,\n"
                         "THOUGH WEAK AND SINFUL\nI BELIEVE HIS WORD;\n"
                         "OH, GLAD MESSAGE!\nEVERY CHILD OF GOD\n"
                         "HATH EVERLASTING LIFE.",
                         "Stanza-4",
                         "THOUGH ALL UNWORTHY,\nYET I WILL NOT DOUBT,\n"
                         "FOR HIM THAT COMETH,\nHE WILL NOT CAST OUT;\n"
                         "HE THAT BELIEVETH,\nOH, THE GOOD NEWS SHOUT,\n"
                         "HATH EVERLASTING LIFE!"]
        self.song_124 = ["Title",
                         "VICTORY IN JESUS\nPage 118",
                         "Chorus",
                         "O VICTORY IN JESUS,\nMY SAVIOR, FOREVER\n"
                         "HE SOUGHT ME AND BOUGHT ME\nWITH HIS REDEEMING BLOOD.\n"
                         "HE LOVED ME ERE I KNEW HIM,\nAND ALL MY LOVE IS DUE HIM.\n"
                         "HE PLUNGED ME TO VICTORY\nBENEATH THE CLEANSING FLOOD.",
                         "Stanza-1",
                         "I HEARD AN OLD, OLD STORY.\n"
                         "HOW A SAVIOR CAME FROM GLORY,\n"
                         "HOW HE GAVE HIS LIFE ON CALVARY\nTO SAVE A WRETCH LIKE ME;\n"
                         "I HEARD ABOUT HIS GROANING,\nOF HIS PRECIOUS BLOOD'S ATONING,\n"
                         "THEN I REPENTED OF MY SINS\nAND WON THE VICTORY.",
                         "Stanza-2",
                         "I HEARD ABOUT HIS HEALING,\nOF HIS CLEANSING POW'R REVEALING,\n"
                         "HOW HE MADE THE LAME TO WALK AGAIN\nAND CAUSED THE BLIND TO SEE;\n"
                         "AND THEN I CRIED, DEAR JESUS,\nCOME AND HEAL MY BROKEN SPIRIT,\n"
                         "AND SOMEHOW JESUS CAME AND BRO'T\nTO ME THE VICTORY.",
                         "Stanza-3",
                         "I HEARD ABOUT THE MANSION\nHE HAS BUILT FOR ME IN GLORY,\n"
                         "AND I HEARD ABOUT THE STREETS OF GOLD\nBEYOND THE CRYSTAL SEA;\n"
                         "ABOUT THE ANGELS SINGING,\nAND THE OLD REDEMPTION STORY,\n"
                         "AND SOME SWEET DAY I'LL SING UP THERE\nTHE SONG OF VICTORY."]
        self.song_125 = ["Title",
                         "WE'VE A STORY TO TELL\nPage 2",
                         "Chorus",
                         "FOR THE DARKNESS\nSHALL TURN TO DAWNING,\n"
                         "AND THE DAWNING\nTO NOON-DAY BRIGHT,\n"
                         "AND CHRIST'S GREAT KINGDOM\nSHALL COME ON EARTH,\n"
                         "THE KINGDOM OF LOVE AND LIGHT.",
                         "Stanza-1",
                         "WE'VE A STORY\nTO TELL TO THE NATIONS,\n"
                         "THAT SHALL TURN\nTHEIR HEARTS TO THE RIGHT;\n"
                         "A STORY OF TRUTH AND SWEETNESS,\n"
                         "A STORY OF PEACE AND LIGHT,\n"
                         "A STORY OF PEACE AND LIGHT.",
                         "Stanza-2",
                         "WE'VE A SONG\nTO BE SUNG TO THE NATIONS,\n"
                         "THAT SHALL LIFT\nTHEIR HEARTS TO THE LORD;\n"
                         "A SONG THAT SHALL CONQUER EVIL\n"
                         "AND SHATTER THE SPEAR AND SWORD,\n"
                         "AND SHATTER THE SPEAR AND SWORD.",
                         "Stanza-3",
                         "WE'VE A MESSAGE\nTO GIVE TO THE NATIONS,\n"
                         "THAT THE LORD WHO REIGNETH ABOVE,\n"
                         "HATH SENT US HIS SON TO SAVE US,\n"
                         "AND SHOW US THAT GOD IS LOVE,\n"
                         "AND SHOW US THAT GOD IS LOVE.",
                         "Stanza-4",
                         "WE'VE A SAVIOUR\nTO SHOW TO THE NATIONS,\n"
                         "WHO THE PATH OF SORROW HAS TROD,\n"
                         "THAT ALL OF THE WORLD'S GREAT PEOPLE\n"
                         "MIGHT COME TO THE TRUTH OF GOD,\n"
                         "MIGHT COME TO THE TRUTH OF GOD!"]
        self.song_126 = ["Title",
                         "WHAT A FRIEND\nPage 85",
                         "Stanza-1",
                         "WHAT A FRIEND WE HAVE IN JESUS,\n"
                         "ALL OUR SINS AND GRIEFS TO BEAR!\n"
                         "WHAT A PRIVILEGE TO CARRY\n"
                         "EVERYTHING TO GOD IN PRAYER!\n"
                         "O WHAT PEACE WE OFTEN FORFEIT,\n"
                         "O WHAT NEEDLESS PAIN WE BEAR,\n"
                         "ALL BEACAUSE WE DO NOT CARRY\n"
                         "EVERYTHING TO GOD IN PRAYER!",
                         "Stanza-2",
                         "HAVE WE TRIALS AND TEMPTATIONS?\n"
                         "IS THERE TROUBLE ANYWHERE?\n"
                         "WE SHOULD NEVER BE DISCOURAGED,\n"
                         "TAKE IT TO THE LORD IN PRAYER.\n"
                         "CAN WE FIND A FRIEND SO FAITHFUL\n"
                         "WHO WILL ALL OUR SORROWS SHARE?\n"
                         "JESUS KNOWS OUR EVERY WEAKNESS,\n"
                         "TAKE IT TO THE LORD IN PRAYER.",
                         "Stanza-3",
                         "ARE WE WEAK AND HEAVY LADEN,\n"
                         "CUMBERED WITH A LOAD OF CARE?\n"
                         "PRECIOUS SAVIOUR, STILL OUR REFUGE,\n"
                         "TAKE IT TO THE LORD IN PRAYER.\n"
                         "DO THY FRIENDS DESPIES, FORSAKE THEE?\n"
                         "TAKE IT TO THE LORD IN PRAYER;\n"
                         "IN HIS ARMS HE'LL TAKE AND SHIELD THEE,\n"
                         "THOU WILT FIND A SOLACE THERE."]
        self.song_127 = ["Title",
                         "WHEN THE ROLL IS CALLED UP YONDER\nPage 30",
                         "Chorus",
                         "WHEN THE ROLL IS CALLED UP YONDER,\n"
                         "WHEN THE ROLL IS CALLED UP YONDER,\n"
                         "WHEN THE ROLL IS CALLED UP YONDER,\n"
                         "WHEN THE ROLL IS CALLED UP YONDER,\nI'LL BE THERE",
                         "Stanza-1",
                         "WHEN THE TRUMPET\nOF THE LORD SHALL SOUND\n"
                         "AND TIME SHALL BE NO MORE,\n"
                         "AND THE MORNING BREAKS,\nETERNAL BRIGHT AND FAIR;\n"
                         "WHEN THE SAVED OF EARTH SHALL\nGATHER OVER ON THE OTHER SHORE\n"
                         "AND THE ROLL IS CALLED UP\nYONDER I'LL BE THERE",
                         "Stanza-2",
                         "ON THAT BRIGHT\nAND CLOUDLESS MORNING\nWHEN THE DEAD IN CHRIST SHALL RISE,\n"
                         "AND THE GLORY OF\nHIS RESURECTION SHARE;\nWHEN THE CHOSEN ONES SHALL GATHER\n"
                         "TO THEIR HOME BEYONG THE SKIES,\nAND THE ROLL IS CALLED UP\nYONDER I'LL BE THERE.",
                         "Stanza-3",
                         "LET US LABOR FOR THE MASTER\nFROM THE DAWN TILL SETTING SUN,\n"
                         "LET US TALK OF ALL\nHIS WONDROUS LOVE AND CARE;\n"
                         "THEN WHEN ALL OF LIFE IS OVER,\nAND OUR WORK ON EARTH IS DONE\n"
                         "AND THE ROLL IS CALLED UP\nYONDER I'LL BE THERE"]
        self.song_128 = ["Title",
                         "WHEN WE ALL GET TO HEAVEN\nPage 53",
                         "Chorus",
                         "WHEN WE ALL GET TO HEAVEN,\n"
                         "WHAT A DAY OF REJOICING THAT WILL BE!\n"
                         "WHEN WE ALL SEE JESUS,\n"
                         "WE'LL SING AND SHOUT THE VICTORY",
                         "Stanza-1",
                         "SING THE WONDROUS LOVE OF JESUS,\n"
                         "SING HIS MERCY AND HIS GRACE;\n"
                         "IN THE MANSIONS BRIGHT AND BLESSED,\n"
                         "HE'LL PREPARE FOR US A PLACE.",
                         "Stanza-2",
                         "WHILE WE WALK THE PILGRIM PATHWAY,\n"
                         "CLOUDS WILL OVER SPREAD THE SKY;\n"
                         "BUT WHEN TRAV'LING DAYS ARE OVER,\n"
                         "NOT A SHADOW, NOT A SIGH.",
                         "Stanza-3",
                         "LET US THEN BE TRUE AND FAITHFUL,\n"
                         "TRUSTING, SERVING EVERY DAY;\n"
                         "JUST ONE GLIMPSE OF HIM IN GLORY\n"
                         "WILL THE TOILS OF LIFE REPAY.",
                         "Stanza-4",
                         "ONWARD TO THE PRIZE BEFORE US!\n"
                         "SOON HIS BEAUTY WE'LL BEHOLD;\n"
                         "SOON THE PEARLY GATES WILL OPEN,\n"
                         "WE SHALL TREAD THE STREETS OF GOLD."]
        self.song_129 = ["Title",
                         "WHERE COULD I GO\nPage 111",
                         "Chorus",
                         "WHERE COULD I GO,\n"
                         "O WHERE COULD I GO;\n"
                         "SEEKING A REFUGE FOR MY SOUL?\n"
                         "NEEDING A FRIEND\n"
                         "TO HELP ME IN THE END,\n"
                         "WHERE COULD I GO BUT TO THE LORD",
                         "Stanza-1",
                         "LIVING BELOW\n"
                         "IN THIS OLD SINFUL WORLD\n"
                         "HARDLY A COMPORT CAN AFFORD;\n"
                         "STRIVING ALONE\n"
                         "TO FACE TEMPTATIONS SORE,\n"
                         "WHERE COULD I GO\nBUT TO THE LORD?",
                         "Stanza-2",
                         "NEIGHBORS ARE KIND,\n"
                         "I LOVE THEM EVERY ONE,\n"
                         "WE GET ALONG IN SWEET ACCORD;\n"
                         "BUT WHEN MY SOUL\n"
                         "NEEDS MANNA FROM ABOVE.\n"
                         "WHERE COULD I GO\nBUT TO THE LORD?",
                         "Stanza-3",
                         "LIFE HERE IS GRAND\n"
                         "WITH FRIENDS I LOVE SO DEAR,\n"
                         "COMFORT I GET FROM GOD'S OWN WORD;\n"
                         "YET WHEN I FACE\n"
                         "THE CHILLING HAND OF DEATH,\n"
                         "WHERE COULD I GO\nBUT TO THE LORD?"]
        self.song_130 = ["Title",
                         "WHISPER A PRAYER\nPage 122",
                         "Stanza-1",
                         "WHISPER A PRAY'R IN THE MORNING,\n"
                         "WHISPER A PRAY'R AT NOON;\n"
                         "WHISPER A PRAY'R IN THE EVENING,\n"
                         "TO KEEP YOU HEART IN TUNE.",
                         "Stanza-2",
                         "GOD ANSWERS PRAY'R IN THE MORNING,\n"
                         "GOD ANSWERS PRAY'R AT NOON;\n"
                         "GOD ANSWERS PRAY'R IN THE EVENING,\n"
                         "TO KEEP YOUR HEART IN TUNE.",
                         "Stanza-3",
                         "JESUS MAY COME IN THE MORNING,\n"
                         "JESUS MAY COME AT NOON;\n"
                         "JESUS MAY COME IN THE EVENING,\n"
                         "SO KEEP YOUR HEART IN TUNE."]
        self.song_131 = ["Title",
                         "WHO IS ON THE LORD SIDE\nPage 269",
                         "Stanza-1",
                         "WHO IS ON THE LORD SIDE?\n"
                         "WHO WILL SERVE THE KING?\n"
                         "WHO WILL BE HIS HELPERS,\n"
                         "OTHER LIVES TO BRING?\n"
                         "WHO WILL LEAVE THE WORLD’S SIDE?\n"
                         "WHO WILL FACE THE FOE?\n"
                         "WHO IS ON THE LORD’S SIDE?\n"
                         "WHO FOR HIM WILL GO?",
                         "Chorus-1",
                         "BY THY CALL OF MERCY,\n"
                         "BY THY GRACE DIVINE,\n"
                         "WE ARE ON THE LORD'S SIDE\n"
                         "SAVIOR, WE ARE THINE!",
                         "Stanza-2",
                         "NOT FOR WEIGHT OF GLORY,\n"
                         "NOT FOR CROWN AND PALM,\n"
                         "ENTER WE THE ARMY,\n"
                         "RAISE THE WARRIOR PSALM;\n"
                         "BUT FOR LOVE THAT CLAIMETH\n"
                         "LIVES FOR WHOM HE DIED;\n"
                         "HE WHOM JESUS NAMETH\n"
                         "MUST BE ON HIS SIDE.",
                         "Chorus-2",
                         "BY THY LOVE CONSTRAINING,\n"
                         "BY THY GRACE DIVINE,\n"
                         "WE ARE ON THE LORD'S SIDE\n"
                         "SAVIOR, WE ARE THINE!",
                         "Stanza-3",
                         "JESUS, THOU HAST BOUGHT US,\n"
                         "NOT WITH GOLD OR GEM,\n"
                         "BUT WITH THINE OWN LIFE BLOOD\n"
                         "FOR THY DIADEM;\n"
                         "WITH THY BLESSING FILLING\n"
                         "EACH WHO COMES TO THEE,\n"
                         "THOU HAST MADE US WILLING,\n"
                         "THOU HAST MADE US FREE.",
                         "Chorus-3",
                         "BY THY GRAND REDEMPTION,\n"
                         "BY THY GRACE DIVINE,\n"
                         "WE ARE ON THE LORD'S SIDE\n"
                         "SAVIOR, WE ARE THINE!",
                         "Stanza-4",
                         "FIERCE MAY BE THE CONFLICT,\n"
                         "STRONG MAY BE THE FOE,\n"
                         "BUT THE KING'S OWN ARMY\n"
                         "NONE CAN OVER THROW;\n"
                         "ROUND HIS STANDARD RANGING,\n"
                         "VICT'RY IS SECURE,\n"
                         "FOR HIS TRUTH UNCHANGING\n"
                         "MAKES THE TRIUMPH SURE.",
                         "Chorus-4",
                         "JOYFULLY ENLISTING,\n"
                         "BY THY GRACE DIVINE,\n"
                         "WE ARE ON THE LORD'S SIDE\n"
                         "SAVIOR, WE ARE THINE!", ]
        self.song_132 = ["Title",
                         "WONDERFUL GRACE OF JESUS\nPage 158",
                         "Chorus",
                         "WONDERFUL THE MATCHLESS\nGRACE OF JESUS\n"
                         "DEEPER THAN THE MIGHTY ROLLING SEA;\n"
                         "WONDERFUL GRACE, ALL SUFFICIENT FOR ME,\n"
                         "BROADER THAN THE SCOPE\nOF MY TRANSGRESSIONS,\n"
                         "GREATER FAR THAN ALL MY SINS AND SHAME\n"
                         "O MAGNIFY THE PRECIOUS NAME OF JESUS,\n"
                         "PRAISE HIS NAME!",
                         "Stanza-1",
                         "WONDERFUL GRACE OF JESUS,\nGREATER THAN ALL MY SIN,\n"
                         "HOW SHALL MY TONGUE DESCRIBE IT,\nWHERE SHALL ITS PRAISE BEGIN?\n"
                         "TAKING AWAY MY BURDEN,\nSETTING MY SPIRIT FREE;\n"
                         "FOR THE WONDERFUL GRACE\nOF JESUS REACHES ME.",
                         "Stanza-2",
                         "WONDERFUL GRACE OF JESUS,\nREACHING TO ALL THE LOST,\n"
                         "BY IT I HAVE BEEN PARDONED,\nSAVED TO THE UTTER MOST,\n"
                         "CHAINS HAVE BEEN TURN A SUNDER,\nGIVING ME LIBERTY;\n"
                         "FOR THE WONDERFUL GRACE\nOF JESUS REACHES ME.",
                         "Stanza-3",
                         "WONDERFUL GRACE OF JESUS,\nREACHING THE MOST DEFILED,\n"
                         "BY ITS TRANSFORMING POWER,\nMAKING HIM GOD'S DEAR CHILD,\n"
                         "PURCHASING PEACE AND HEAVEN,\nFOR ALL ETERNITY;\n"
                         "AND THE WONDERFUL GRACE\nOF JESUS REACHES ME."]
        self.song_133 = ["Title",
                         "WONDERFUL WORDS OD LIFE\nPage 244",
                         "Chorus",
                         "BEAUTIFUL WORDS,\n"
                         "WONDERFUL WORDS,\n"
                         "WONDERFUL WORDS OF LIFE. (2X)",
                         "Stanza-1",
                         "SING THEM OVER AGAIN TO ME,\n"
                         "WONDERFUL WORDS OF LIFE;\n"
                         "LET ME MORE OF THEIR BEAUTY SEE,\n"
                         "WONDERFUL WORDS OF LIFE.\n"
                         "WORDS OF LIFE AND BEAUTY,\n"
                         "TEACH ME FAITH AND DUTY;",
                         "Stanza-2",
                         "CHRIST, THE BLESSED ONE GIVES TO ALL,\n"
                         "WONDERFUL WORDS OF LIFE,\n"
                         "SINNER, LIST TO THE LOVING CALL,\n"
                         "WONDERFUL WORDS OF LIFE.\n"
                         "ALL SO FREELY GIVEN,\n"
                         "WOOING US TO HEAVEN;",
                         "Stanza-3",
                         "SWEETLY ECHO THE GOSPEL CALL,\n"
                         "WONDERFUL WORDS OF LIFE;\n"
                         "OFFER PARDON AND PEACE TO ALL,\n"
                         "WONDERFUL WORDS OF LIFE.\n"
                         "JESUS ONLY SAVIOUR, SANCTIFY FOREVER;"]
        self.song_134 = ["Title",
                         "YES, I KNOW!\nPage 142",
                         "Chorus",
                         "AND I KNOW, YES I KNOW\n"
                         "JESUS BLOOD CAN MAKE\nTHE VILEST SINNER CLEAN (2X)",
                         "Stanza-1",
                         "COME YE SINNERS, LOST AND HOPELESS,\n"
                         "JESUS BLOOD CAN MAKE YOU FREE;\n"
                         "FOR HE SAVED THE WORST AMONG YOU,\n"
                         "WHEN HEA SAVED A WRETCH LIKE ME.",
                         "Stanza-2",
                         "TO THE FAINT HE GIVETH POWER,\n"
                         "THRO' THE MOUNTAINS MAKE A WAY;\n"
                         "FINDETH WATER IN THE DESERT,\n"
                         "TURNS THE NIGHT TO GOLDEN DAY",
                         "Stanza-3",
                         "IN TEMPTATION HE IS NEAR THEE,\n"
                         "HOLDS THE POW'RE OF HELL AT BAY;\n"
                         "GUIDES YOU TO THE PATH OF SAFETY,\n"
                         "GIVES YOU GRACE FOR EVERY DAY.",
                         "Stanza-4",
                         "HE WILL KEEP THEE WHILE THE AGES\n"
                         "ROLL THRO'-OUT ETERNITY;\n"
                         "THO' EARTH HINDERS AND HELL RAGES,\n"
                         "ALL MUST WORK FOR GOOD TO THEE"]
        self.song_135 = ["Title",
                         "BASTA'T TAYO'Y SAMA-SAMA\n",
                         "Bridge",
                         "NGUNIT DI KA BA NAGTATAKA,\n"
                         "IKAW AT AKO'Y NARITO PA\n"
                         "HINDI KA BA NAGTATANONG\n"
                         "SAAN HUMUGOT NG LAKAS\n"
                         "SA NAGDAANG PANAHON",
                         "Chorus",
                         "BASTA'T TAYO'Y SAMA-SAMA\n"
                         "SI CRISTO ANG MAGBUBUKLOD\n"
                         "HABANG TUON AY NASA LANGIT\n"
                         "DI TAYO MABIBIGO\n"
                         "HAHARAPIN ANG BAWAT HAMON,\n"
                         "BAON ARAL NG KAHAPON\n"
                         "NA DAKILA ANG KATAPATAN NG PANGINOON.",
                         "Stanza-1",
                         "ILANG PAGSUBOK NARIN\n"
                         "ANG ATING NARANASAN\n"
                         "IBA'T IBA AND SUKAT\n"
                         "IBA'T IBA ANG KULAY\n"
                         "ILANG UNOS NARIN\n"
                         "ANG SA ATI'Y DUMAAN\n"
                         "BAWAT ISA'Y HUMAMON\n"
                         "SA ATING KATAPATAN",
                         "Stanza-2",
                         "DI MALILIMUTAN\n"
                         "PAHINA NG KASAYSAYAN\n"
                         "KUNG PAANO KINALINGA\n"
                         "NG DIYOS NA MAPAGPALA\n"
                         "NGAYON SA ATING AWIT\n"
                         "HANDOG KAY HESUS ANG TINIG\n"
                         "BUHAY NATIN NA NABAGO.\n"
                         "BIYAYANG HANDOG NI CRISTO."]
        self.song_136 = ["Title",
                         "FIND US FAITHFUL\n",
                         "Chorus",
                         "O MAY ALL WHO COME\n"
                         "BEHIND US FIND US FAITHFUL\n"
                         "MAY THE FIRE OF OUR DEVOTION\n"
                         "LIGHT THEIR WAY\n"
                         "MAY THE FOOTPRINTS THAT WE LEAVE\n"
                         "LEAD THEM TO BELIEVE\n"
                         "AND THE LIFE WE LIVE INSPIRE THEM\n"
                         "TO OBEY, O MAY ALL WHO COME\n"
                         "BEHIND US FIND US FAITHFUL",
                         "Stanza-1",
                         "WE'VE PILGRIM ON THE JOURNEY\n"
                         "ON THE NARROW ROAD\n"
                         "AND THOSE WHO'VE COME\n"
                         "BEFORE US LIGHT THE WAY\n"
                         "CHEERING OF THE FAITHFUL,\n"
                         "ENCOURAGING THE WEARY\n"
                         "THEIR LIVES A STEERING TESTAMENT\n"
                         "TO GOD SUSTAINING GRACE.\n",
                         "SURROUNDED BY SO GREAT\n"
                         "A CLOUD OF WITNESSES\n"
                         "LET US RUN THE RACE\n"
                         "NOT ONLY FOR THE PRIZE\n"
                         "BUT AS THOSE WHO'VE\nCOME BEFORE US\n"
                         "LET US LEAVE TO THOSE BEHIND US\n"
                         "A HERITAGE OF FAITHFULNESS\n"
                         "PASSED ON THROUGH GODLY LIVES.",
                         "Stanza-2",
                         "AFTER ALL OUR HOPES AND DREAMS\n"
                         "HAVE COME AND GONE\n"
                         "AND THE CHILDREN SIFT\nTHROUGH ALL WE'VE LEFT BEHIND\n"
                         "MAY THE CLUES THAT THEY DISCOVER\n"
                         "AND THE MEMORIES THEY UNCOVERED\n"
                         "BECOMES A LIGHT THAT LEADS THEM\n"
                         "TO THE ROAD WE EACH MUCH FIND."]
        self.song_137 = ["Title",
                         "HAVE YOU DECIDED TO FOLLOW JESUS?\n",
                         "Stanza-1",
                         "I HAVE DECIDED\nTO FOLLOW JESUS; (3x)\n"
                         "NO TURNING BACK, NO TURNING BACK.",
                         "Stanza-2",
                         "THE WORLD BEHIND ME,\nTHE CROSS BEFORE ME; (3x)\n"
                         "NO TURNING BACK, NO TURNING BACK.",
                         "Stanza-3",
                         "THOUGH NONE GO WITH ME,\nSTILL I WILL FOLLOW; (3x)\n"
                         "NO TURNING BACK, NO TURNING BACK.",
                         "Stanza-4",
                         "MY CROSS I'LL CARRY,\nTILL I SEE JESUS; (3x)\n"
                         "NO TURNING BACK, NO TURNING BACK.",
                         "Stanza-5",
                         "WILL YOU DECIDED NOW\nTO FOLLOW JESUS? (3x)\n"
                         "NO TURNING BACK, NO TURNING BACK."]
        self.song_138 = ["Title",
                         "PSALMS 19:7-10\n",
                         "Chorus",
                         "10   MORE TO BE DESIRED\n       ARE THEY THAN GOLD,\n"
                         "       YEA, THAN MUCH FINE GOLD:\n       SWEETER ALSO THAN HONEY\n"
                         "       AND THE HONEYCOMB.",
                         "Stanza-1",
                         "7    THE LAW OF THE LORD IS PERFECT,\n"
                         "      CONVERTING THE SOUL:\n"
                         "      THE TESTIMONY OF THE LORD IS SURE,\n"
                         "      MAKING WISE THE SIMPLE.",
                         "Stanza-2",
                         "8    THE STATUTES OF THE LORD ARE RIGHT,\n"
                         "      REJOICING THE HEART:\n"
                         "      THE COMMANDMENT OF\n      THE LORD IS PURE,\n"
                         "      ENLIGHTENING THE EYES.",
                         "Stanza-3",
                         "9     THE FEAR OF THE LORD IS CLEAN,\n"
                         "       ENDURING FOR EVER:\n"
                         "       THE JUDGEMENTS OF THE LORD\n"
                         "       ARE TRUE AND RIGHTEOUS ALTOGETHER."]

    def what_song_selected(self, title):
        song_title = title.text()
        self.title_label.setText('Song: ' + song_title)
        self.search_engine.clear()

        # set song lyrics
        row = self.list_of_all_songs.index(song_title)
        self.lyrics_listwidget.clear()

        # this is the more efficient code than doing if else
        var_list = [self.song_0, self.song_1, self.song_2, self.song_3, self.song_4, self.song_5, self.song_6, self.song_7, self.song_8, self.song_9, self.song_10,
                    self.song_11, self.song_12, self.song_13, self.song_14, self.song_15, self.song_16, self.song_17, self.song_18, self.song_19, self.song_20,
                    self.song_21, self.song_22, self.song_23, self.song_24, self.song_25, self.song_26, self.song_27, self.song_28, self.song_29, self.song_30,
                    self.song_31, self.song_32, self.song_33, self.song_34, self.song_35, self.song_36, self.song_37, self.song_38, self.song_39, self.song_40,
                    self.song_41, self.song_42, self.song_43, self.song_44, self.song_45, self.song_46, self.song_47, self.song_48, self.song_49, self.song_50,
                    self.song_51, self.song_52, self.song_53, self.song_54, self.song_55, self.song_56, self.song_57, self.song_58, self.song_59, self.song_60,
                    self.song_61, self.song_62, self.song_63, self.song_64, self.song_65, self.song_66, self.song_67, self.song_68, self.song_69, self.song_70,
                    self.song_71, self.song_72, self.song_73, self.song_74, self.song_75, self.song_76, self.song_77, self.song_78, self.song_79, self.song_80,
                    self.song_81, self.song_82, self.song_83, self.song_84, self.song_85, self.song_86, self.song_87, self.song_88, self.song_89, self.song_90,
                    self.song_91, self.song_92, self.song_93, self.song_94, self.song_95, self.song_96, self.song_97, self.song_98, self.song_99, self.song_100,
                    self.song_101, self.song_102, self.song_103, self.song_104, self.song_105, self.song_106, self.song_107, self.song_108, self.song_109, self.song_110,
                    self.song_111, self.song_112, self.song_113, self.song_114, self.song_115, self.song_116, self.song_117, self.song_118, self.song_119, self.song_120,
                    self.song_121, self.song_122, self.song_123, self.song_124, self.song_125, self.song_126, self.song_127, self.song_128, self.song_129, self.song_130,
                    self.song_131, self.song_132, self.song_133, self.song_134, self.song_135, self.song_136, self.song_137, self.song_138]
        var = var_list[row]

        # add list lyrics to lyrics widget
        for item in range(len(var)):
            self.lyrics_listwidget.addItem(var[item])
            lw = self.lyrics_listwidget.item(item)
            tbd = lw.text()
            if tbd == 'Stanza-1' or tbd == 'Stanza-2' or tbd == 'Stanza-3' or tbd == 'Stanza-4' or tbd == 'Stanza-5' or tbd == 'Chorus' or tbd == 'Title' or tbd == 'Chorus-1' or tbd == 'Chorus-2' or tbd == 'Chorus-3' or tbd == 'Chorus-4' or tbd == 'Bridge':
                lw.setFlags(Qt.NoItemFlags)
                lw.setForeground(Qt.white)
                lw.setBackground(Qt.darkGray)

    def clear_live_screen(self):
        if self.isclear == False:
            self.isclear = True
            self.clear_btn.setStyleSheet("#clear_btn{\n"
                                         "    color: #ffffff;\n"
                                         "    background-color: #1e88e5;\n"
                                         "    border: none;\n"
                                         "    padding: 10px;\n"
                                         "    border-radius: 7px;\n"
                                         "}")
            if self.islive == True:
                self.second_window.label.setText('')
        else:
            self.isclear = False
            self.clear_btn.setStyleSheet("#clear_btn{\n"
                                         "    color: #ffffff;\n"
                                         "    background-color: grey;\n"
                                         "    border: none;\n"
                                         "    padding: 10px;\n"
                                         "    border-radius: 7px;\n"
                                         "}")
            if self.islive == True:
                self.second_window.label.setText(self.lyrics)

    def go_in_live_screen(self, lyrics):
        if self.islive == True:
            ly = lyrics.text()
            self.label_2.setText(ly)
            self.lyrics = ly
            self.second_window.label.setText(self.lyrics)
            if self.isclear == True:
                self.second_window.label.setText('')

            """""
            self.window = QtWidgets.QMainWindow()
            self.second_window = Ui_UI_second()
            self.second_window.setupUi(self.window)
            self.second_window.label.setText(self.lyrics)
            self.second_window.label.update()
            widget = self.window
            display_monitor = 1
            monitor = QDesktopWidget().screenGeometry(display_monitor)
            widget.move(monitor.left(), monitor.top())
            #widget.update()
            widget.showFullScreen()
            """
        else:
            ly = lyrics.text()
            self.label_2.setText(ly)
            self.lyrics = ly

    def filter_search(self, keyword):
        datalist = self.filtered_song_list
        keyword = keyword.upper()
        done_filter = (
            [val for val in datalist if re.search(r'' + keyword, val)])
        print(datalist)
        self.song_listwidget.clear()
        for i in range(len(done_filter)):
            self.song_listwidget.addItem(done_filter[i])

    def go_live(self):

        if self.islive == False:
            self.live_btn.setStyleSheet("#live_btn{\n"
                                        "    color: #ffffff;\n"
                                        "    background-color: rgb(198, 40, 40);\n"
                                        "    border: none;\n"
                                        "    padding: 10px;\n"
                                        "    border-radius: 7px;\n"
                                        "}")
            self.islive = True
            self.window = QtWidgets.QMainWindow()
            self.second_window = Ui_UI_second()
            self.second_window.setupUi(self.window)
            self.second_window.label.setText(self.lyrics)
            # check if clear btn is active
            if self.isclear == True:
                self.second_window.label.setText('')
            # self.window.show()

            widget = self.window
            display_monitor = 1
            monitor = QDesktopWidget().screenGeometry(display_monitor)
            widget.move(monitor.left(), monitor.top())
            widget.showFullScreen()
        else:
            self.islive = False
            self.window = QtWidgets.QMainWindow()
            self.second_window = Ui_UI_second()
            self.second_window.setupUi(self.window)
            self.second_window.label.setText(self.lyrics)
            self.window.hide()
            self.live_btn.setStyleSheet("#live_btn{\n"
                                        "    color: #ffffff;\n"
                                        "    background-color: grey;\n"
                                        "    border: none;\n"
                                        "    padding: 10px;\n"
                                        "    border-radius: 7px;\n"
                                        "}")

    def closeEvent(self, event):
        # close second window if the primary window closed
        self.window = QtWidgets.QMainWindow()
        self.window.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    iWindow = Ui_MainWindow()
    iWindow.showMaximized()
    sys.exit(app.exec_())
