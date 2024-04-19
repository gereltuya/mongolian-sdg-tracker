import streamlit as st
import streamlit.components.v1 as components

def create_goal_section(number, goal, subdescription, iframe_url):
    st.markdown(f"### {number}. {goal}")
    st.markdown(f"_{subdescription}_")
    components.iframe(iframe_url, height=500)

st.title('Зорилт 9. Инновaци болон дэд бүтцийг хөгжүүлэх')

st.write('Уян хатан дэд бүтцийг байгуулж, хүртээмжтэй, тогтвортой аж үйлдвэржилтийг дэмжиж, инновацийг хөгжүүлэх')
#JSON table
goals_data = {
  "goals": [
    {
      "number": "9.1",
      "goal": "Хүн бүрт тэгш, хүртээмжтэй байх талыг голлон анхаарч эдийн засгийн хөгжил, хүний сайн сайхан аж байдлыг дэмжих чанартай, найдвартай, тогтвортой, уян хатан дэд бүтэц, түүний бүсийн болон хил дамнасан дэд бүтцийг хөгжүүлэх",
      "subgoals": [
        {
          "number": "9.1.1",
          "description": "Бүх улирлын туршид замаас 2 км зайтай амьдарч байгаа хөдөөгийн хүн амын эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/railways-passengers-carried-passenger-km"
        }
      ]
    },
    {
      "number": "9.2",
      "goal": "Хүртээмжтэй, тогтвортой аж үйлдвэржилтийг хөхүүлэн дэмжиж, 2030 он гэхэд үндэсний нөхцөл байдалтай уялдуулан ДНБ-нд аж үйлдвэрийн салбарын ажлын байрны эзлэх хувийг үлэмж хэмжээгээр нэмэгдүүлж, нэн буурай хөгжилтэй орнуудад энэ хувийг хоёр дахин өсгөх",
      "subgoals": [
        {
          "number": "9.2.1",
          "description": "ДНБ-д боловсруулах үйлдвэрлэлийн нэмэгдэл өртгийн эзлэх хувь, 1 хүнд ногдох боловсруулах үйлдвэрлэлийн нэмэгдэл өртөг",
          "iframe_url": "https://ourworldindata.org/grapher/manufacturing-value-added-to-gdp"
        },
        {
          "number": "9.2.2",
          "description": "Нийт ажиллагчдад боловсруулах салбарт ажиллагчдын эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/manufacturing-share-of-total-employment"
        }
      ]
    },
    {
      "number": "9.3",
      "goal": "Жижиг хэмжээний аж үйлдвэрийн болон бусад салбарын аж ахуй нэгжүүд, ялангуяа хөгжиж буй орнуудын эдгээр аж ахуй нэгжүүдийн санхүүгийн үйлчилгээ авах, түүний дотор хямд зээл авах, үйлдвэрлэл, зах зээл нэвтрэх боломжийг нэмэгдүүлэх",
      "subgoals": [
        {
          "number": "9.3.1",
          "description": "Нийт аж үйлдвэрийн салбарын нэмэгдэл өртөгт жижиг үйлдвэрлэлийн эзлэх хувь"
        },
        {
          "number": "9.3.2",
          "description": "Зээл авахаар бүртгүүлсэн болон зээлтэй жижиг үйлдвэрлэгчдийн эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/smalsmall-scale-industries-loan"
        }
      ]
    },
    {
      "number": "9.4",
      "goal": "2030 он гэхэд нөөц баялгийн хэрэглээний үр ашгийг нэмэгдүүлж, цэвэр, байгальд ээлтэй технологи, үйлдвэрлэлийн ажиллагааг нэвтрүүлж, бүх улс орнууд өөрсдийн нөөц чадавхдаа уялдуулан арга хэмжээ авч хэрэгжүүлж, аж үйлдвэрийн тогтвортой ажиллагааг хангах зорилгоор дэд бүтцийг хөгжүүлж, аж үйлдвэрийг боловсронгуй болгох",
      "subgoals": [
        {
          "number": "9.4.1",
          "description": "Нэмэгдэл өртгийн нэгжид ногдох нүүрстөрөгчийн ялгарлын хэмжээ",
          "iframe_url": "https://ourworldindata.org/grapher/co2-intensity"
        }
      ]
    },
    {
      "number": "9.5",
      "goal": "Бүх улс орнууд, ялангуяа хөгжиж буй орнуудын технологийн чадавхыг дээшлүүлэх, шинжлэх ухааны судалгаа шинжилгээний ажлыг сайжруулах, түүний дотор 2030 он гэхэд инновацийг дэмжих, 1 сая хүн ногдох судалгаа-хөгжлийн ажилтны тоог [x] хувиар нэмэгдүүлэх, судалгаа-хөгжилд зарцуулах төр, хувийн хэвшлийн зардлыг өсгөх",
      "subgoals": [
        {
          "number": "9.5.1",
          "description": "ДНБ-д Судалгаа, хөгжлийн салбарын зардлын эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/research-spending-gdp"
        },
        {
          "number": "9.5.2",
          "description": "1 сая оршин суугчдад ногдох орон тооны судлаачдын тоо",
          "iframe_url": "https://ourworldindata.org/grapher/researchers-in-rd-per-million-people"
        }
      ]
    },
    {
      "number": "9.a",
      "goal": "Африкийн улс орнууд, нэн буурай хөгжилтэй улс орнууд, далайд гарцгүй хөгжиж буй улс орнууд, жижиг арлын хөгжиж буй орнуудад үзүүлэх санхүү, технологи, техникийн туслалцаа дэмжлэгийг нэмэгдүүлэх замаар хөгжиж буй орнуудад тогтвортой, уян хатан дэд бүтцийг хөгжүүлэхэд туслах",
      "subgoals": [
        {
          "number": "9.a.1",
          "description": "\"Дэд бүтцэд зориулсан албан ёсны олон улсын тусламжийн нийт хэмжээ (Албан ёсны хөгжлийн тусламж болон бусад албан тусламж)\"",
          "iframe_url": "https://ourworldindata.org/grapher/total-oda-for-infrastructure-by-recipient"
        }
      ]
    },
    {
      "number": "9.b",
      "goal": "Бодлогын таатай орчныг хангах, тухайлбал аж үйлдвэрийн төрөлжилт, бараа бүтээгдэхүүнд нэмүү өртөг шингээх замаар хөгжиж буй орнуудын дотоодын технологийн хөгжил, судалгаа шинжилгээ, инновацийг дэмжих",
      "subgoals": [
        {
          "number": "9.b.1",
          "description": "ДНБ-нд дунд болон өндөр технологийн үйлдвэрийн салбарын нэмэгдэл өртгийн эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/total-manufacturing-value-added-from-high-tech"
        }
      ]
    },
    {
      "number": "9.c",
      "goal": "2020 он гэхэд мэдээлэл, холбооны технологийн хүртээмжийг үлэмж хэмжээгээр нэмэгдүүлж, нэн буурай хөгжилтэй орнуудын хүн амыг хямд үнэтэй интернетээр хангахыг эрмэлзэх",
      "subgoals": [
        {
          "number": "9.c.1",
          "description": "Хөдөлгөөнт холбооны сүлжээнд хамрагдсан нийт хүн амын эзлэх хувь, технологийн төрлөөр",
          "iframe_url": "https://ourworldindata.org/grapher/population-covered-by-mobile-network-by-network-capability?country=~MNG"
        }
      ]
    }
  ]
}

 

def create_goal_section(number, goal, subgoals):
    st.markdown(f"### {number}. {goal}")
    for subgoal in subgoals:
        st.markdown(f"_{subgoal['number']}. {subgoal['description']}_")
        if 'iframe_url' in subgoal:
            components.iframe(subgoal['iframe_url'], height=500)
        else:
            st.markdown("Мэдээлэл байхгүй байна.")

for data in goals_data["goals"]:
    create_goal_section(
        number=data["number"],
        goal=data["goal"],
        subgoals=data["subgoals"]
    )

st.divider()

st.markdown("<p style='text-align: center; color: black;'>All plots generated by Our World In Data are under CC-BY License of Fair Use.</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: black;'>2024 © Green Dot Climate</p>", unsafe_allow_html=True)