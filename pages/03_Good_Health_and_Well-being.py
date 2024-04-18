import streamlit as st
import streamlit.components.v1 as components

def create_goal_section(number, goal, subdescription, iframe_url):
    st.markdown(f"### {number}. {goal}")
    st.markdown(f"_{subdescription}_")
    components.iframe(iframe_url, height=500)

st.title('Mongolian SDG Tracker төсөл: Зорилт #3 - Эрүүл Мэндийг Дэмжих')

#JSON table
goals_data = [
    {
        "number": "3.1",
        "goal": "2030 он гэхэд 100,000 амьд төрөлт тутамд эхийн эндэгдлийн түвшнийг 70-аас доош болгон бууруулах",
        "subgoals": [
            {
                "number": "3.1.1",
                "description": "Эхийн эндэгдлийн харьцаа (100 000 амьд төрөлтөд ногдох)",
                "iframe_url": "https://ourworldindata.org/grapher/maternal-mortality-ratio-who-gho"
            },
            {
                "number": "3.1.2",
                "description": "Эмнэлгийн мэргэжилтний эх барьсан төрөлтийн эзлэх хувь",
                "iframe_url": "https://ourworldindata.org/grapher/births-attended-by-health-staff-sdgs"
            }
        ]
    },
    {
        "number": "3.2",
        "goal": "2030 он гэхэд урьдчилан сэргийлэх боломжтой нялхсын болон 5 хүртэлх насны хүүхдийн эндэгдлийг арилгах",
        "subgoals": [
            {
                "number": "3.2.1",
                "description": "Тав хүртэлх насны хүүхдийн эндэгдлийн түвшин (1 000 амьд төрөлтөд ногдох)",
                "iframe_url": "https://ourworldindata.org/grapher/child-mortality-igme"
            },
            {
                "number": "3.2.2",
                "description": "Нярайн эндэгдлийн түвшин (1 000 амьд төрөлтөд ногдох)",
                "iframe_url": "https://ourworldindata.org/grapher/neonatal-mortality-wdi"
            }
        ]
    },
    {
        "number": "3.3",
        "goal": "2030 он гэхэд ДОХ, сүрьеэ, хумхаа өвчний тархалтыг дарах, элэгний үрэвсэл, усаар дамжин халдварладаг өвчин, бусад халдварт өвчинтэй тэмцэх",
        "subgoals": [
            {
                "number": "3.3.1",
                "description": "ХДХВ-ийн халдваргүй 1 000 хүн амд ногдох ХДХВ-ийн шинэ тохиолдлын тоо",
                "iframe_url": "https://ourworldindata.org/grapher/incidence-of-hiv-by-age?country=~MNG"
            },
            {
                "number": "3.3.2",
                "description": "Сүрьеэ өвчний тохиолдлын түвшин (1 000 хүн амд ногдох)",
                "iframe_url": "https://ourworldindata.org/grapher/incidence-of-tuberculosis-sdgs"
            },
            {
                "number": "3.3.3",
                "description": "100,000 хүн амд ногдох хумхаа өвчний тохиолдол",
                "iframe_url": "https://ourworldindata.org/grapher/incidence-of-malaria"
            },
            {
                "number": "3.3.4",
                "description": "В вирүст хепатит өвчний тохиолдлын түвшин (100 000 хүн амд ногдох)",
                "iframe_url": "https://ourworldindata.org/grapher/prevalence-of-hepatitis-b-surface-antigen"
            },
            {
                "number": "3.3.5",
                "description": "Халуун орны устсан өвчний эсрэг эмчилгээ шаардлагатай хүмүүсийн тоо",
                "iframe_url": "https://ourworldindata.org/grapher/interventions-ntds-sdgs"
            }
        ]
    },
    {
        "number": "3.4",
        "goal": "2030 он гэхэд халдварт өвчнөөс урьдчилан сэргийлэх, түүнийг эмчлэх замаар халдварт өвчнөөс үүдэлтэй цаг бусаар нас барах явдлыг гуравны нэгээр бууруулах",
        "subgoals": [
            {
                "number": "3.4.1",
                "description": "Зүрх судасны өвчин, хорт хавдар, чихрийн шижин болон амьсгалын замын архаг өвчний шалтгаант нас баралтын түвшин (10 000 хүн амд ногдох)",
                "iframe_url": "https://ourworldindata.org/grapher/mortality-from-ncds-sdgs"
            },
            {
                "number": "3.4.2",
                "description": "Амиа хорлож нас барсан тохиолдлын түвшин (10 000 хүн амд ногдох)",
                "iframe_url": "https://ourworldindata.org/grapher/death-rate-from-suicides-ghe"
            }
        ]
    },
    {
        "number": "3.5",
        "goal": "Мансууруулах бодис хэтрүүлэн хэрэглэх, түүний дотор хар тамхи хэтрүүлэх хэрэглэх, архийг эрүүл мэндэд хортойгоор хэрэглэх явдлаас урьдчилан сэргийлэх, эмчлэх үйл ажиллагааг сайжруулах",
        "subgoals": [
            {
                "number": "3.5.1",
                "description": "Мансууруулах бодис хэрэглэх эмгэгтэй хүмүүсийн эмчилгээний хамралтын хувь (эмийн эмчилгээ, сэтгэлзүйн эмчилгээ, нийгмийн нөхөн сэргээх-нийгэмшүүлэх тусламж)",
                "iframe_url": "https://ourworldindata.org/grapher/population-with-alcohol-use-disorders"
            },
            {
                "number": "3.5.2",
                "description": "Нэг хүнд (15 ба түүнээс дээш насны) жилд ногдох цэвэр спиртийн хэмжээгээр илэрхийлэгдсэн согтууруулах ундааны хэмжээ, литрээр",
                "iframe_url": "https://ourworldindata.org/grapher/total-alcohol-consumption-per-capita-litres-of-pure-alcohol"
            }
        ]
    },
    {
        "number": "3.6",
        "goal": "2020 он гэхэд замын хөдөлгөөний ослын улмаас нас барсан, гэмтэж бэртсэн хүний тоог хоёр дахин бууруулах",
        "subgoals": [
            {
                "number": "3.6.1",
                "description": "Зам тээврийн ослын шалтгаант нас баралтын түвшин (100 000 хүн амд ногдох)",
                "iframe_url": "https://ourworldindata.org/grapher/death-rate-road-traffic-injuries"
            }
        ]
    },
    {
        "number": "3.7",
        "goal": "2030 он гэхэд гэр бүл төлөвлөлт, мэдээлэл, мэдлэг өгөх, нөхөн үржихүйн эрүүл мэндийн асуудлыг үндэсний бодлого, хөтөлбөр тусгах зорилгоор бэлгийн болон нөхөн үржихүйн эрүүл мэндийн тусламж үйлчилгээг хүн бүрт хүргэх",
        "subgoals": [
            {
                "number": "3.7.1",
                "description": "Гэр бүл төлөвлөлтийн хэрэгцээ нь жирэмслэхээс сэргийлэх орчин үеийн аргаар хангагдсан нөхөн үржихүйн насны (15-49) эмэгтэйчүүдийн хувь",
                "iframe_url": "https://ourworldindata.org/grapher/share-of-married-women-ages-15-49-years-whose-need-for-family-planning-is-satisfied"
            },
            {
                "number": "3.7.2",
                "description": "Өсвөр насны 1 000 эмэгтэйд ногдох төрөлтийн түвшин (10-14, 15-19 нас)",
                "iframe_url": "https://ourworldindata.org/grapher/adolescent-fertility"
            }
        ]
    },
    {
        "number": "3.8",
        "goal": "Хүн бүрт эрүүл мэндийн үйлчилгээ, түүний дотор санхүүгийн эрсдэлийн хамгаалалт, нэн шаардлагатай чанартай эрүүл мэндийн тусламж үйлчилгээ, аюулгүй, үр дүнтэй, чанартай, боломжийн үнэтэй нэн шаардлагатай эм, вакциныг хүртээмжтэй хүргэх",
        "subgoals": [
            {
                "number": "3.8.1",
                "description": "Эрүүл мэндийн зайлшгүй шаардлагатай тусламж үйлчилгээний хамралтын хувь",
                "iframe_url": "https://ourworldindata.org/grapher/universal-health-coverage-index"
            },
            {
                "number": "3.8.2",
                "description": "Өрхийн зардлын дийлэнх хувийг эрүүл мэнддээ зарцуулдаг хүн амын эзлэх хувь",
                "iframe_url": "https://ourworldindata.org/grapher/large-household-expenditures-health"
            }
        ]
    },
    {
        "number": "3.9",
        "goal": "2030 он гэхэд аюултай химийн бодис, агаар, ус, хөрсний бохирдол, халдвараас болж үхсэн, өвдсөн хүмүүсийн тоог үлэмж хэмжээгээр бууруулах",
        "subgoals": [
            {
                "number": "3.9.1",
                "description": "Дотоод болон гадаад орчны агаарын бохирдлоор нөхцөлдсөн нас баралтын түвшин (100 000 хүн амд ногдох)",
                "iframe_url": "https://ourworldindata.org/grapher/death-rate-household-and-ambient-air-pollution"
            },
            {
                "number": "3.9.2",
                "description": "Баталгаагүй ундны ус, эрүүл ахуйн шаардлага хангаагүй ариун цэвэр усны дамжуулалт өвчний түвшин (100 000 хүн амд ногдох)",
                "iframe_url": "https://ourworldindata.org/grapher/mortality-rate-attributable-to-wash"
            },
            {
                "number": "3.9.3",
                "description": "Санамсаргүй хордох, хорт бодист өртснөөс шалтгаалсан нас баралтын түвшин (100 000 хүн амд ногдох)",
                "iframe_url": "https://ourworldindata.org/grapher/death-rate-from-poisonings"
            }
        ]
    },
    {
        "number": "3.A",
        "goal": "Боломжтой гэж үзвэл Тамхины хяналтын тухай Дэлхийн эрүүл мэндийн байгууллагын суурь конвенцийн хэрэгжилтийг сайжруулах",
        "subgoals": [
            {
                "number": "3.A.1",
                "description": "15 ба түүнээс дээш насны хүн амын дундах тамхи таталтын тархалт",
                "iframe_url": "https://ourworldindata.org/grapher/prevalence-of-tobacco-use-sdgs"
            }
        ]
    },
    {
        "number": "3.B",
        "goal": "Хөгжиж буй орнуудад эхлээд нөлөөлдөг халдварт болон халдварт бус өвчний эм, вакцины судалгаа хөгжлийн ажлыг дэмжиж, нийтийн эрүүл мэндийг хамгаалах уян хатан байдлын тухайд Худалдаанд холбогдолтой оюуны өмчийн асуудлын хэлэлцээр, нийтийн эрүүл мэндийн тухай Дохагийн тунхаглалын дагуу боломжийн үнэтэй нэн шаардлагатай эм, вакцины хангамжийг сайжруулах, хүн бүрийг эм авч хэрэглэх боломжоор хангах",
        "subgoals": [
            {
                "number": "3.B.1",
                "description": "Үндэсний хөтөлбөрт тусгагдсан бүх төрлийн вакцинжуулалтад хамрагдсан зорилтот хүн амын эзлэх хувь",
                "iframe_url": "https://ourworldindata.org/grapher/share-of-children-immunized-dtp3?country=~MNG"
            },
            {
                "number": "3.B.2",
                "description": "Эрүүл мэндийн судалгаа, эрүүл мэндийн анхан шатны салбарт үзүүлэх хөгжлийн албан ёсны нийт цэвэр тусламж",
                "iframe_url": "https://ourworldindata.org/grapher/net-oda-to-medical-research"
            },
            {
                "number": "3.B.3",
                "description": "Зайлшгүй шаардлагатай эмээр тасалдалгүй хангах хүрэлцэхүйц нөөцтэй, бэлэн байдлыг хангаж ажилладаг эрүүл мэндийн байгууллагуудын эзлэх хувь",
                "iframe_url": "https://ourworldindata.org/grapher/share-of-health-facilities-with-essential-medicines?country=~MNG"
            }
        ]
    },
    {
        "number": "3.C",
        "goal": "Хөгжиж буй орнууд, ялангуяа нэн буурай хөгжилтэй орон, жижиг арлын хөгжиж буй орнуудад эрүүл мэндийн санхүүжилтийг ихээхэн хэмжээгээр нэмэгдүүлж, эрүүл мэндийн салбарын ажилтнуудыг ажилд авах, хөгжүүлэх, сургах, тогтвор суурьшилтай ажиллуулах явдлыг сайжруулах",
        "subgoals": [
            {
                "number": "3.C.1",
                "description": "Эрүүл мэндийн ажилтнуудын нягтрал, тархалт",
                "iframe_url": "https://ourworldindata.org/grapher/physicians-per-1000-people"
            }
        ]
    },
    {
        "number": "3.D",
        "goal": "Урьдчилан сэрэмжлүүлэх, эрсдэлийг бууруулах, эрсдэлийг бууруулах, олон улсын болон үндэсний эрүүл мэндийн эрсдэлийг удирдах зорилгоор, бүх улс орнууд, ялангуяа хөгжиж буй улс орнуудын чадавхыг бэхжүүлэх",
        "subgoals": [
            {
                "number": "3.D.1",
                "description": "Олон улсын эрүүл мэндийн дүрмийг хэрэгжүүлэх чадавх, нийгмийн эрүүл мэндийн ноцтой үеийн бэлэн байдал",
                "iframe_url": "https://ourworldindata.org/grapher/ihr-core-capacity-index-sdgs?country=~MNG"
            }
        ]
    }
]


def create_goal_section(number, goal, subgoals):
    st.markdown(f"### {number}. {goal}")
    for subgoal in subgoals:
        st.markdown(f"_{subgoal['number']}. {subgoal['description']}_")
        if 'iframe_url' in subgoal:
            components.iframe(subgoal['iframe_url'], height=500)
        else:
            st.markdown("⚠️ Not available ⚠️")

for data in goals_data:
    create_goal_section(
        number=data["number"],
        goal=data["goal"],
        subgoals=data["subgoals"]
    )