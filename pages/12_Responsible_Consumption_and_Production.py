import streamlit as st
import streamlit.components.v1 as components

def create_goal_section(number, goal, subdescription, iframe_url):
    st.markdown(f"### {number}. {goal}")
    st.markdown(f"_{subdescription}_")
    components.iframe(iframe_url, height=500)

st.title('Mongolian SDG Tracker төсөл: Зорилт #12 - ')
st.write('lorem ipsum dolor')

#JSON table
goals_data = [
  {
    "number": "12.1",
    "goal": "Хөгжиж буй орнуудын хөгжил, чадавх нөөц бололцоог харгалзан үзэж хөгжингүй орнууд хошуучлан бүх улс орнууд зохих арга хэмжээ авч хэрэгжүүлж, тогтвортой хэрэглээ, үйлдвэрлэлийн 10 жилийн хугацаатай хөтөлбөрийг хэрэгжүүлэх",
    "subgoals": [
      {
        "number": "12.1.1",
        "description": "Тогтвортой хэрэглээ үйлдвэрлэлийн талаар үндэсний төлөвлөгөөтэй эсвэл үндэсний төлөвлөгөөндөө эдгээрийг зорилт, үндсэн чиглэл болгон тусгасан эсэх"
      }
    ]
  },
  {
    "number": "12.2",
    "goal": "2030 он гэхэд байгалийн баялгийг үр ашигтай хэрэглэж, түүний тогтвортой менежментийг бүрдүүлэх",
    "subgoals": [
      {
        "number": "12.2.1",
        "description": "Материалын өгөөж (МӨ) ба нэг хүнд ноогдох МӨ, ДНБ-д ногдох материалын өгөөж",
        "iframe_url": "https://ourworldindata.org/grapher/material-footprint-per-capita"
      },
      {
        "number": "12.2.2",
        "description": "Дотоодын материалын хэрэглээ, нэг хүнд ногдох дотоодын материалын хэрэглээ, ДНБ-д ногдох дотоодын материалын хэрэглээ",
        "iframe_url": "https://ourworldindata.org/grapher/domestic-material-consumption-per-capita"
      }
    ]
  },
  {
    "number": "12.3",
    "goal": "2030 он гэхэд жижиглэн худалдааны болон хэрэглээний түвшинд нэг хүнд ногдох дэлхийн хүнсний хаягдлыг хоёр дахин багасгаж, үйлдвэрлэлийн болон нийлүүлэлтийн тогтолцоотой холбоотойгоор гарах хүнсний алдагдал, түүний дотор ургац хураалтын дараах алдагдлыг бууруулах",
    "subgoals": [
      {
        "number": "12.3.1",
        "description": "Дэлхийн хүнсний алдагдлын индекс",
        "iframe_url": "https://ourworldindata.org/grapher/global-food-loss-index?country=OWID_WRL~Central+and+Southern+Asia+%28UN%29"
      }
    ]
  },
  {
    "number": "12.4",
    "goal": "2020 он гэхэд хүлээн зөвшөөрөгдсөн олон улсын баримт бичигт нийцүүлэн химийн бодис болон бүх төрлийн хог хаягдлыг амьдралынх нь мөчлөгийн хугацаанд байгаль орчинд ээлтэй байдлаар зохицуулах",
    "subgoals": [
      {
        "number": "12.4.1",
        "description": "Аюултай хог хаягдал, бусад химийн бодисын тухай байгаль орчны олон улсын олон талт гэрээ, хэлэлцээрийн дагуу мэдээлэл солилцох үүргээ биелүүлж байгаа эсэх",
        "iframe_url": "https://ourworldindata.org/grapher/parties-to-multilateral-agreements-on-hazardous-waste?country=~MNG"
      },
      {
        "number": "12.4.2",
        "description": "Нэг хүнд ногдох аюултай хог хаягдал, устгасан хог хаягдлын эзлэх хувь, устгалын төрлөөр",
        "iframe_url": "https://ourworldindata.org/grapher/hazardous-waste-generated-per-capita"
      }
    ]
  },
  {
    "number": "12.5",
    "goal": "2030 он гэхэд хог хаягдлаас сэргийлэх, түүнийг бууруулах дахин боловсруулах, дахин хэрэглэх замаар хог хаягдал бий болгож буй хэмжээг үлэмж хэмжээгээр бууруулах",
    "subgoals": [
      {
        "number": "12.5.1",
        "description": "Хог хаягдлын дахин боловсруулалтын үндэсний түвшин, дахин боловсруулсан материал, тонноор",
        "iframe_url": ""
      }
    ]
  },
  {
    "number": "12.6",
    "goal": "Хувийн хэвшил, ялангуяа томоохон, үндэстэн дамнасан компаниудыг тогтвортой байдалд чиглэсэн арга ажиллагааг нэвтрүүлж, энэ талаарх мэдээллийг өөрсдийн үйл ажиллагааны тайландаа тусгаж байх явдлыг дэмжих",
    "subgoals": [
      {
        "number": "12.6.1",
        "description": "Тогтвортой байдлын тайланг хэвлэдэг компаниудын тоо",
        "iframe_url": "https://ourworldindata.org/grapher/companies-publishing-sustainability-reports-minimum-requirements"
      }
    ]
  },
  {
    "number": "12.7",
    "goal": "Үндэсний бодлого, тэргүүлэх чиглэлтэй нийцүүлэн тогтвортой байдалд чиглэсэн төрийн худалдан авах ажиллагааг дэмжих",
    "subgoals": [
      {
        "number": "12.7.1",
        "description": "Төрийн худалдан авах ажиллагааны тогтвортой бодлого, үйл ажиллагааны төлөвлөгөөтэй эсэх",
        "iframe_url": ""
      }
    ]
  },
  {
    "number": "12.8",
    "goal": "2030 он гэхэд хүн бүр тогтвортой хөгжил, байгаль дэлхийтэйгээ зохицон амьдрах амьдралын хэв маягийн талаар холбогдох мэдээлэл, мэдлэгтэй болсон байх",
    "subgoals": [
      {
        "number": "12.8.1",
        "description": "(i) Дэлхийн иргэний боловсрол уур амьсгалын өөрчлөлтийн талаар тусгасан (ii) тогтвортой хөгжлийн боловсролыг a) боловсролын үндэсний бодлого, (b) сургалтын хөтөлбөр, (c) багш нарын боловсрол болон (d) суралцагчийн үнэлгээнд тусгасан байдал",
        "iframe_url": "https://ourworldindata.org/grapher/mainstreaming-sustainable-development-into-teacher-education"
      }
    ]
  },
  {
    "number": "12.a",
    "goal": "Хэрэглээний болон үйлдвэрлэлийн илүү тогтвортой бүтцэд шилжих зорилгоор шинжлэх ухааны болон технологийн чадавхаа бэхжүүлэхэд хөгжиж буй орнуудыг дэмжих",
    "subgoals": [
      {
        "number": "12.a.1",
        "description": "Байгаль орчинд ээлтэй технологи, үйлдвэрлэл, тогтвортой хэрэглээнд зориулсан судалгаа, хөгжлийн тусламжийн хэмжээ",
        "iframe_url": "https://ourworldindata.org/grapher/renewable-electricity-generating-capacity-per-capita"
      }
    ]
  },
  {
    "number": "12.b",
    "goal": "Шинээр ажлын байр бий болгодог, орон нутгийн соёл, бүтээгдэхүүнийг хөхүүлэн дэмждэг тогтвортой аялал жуулчлалд тогтвортой хөгжлийн үзүүлж буй нөлөөнд хяналт шинжилгээ хийх арга хэрэгслийг боловсруулж, нэвтрүүлэх",
    "subgoals": [
      {
        "number": "12.b.1",
        "description": "Аялал жуулчлалын тогтвортой стратеги эсвэл бодлого, хяналт үнэлгээний арга хэрэгслийн хамт хэрэгжүүлсэн үйл ажиллагааны төлөвлөгөөний тоо",
        "iframe_url": "https://ourworldindata.org/grapher/implementation-of-tools-to-monitor-economic-and-environmental-tourism"
      }
    ]
  },
  {
    "number": "12.c",
    "goal": "Хөгжиж буй орнуудын онцгой хэрэгцээ шаардлага, нөхцөл байдлыг харгалзан үзэж, ядуу, эмзэг бүлгийн хүн амыг хамгаалах байдлаар өөрсдийн хөгжилд сөрөг нөлөө үзүүлж болохуйц нөлөөллийг багасгаж, үндэсний нөхцөл байдалд нийцүүлэн зах зээлийн гажилтыг арилгах, түүний дотор татварын бүтцийг өөрчлөх, байгаль орчин сөрөг нөлөө учруулж буй татаасыг аажмаар багасгах замаар үрэлгэн хэрэглээг өөгшүүлдэг шатах түлшний үр ашиггүй татаасыг оновчтой болгох",
    "subgoals": [
      {
        "number": "12.c.1",
        "description": "ДНБ-нд ногдох хатуу түлшний татаасны хэмжээ (үйлдвэрлэл, хэрэглээ), Нийт төсвийн зарлагад хатуу түлшинд зарцуулсан зардлын эзлэх хувь",
        "iframe_url": "https://ourworldindata.org/grapher/fossil-fuel-subsidies-gdp"
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