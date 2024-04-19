import streamlit as st
import streamlit.components.v1 as components


def create_goal_section(number, goal, subdescription, iframe_url):
    st.markdown(f"### {number}. {goal}")
    st.markdown(f"_{subdescription}_")
    components.iframe(iframe_url, height=500)

st.title('Зорилт 2. Өлсгөлөнг зогсоох')
st.markdown('Өлсгөлөнг бүр мөсөн устгаж, хүнсний аюулгүй байдлыг хангаж, хоол тэжээл байдлыг сайжруулж, тогтвортой хөдөө аж ахуйг хөхүүлэн дэмжих')
#JSON Table
goals_data = [
    {
        "number": "2.1",
        "goal": "2030 он гэхэд ядуурлыг эцэс болгож, хүн бүрийг, ялангуяа ядуу болон эмзэг бүлгийн хүмүүс, түүний дотор нялхсыг эрүүл, шим тэжээллэг, хүрэлцэхүйц хоол хүнсийг жилийн турш авах боломжоор хангах",
        "subgoals": [
            {
                "number": "2.1.1",
                "description": "Хоол тэжээлийн дутагдлын тархалт (POU)",
                "iframe_url": "https://ourworldindata.org/grapher/prevalence-of-undernourishment?country=~MNG"
            },
            {
                "number": "2.1.2",
                "description": "Хүнсний баталгаат байдлын алдагдлыг тооцох хэмжүүрт үндэслэн баталгаагүй хоол, хүнсний дунд болон хүнд хэлбэрийн байдалд өртсөн хүн амын тархалт (FIES)",
                "iframe_url": "https://ourworldindata.org/grapher/share-of-population-with-moderate-or-severe-food-insecurity?region=Asia"
            }
        ]
    },
    {
        "number": "2.2",
        "goal": "2025 он гэхэд 5 хүртэлх насны өсөлтийн хоцролттой, туранхай хүүхдийн талаар олон улсын хэмжээнд хүлээн зөвшөөрсөн зорилтуудад хүрэх замаар хоол тэжээлийн дутагдлын бүх хэлбэрийг арилгаж, өсвөр насны охид, жирэмсэн болон хүүхдээ хөхөөрөө хооллож буй эмэгтэйчүүд, өндөр настнуудын хоол тэжээлийн хэрэгцээг 2030 он гэхэд хангах",
        "subgoals": [
            {
                "number": "2.2.1",
                "description": "Өсөлтийн хоцролттой 5 хүртэлх насны хүүхдийн тархалт (Биеийн өндөр, насны харьцаа нь ДЭМБ-аас боловсруулсан хүүхдийн өсөлтийн стандарт харьцааны голчоос \"- 2 стандарт хазайлтаас\" доогуур)",
                "iframe_url": "https://ourworldindata.org/grapher/share-of-children-younger-than-5-who-suffer-from-stunting?region=Asia"
            },
            {
                "number": "2.2.2",
                "description": "Хоол тэжээлийн дутагдалтай 5 хүртэлх насны хүүхдийн тархалт, төрлөөр (туранхай ба илүүдэл жинтэй), (Биеийн жин, өндрийн харьцаа нь ДЭМБ-аас боловсруулсан хүүхдийн өсөлтийн стандарт харьцааны голчоос \" +2 стандарт хазайлтаас\" их эсвэл \"- 2 стандарт хазайлтаас\" доогуур)",
                "iframe_url": "https://ourworldindata.org/grapher/share-of-children-with-a-weight-too-low-for-their-height-wasting"
            }
        ]
    },
    {
        "number": "2.3",
        "goal": "Нэмүү өртөг шингээх, хөдөө аж ахуйн бус ажил эрхлэлтийг бий болгох үүднээс газар, үр ашигтай бусад баялаг, мэдээлэл мэдлэг, санхүүгийн үйлчилгээ, зах зээл, нөөц боломжийг ашиглах эрх тэгш, баталгаатай боломжийг бүрдүүлэх замаар жижиг хэмжээний хүнсний үйлдвэрлэгчид, ялангуяа нутгийн иргэд, гэр бүлийн фермерийн аж ахуй эрхлэгчид, малчид, загасны аж ахуй эрхлэгчдийн хөдөө аж ахуйн бүтээмж, орлогыг 2030 он гэхэд 2 дахин нэмэгдүүлэх",
        "subgoals": [
            {
                "number": "2.3.1",
                "description": "1 ажилтанд ногдох бүтээгдэхүүн үйлдвэрлэлийн хэмжээ, Фермийн аж ахуй/ бэлчээрийн мал аж ахуй/ ойн аж ахуйн нэгжийн хэмжээгээр",
                "iframe_url": "https://ourworldindata.org/grapher/productivity-of-small-scale-food-producers"
            },
            {
                "number": "2.3.2",
                "description": "Хоол хүнсний жижиг, дунд үйлдвэрлэл эрхлэгчдийн дундаж орлого, хүйс, үндсэн засаг захиргаагааны нэгжээр",
                "iframe_url": "https://ourworldindata.org/grapher/income-small-scale-food-producers"
            }
        ]
    },
    {
        "number": "2.4",
        "goal": "2030 он гэхэд хүнс үйлдвэрлэлийн тогтвортой системийг бий болгож, бүтээмж, үйлдвэрлэлийг нэмэгдүүлэх, экосистемийн тэнцвэрийг хангаж чадах, цаг уурын өөрчлөлт, эрс тэс цаг агаар, ган зуд, үер, бусад гамшигт үзэгдэлд дасан зохицох чадавхыг бэхжүүлэх, газар хөрсний чанарыг тасралтгүй сайжруулах хөдөө аж ахуйн уян хатан арга туршлагыг нэвтрүүлэх",
        "subgoals": [
            {
                "number": "2.4.1",
                "description": "Бүтээмжтэй, тогтвортой хөдөө аж ахуйн үйл ажиллагаанд ашиглагддаг хөдөө аж ахуйн газар нутгийн эзлэх хувь"
            }
        ]
    },
    {
        "number": "2.5",
        "goal": "2030 он гэхэд олон улс, бүс нутаг, үндэсний түвшний зохистой удирдлага, зохион байгуулалттай, олон төрлийн үр, ургамлын сантай банкаар дамжуулан үр, тариалах ургамал, фермерийн болон гэрийн тэжээвэр амьтан, тэдгээртэй холбоотой зэрлэг ан амьтдын генетикийн олон янз байдлыг хадгалж, олон улсын хэмжээнд тохиролцсоны дагуу генетикийн нөөц баялаг, уламжлалт холбогдох мэдлэгийг ашигласнаар гарах үр шимийг хүртэх, эрх тэгш, шударга зарчмаар солилцох нөхцөлийг бүрдүүлэх",
        "subgoals": [
            {
                "number": "2.5.1",
                "description": "Хүнс, хөдөө аж ахуйн чиглэлээр дунд болон урт хугацаанд ашиглахаар зориулалтын байгууламжид хадгалсан ургамал, амьтны генетикийн нөөц",
                "iframe_url": "https://ourworldindata.org/grapher/number-of-accessions-of-plant-genetic-resources-secured-in-conservation-facilities"
            },
            {
                "number": "2.5.2",
                "description": "Устах эрсдэлтэй, устах эрсдэлгүй, устах эрсдэлийн үл мэдэгдэх түвшинд байгаа нутгийн үүлдрийн малын эзлэх хувь",
                "iframe_url": "https://ourworldindata.org/grapher/proportion-of-local-breeds-at-risk-of-extinction"
            }
        ]
    },
    {
        "number": "2.A",
        "goal": "Хөгжиж буй орнуудад, ялангуяа нэн буурай хөгжилтэй орнуудын хөдөө аж ахуйн бүтээмжийн чадамжийг сайжруулах үүднээс хөдөөгийн дэд бүтэц, хөдөө аж ахуйн судалгаа, хөдөө аж ахуйг өргөжүүлэх үйлчилгээ, технологийн хөгжил, ургамал болон малын генийн банкны салбарт олон улсын хамтын ажиллагааг хөгжүүлэх замаар хөрөнгө оруулалтыг нэмэгдүүлэх",
        "subgoals": [
            {
                "number": "2.A.1",
                "description": "Засгийн газрын хөдөө аж ахуйд зориулсан Зардлын Индекс",
                "iframe_url": "https://ourworldindata.org/grapher/agriculture-orientation-index"
            },
            {
                "number": "2.A.2",
                "description": "ХАА-н салбарт зориулсан хөгжлийн албан ёсны тусламж, орлого, сая. ам доллар",
                "iframe_url": "https://ourworldindata.org/grapher/total-financial-assistance-and-flows-for-agriculture-by-recipient"
            }
        ]
    },
    {
        "number": "2.B",
        "goal": "Дохагийн хөгжлийн хөтөлбөрийн хүрээнд бий болсон эрх үүргийн дагуу хөдөө аж ахуйн экспортын татаас, түүнтэй адил экспортын арга хэмжээний бүх хэлбэрийг нэгэн зэрэг халах замаар дэлхийн хөдөө аж ахуйн зах зээлд байгаа худалдааны хязгаарлалт, гажуудлаас урьдчилан сэргийлэх, тэдгээрийг засах",
        "subgoals": [
            {
                "number": "2.B.1",
                "description": "Хөдөө аж ахуйн экспортын татаас",
                "iframe_url": "https://ourworldindata.org/grapher/agricultural-export-subsidies?country=~Asia+%28UN%29"
            }
        ]
    },
    {
        "number": "2.C",
        "goal": "Хүнсний үнэ хэт ихээр хэлбэлзэх байдлыг хязгаарлах үүднээс зах зээлийн мэдээлэл, түүний дотор хүнсний нөөцийн мэдээллийг шуурхай авах ажлыг хөнгөвчлөх, хүнсний бүтээгдэхүүний зах зээл, түүний үүсмэл хэрэгслийг зөв ажиллах нөхцөлийг бүрдүүлэх арга хэмжээ авах",
        "subgoals": [
            {
                "number": "2.C.1",
                "description": "Хүнсний үнийн огцом өөрчлөлтийн үзүүлэлт",
                "iframe_url": "https://ourworldindata.org/grapher/food-price-anomalies"
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
            st.markdown("Мэдээлэл байхгүй байна.")

for data in goals_data:
    create_goal_section(
        number=data["number"],
        goal=data["goal"],
        subgoals=data["subgoals"]
    )

st.divider()

st.markdown("<p style='text-align: center; color: black;'>All plots generated by Our World In Data are under CC-BY License of Fair Use.</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: black;'>2024 © Green Dot Climate</p>", unsafe_allow_html=True)