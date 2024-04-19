import streamlit as st
import streamlit.components.v1 as components

def create_goal_section(number, goal, subdescription, iframe_url):
    st.markdown(f"### {number}. {goal}")
    st.markdown(f"_{subdescription}_")
    components.iframe(iframe_url, height=500)

st.title('Mongolian SDG Tracker төсөл: Зорилт #16 - ')
st.write('lorem ipsum dolor')

#JSON table
goals_data = [
    {
        "number": "16.1",
        "goal": "Хүчирхийллийн бүх хэлбэр, нас баралтын холбогдолтой түвшнийг үлэмж хэмжээгээр бууруулах",
        "subgoals": [
            {
                "number": "16.1.1",
                "description": "100,000 хүн амд ногдох санаатай аллагын хохирогчдын тоо, хүйсээр, насны бүлгээр",
                "iframe_url": "https://ourworldindata.org/grapher/homicide-rate-unodc"
            },
            {
                "number": "16.1.2",
                "description": "100,000 хүн амд ногдох зөрчлөөс үүдэлтэй нас баралт, хүйсээр, насны бүлгээр, тохиолдлоор",
                "iframe_url": "https://ourworldindata.org/grapher/deaths-in-armed-conflicts-by-country"
            },
            {
                "number": "16.1.3",
                "description": "Сүүлийн 12 сарын дотор бие бялдар, сэтгэл санааны, бэлгийн хүчирхийлэлд өртсөн хүн амын эзлэх хувь"
            },
            {
                "number": "16.1.4",
                "description": "Амьдардаг орчиндоо ганцаараа алхахад аюулгүй байдлыг мэдэрдэг хүн амын эзлэх хувь"
            }
        ]
    },
    {
        "number": "16.2",
        "goal": "Хүүхэдтэй зэрлэгээр харьцах, тэднийг мөлжих, наймаалах, тамлан зовоох, хүүхдийн эсрэг хүчирхийллийн бүх хэлбэрийг зогсоох устгах",
        "subgoals": [
            {
                "number": "16.2.1",
                "description": "Сүүлийн нэг сард асран хамгаалагчаасаа ямар нэг бие махбодын шийтгэл болон сэтгэл санааны түрэмгийлэлд өртсөн 1-17 насны хүүхдийн эзлэх хувь",
                "iframe_url": "https://ourworldindata.org/grapher/share-of-children-who-experienced-violence"
            },
            {
                "number": "16.2.2",
                "description": "100,000 хүнд ногдох хүн худалдаалах гэмт хэргийн хохирогчдын тоо, хүйсээр, насны бүлгээр, мөлжлөгийн хэлбэрээр"
            },
            {
                "number": "16.2.3",
                "description": "18 хүртэлх насандаа бэлгийн хүчирхийлэлд өртөж байсан 18-29 насны эрэгтэй, эмэгтэйчүүдийн эзлэх хувь"
            }
        ]
    },
    {
        "number": "16.3",
        "goal": "Олон улсын болон үндэсний түвшинд хууль ёсыг хөхүүлэн дэмжих, хүн бүрийг хуулиар хамгаалуулах тэгш боломжоор хангах",
        "subgoals": [
            {
                "number": "16.3.1",
                "description": "Өмнөх 12 сарын хугацаанд хүчирхийллийн хохирогч болсноо эрх бүхий байгууллага болон бусад албан ёсоор хүлээн зөвшөөрөгдсөн зөрчил шийдвэрлэх байгууллагад мэдээлсэн хохирогчдын эзлэх хувь"
            },
            {
                "number": "16.3.2",
                "description": "Нийт шоронгийн хоригдогсдын дотор сэжигтнээр татагдсан хүний эзлэх хувь",
                "iframe_url": "https://ourworldindata.org/grapher/unsentenced-detainees-as-proportion-of-prison-population"
            }
        ]
    },
    {
        "number": "16.4",
        "goal": "2030 он гэхэд санхүүгийн болон галт зэвсгийн хууль бус урсгалыг үлэмж хэмжээгээр багасгаж, хулгайлагдсан эд хөрөнгийг буцаан олгох, нөхөн төлөөллийн ажлыг сайжруулах, зохион байгуулалттай гэмт хэргийн бүх хэлбэртэй тэмцэх",
        "subgoals": [
            {
                "number": "16.4.1",
                "description": "Дотоод, гадаад санхүүгийн хууль бус урсгалын нийт хэмжээ, тухайн үеийн ам.долларын ханшаар"
            },
            {
                "number": "16.4.2",
                "description": "Олон улсын гэрээ хэлэлцээрийн дагуу эрх бүхий байгууллагаас хууль бус гарал үүслийг нь мөрдөж тогтоосон хураагдсан, олдсон, тушаасан галт зэвсгийн эзлэх хувь"
            }
        ]
    },
    {
        "number": "16.5",
        "goal": "Авлига, хээл хахуулийн бүх хэлбэрийг үлэмж хэмжээгээр багасгах",
        "subgoals": [
            {
                "number": "16.5.1",
                "description": "Сүүлийн 12 сарын хугацаанд, төрийн албан хаагчид авлига өгсөн, эсвэл төрийн албан хаагчаас авилга өгөхийг гуйлгуулсан, төрийн албан хаагчтай хамгийн багадаа нэг удаа холбогдсон хүмүүсийн эзлэх хувь",
                "iframe_url": "https://ourworldindata.org/grapher/bribery-prevalence-un"
            },
            {
                "number": "16.5.2",
                "description": "Сүүлийн 12 сарын хугацаанд, төрийн албан хаагчид авлига өгсөн, эсвэл төрийн албан хаагчаас авилга өгөхийг гуйлгуулсан, төрийн албан хаагчтай хамгийн багадаа нэг удаа холбогдсон аж ахуй нэгжийн эзлэх хувь",
                "iframe_url": "https://ourworldindata.org/grapher/bribery-incidence-for-firms"
            }
        ]
    },
    {
        "number": "16.6",
        "goal": "Бүх түвшинд үр дүнтэй, хариуцлагатай, ил тод үйл ажиллагаатай институтийг хэвшүүлэх",
        "subgoals": [
            {
                "number": "16.6.1",
                "description": "Анх батлагдсан төсөвт засгийн газрын зардлын эзлэх хувь",
                "iframe_url": "https://ourworldindata.org/grapher/govt-expenditure-share-budget"
            },
            {
                "number": "16.6.2",
                "description": "Төрийн албаар үйлчлүүлсэн сүүлийн үйлчилгээндээ сэтгэл хангалуун байгаа хүн амын эзлэх хувь"
            }
        ]
    },
    {
        "number": "16.7",
        "goal": "Бүх түвшинд хурдан шуурхай, бүх талын оролцоог хангасан, оролцооны аргад тулгуурласан, төлөөллийн шийдвэр гаргадаг болох",
        "subgoals": [
            {
                "number": "16.7.1",
                "description": "Үндэсний болон орон нутгийн хууль тогтоох байгууллага, төрийн алба, шүүхийн байгууллагад ажиллагчдын нийт төрийн албан ажиллагчдад эзлэх хувь (хүйс, насны бүлгээр, хөгжлийн бэрхшээлтэй хүн амаар, хүн амын бүлгээр)",
                "iframe_url": "https://ourworldindata.org/grapher/share-of-women-in-parliament"
            },
            {
                "number": "16.7.2",
                "description": "Шийдвэр гаргалт нь хүртээмжтэй, хариуцлагатай байдагт итгэдэг хүн амын эзлэх хувь, хүйсээр, насны бүлгээр, хөгжлийн бэрхшээлтэй хүн амаар, хүн амын бүлгээр"
            }
        ]
    },
    {
        "number": "16.8",
        "goal": "Дэлхийн засаглалын үйл ажиллагаанд хөгжиж буй улс орнуудыг оролцуулах явдлыг нэмэгдүүлэх, сайжруулах",
        "subgoals": [
            {
                "number": "16.8.1",
                "description": "Олон улсын байгууллагад хөгжиж буй орнуудын гишүүнчлэл, санал өгөх эрхийн эзлэх хувь",
                "iframe_url": "https://ourworldindata.org/grapher/proportion-of-members-of-developing-countries-in-international-organizations?country=~MNG"
            }
        ]
    },
    {
        "number": "16.9",
        "goal": "2030 он гэхэд хүн бүрт албан ёсны үнэмлэх, түүний дотор төрсний гэрчилгээ олгох",
        "subgoals": [
            {
                "number": "16.9.1",
                "description": "Төрөлтийг нь иргэний бүртгэлийн байгууллага бүртгэсэн 5-аас доош насны хүүхдүүдийн эзлэх хувь, насны бүлгээр"
            }
        ]
    },
    {
        "number": "16.10",
        "goal": "Үндэсний хууль тогтоомж болон олон улсын гэрээ хэлэлцээрт нийцүүлэн олон нийтийг мэдээлэл олж авах боломжоор хангах, үндсэн эрх чөлөөг хамгаалах",
        "subgoals": [
            {
                "number": "16.10.1",
                "description": "Сүүлийн 12 сарын хугацаанд амийг хөнөөсөн, хулгайлсан, хүчээр сураггүй алга болгосон, дур зоргоор баривчлан эрүүдэн шүүсэн сэтгүүлчид, хэвлэл мэдээллийн ажилтнууд, ҮЭ-ийн болон хүний эрхийг хамгаалах байгууллагын ажилтнуудын батлагдсан тоо",
                "iframe_url": "https://ourworldindata.org/grapher/cases-of-killed-human-rights-defenders-journalists-trade-unionists?country=Central+and+Southern+Asia+%28UN%29~Eastern+and+South-Eastern+Asia+%28UN%29"
            },
            {
                "number": "16.10.2",
                "description": "Олон нийтийн мэдээлэл авах эрхийг үндсэн хууль, хууль тогтоомж, дүрэм журам, бодлогын түвшинд баталгаажуулж, хуульчилсан эсэх",
                "iframe_url": "https://ourworldindata.org/grapher/countries-that-adopt-guarantees-for-public-access-to-information"
            }
        ]
    },
    {
        "number": "16.a",
        "goal": "Хүчирхийллээс сэргийлэх, терроризм, гэмт хэрэгтэй тэмцэх зорилгоор бүх түвшинд, ялангуяа хөгжиж буй орнуудын чадавхыг бэхжүүлэх үүднээс олон улсын хамтын ажиллагаагаар дамжуулан үндэсний холбогдох байгууллагуудын үйл ажиллагааг сайжруулах",
        "subgoals": [
            {
                "number": "16.a.1",
                "description": "Парисын зарчмыг мөрдлөг болгодог хүний эрхийн бие даасан байгууллагатай эсэх",
                "iframe_url": "https://ourworldindata.org/grapher/share-countries-accredited-independent-national-human-rights-institutions?country=Central+and+Southern+Asia+%28UN%29~OWID_WRL~Eastern+and+South-Eastern+Asia+%28UN%29"
            }
        ]
    },
    {
        "number": "16.b",
        "goal": "Тогтвортой хөгжлийн үл ялгаварласан хууль, бодлогыг хөхүүлэн дэмжиж, мөрдүүлэх",
        "subgoals": [
            {
                "number": "16.b.1",
                "description": "Олон улсын хүний ​​эрхийн хуулиар хориглосон ялгаварлан гадуурхах явцын хууль, бодлогыг хөхүүлэх, мөрдүүлэх байгууллага болон бусад байгууллагуудын тоо",
                "iframe_url": "https://ourworldindata.org/grapher/share-of-the-population-reporting-having-felt-discriminated-against"
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