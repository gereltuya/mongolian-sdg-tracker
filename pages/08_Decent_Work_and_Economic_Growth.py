import streamlit as st
import streamlit.components.v1 as components

def create_goal_section(number, goal, subdescription, iframe_url):
    st.markdown(f"### {number}. {goal}")
    st.markdown(f"_{subdescription}_")
    components.iframe(iframe_url, height=500)

st.title('Зорилт 8. Зохистой хөдөлмөр ба эдийн засгийн өсөлт')

st.write('Тогтвортой, хүртээмжтэй эдийн засгийн өсөлт, бүрэн, бүтээмжтэй ажил эрхлэлт, зохистой хөдөлмөрийг хөхүүлэн дэмжих')

#JSON table
goals_data = {
  "goals": [
    {
      "number": "8.1",
      "goal": "Үндэсний нөхцөл байдалд нийцүүлэн нэг хүнд ногдох эдийн засгийн өсөлтийг хангаж, ялангуяа нэн буурай хөгжилтэй улс орнуудад жилийн ДНБ-ий өсөлтийг 7 хувьд байлгах",
      "subgoals": [
        {
          "number": "8.1.1",
          "description": "Зэрэгцүүлэх үнээр тооцсон нэг хүнд ногдох ДНБ-ны жилийн өсөлт",
          "iframe_url": "https://ourworldindata.org/grapher/gdp-per-capita-growth"
        }
      ]
    },
    {
      "number": "8.2",
      "goal": "Эдийн засгийг төрөлжилт, технологийн шинэчлэл, инновациар дамжуулан, түүний дотор өндөр өртөг шингэсэн, ажиллах хүч ихээр шаарддаг салбаруудад голлон анхаарч эдийн засгийн бүтээмжийн өндөр түвшинд хүрэх",
      "subgoals": [
        {
          "number": "8.2.1",
          "description": "Зэрэгцүүлэх үнээр тооцсон нэг ажиллагчид ногдох ДНБ-ны жилийн өсөлт",
          "iframe_url": "https://ourworldindata.org/grapher/growth-rate-of-real-gdp-per-employed-person"
        }
      ]
    },
    {
      "number": "8.3",
      "goal": "Бүтээмжтэй үйл ажиллагаа, зохистой ажлын байр бий болгох, аж ахуй эрхлэх, бүтээлч байдал, инновацийг дэмждэг хөгжлийн чиг баримжаатай бодлогыг хөхүүлэн дэмжиж, санхүүгийн үйлчилгээг хүртээмжтэй болгох замаар бичил, жижиг, дунд бизнесийг албан ёсны болгож, тэдгээрийн өсөлтийг дэмжих",
      "subgoals": [
        {
          "number": "8.3.1",
          "description": "Хөдөө аж ахуйн бус ажил эрхлэлтэд албан бус секторын ажил эрхлэлтийн эзлэх хувь, хүйсээр",
          "iframe_url": "https://ourworldindata.org/grapher/informal-employment-of-total-non-agricultural-employment"
        }
      ]
    },
    {
      "number": "8.4",
      "goal": "2030 он гэхэд хөгжингүй орнуудын хошуучлан тогтвортой хэрэглээ, үйлдвэрлэлийн 10 жилийн хөтөлбөрт нийцүүлэн байгаль орчны доройтлоос эдийн засгийн өсөлтийг ялгаатай авч үзэх гэсэн хүчин чармайлт, үйлдвэрлэл, хэрэглээний чиглэлээр дэлхийн баялгийн үр ашгийг аажмаар нэмэгдүүлэх",
      "subgoals": [
        {
          "number": "8.4.1",
          "description": "Материалын өгөөж (МӨ) ба нэг хүнд ноогдох МӨ, ДНБ-д ногдох материалын өгөөж",
          "iframe_url": "https://ourworldindata.org/grapher/material-footprint-per-capita"
        },
        {
          "number": "8.4.2",
          "description": "Дотоодын материалын хэрэглээ, нэг хүнд ногдох дотоодын материалын хэрэглээ, ДНБ-д ногдох дотоодын материалын хэрэглээ",
          "iframe_url": "https://ourworldindata.org/grapher/domestic-material-consumption-per-capita"
        }
      ]
    },
    {
      "number": "8.5",
      "goal": "2030 он гэхэд эрэгтэй, эмэгтэй бүх хүн, түүний дотор залуу болон хөгжлийн бэрхшээлтэй хүмүүсийг бүрэн, бүтээмжтэй ажил, зохистой хөдөлмөр эрхлүүлж, адил үнэ цэнэтэй ажилд адилхан цалин хөлс олгох",
      "subgoals": [
        {
          "number": "8.5.1",
          "description": "Эмэгтэй, эрэгтэй ажиллагчдын цагийн дундаж хөлс, ажил мэргэжлээр, насны бүлгээр, хөгжлийн бэрхшээлтэй иргэдээр"
        },
        {
          "number": "8.5.2",
          "description": "Ажилгүйдлийн түвшин, хүйсээр, насны бүлгээр, хөгжлийн бэрхшээлтэй иргэнээр",
          "iframe_url": "https://ourworldindata.org/grapher/unemployment-rate"
        }
      ]
    },
    {
      "number": "8.6",
      "goal": "2020 он гэхэд ажил эрхэлдэггүй, боловсрол эсвэл сургалтад хамрагдаагүй залуучуудын эзлэх хувийг үлэмж хэмжээгээр бууруулах",
      "subgoals": [
        {
          "number": "8.6.1",
          "description": "Боловсрол эзэмшээгүй, хөдөлмөр эрхлээгүй болон сургалтад хамрагдаагүй 15-24 насны залуучуудын эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/youth-not-in-education-employment-training"
        }
      ]
    },
    {
      "number": "8.7",
      "goal": "Хүүхдийн хөдөлмөрийн тэвчишгүй хэлбэрүүдийг хориглох, устгахад чиглэлээр шуурхай, үр дүнтэй арга хэмжээ авч, албадан хөдөлмөр хийлгэх явдлыг арилгаж, бүх хэлбэрийн хүүхдийн хөдөлмөр, түүний дотор хүүхдийг цэрэг болгон элсүүлэх, ашиглах явдлыг 2025 он гэхэд эцэс болгох",
      "subgoals": [
        {
          "number": "8.7.1",
          "description": "Хөдөлмөр эрхэлж буй 5-17 насны хүүхдийн тоо, эзлэх хувь, хүйсээр, насны бүлгээр",
          "iframe_url": "https://ourworldindata.org/grapher/children-aged-5-17-engaged-in-labor"
        }
      ]
    },
    {
      "number": "8.8",
      "goal": "Хөдөлмөрлөх эрхийг хамгаалах, бүх ажил хөдөлмөр эрхлэгчид, түүний дотор улирлын түр ажилтан, ялангуяа улирлын түр эмэгтэй ажилтан, аюултай хөдөлмөр эрхэлдэг ажилтнуудад аюулгүй, найдвартай ажиллах орчныг бий болгох",
      "subgoals": [
        {
          "number": "8.8.1",
          "description": "Ажлын байр дахь хүнд болон хөнгөн осол гэмтлийн давтамжийн хувь, хүйсээр, цагаачлалын байдлаар",
          "iframe_url": "https://ourworldindata.org/grapher/fatal-occupational-injuries-among-employees"
        },
        {
          "number": "8.8.2",
          "description": "Олон улсын хөдөлмөрийн байгууллагын конвенц, зөвлөмж болон үндэсний хууль тогтоомжид үндэслэн гарах эвлэлдэн нэгдэх эрх чөлөө болон хамтын хэлэлцээртэй холбоотой хөдөлмөрлөх эрхийн хэрэгжилтийн түвшин",
          "iframe_url": "https://ourworldindata.org/grapher/level-of-national-compliance-with-labor-rights"
        }
      ]
    },
    {
      "number": "8.9",
      "goal": "2030 он гэхэд ажлын байр бий болгож, орон нутгийн соёл, бүтээгдэхүүнийг дэмждэг тогтвортой аялал жуулчлалыг хөхүүлэн дэмжих бодлогыг боловсруулж, хэрэгжүүлэх",
      "subgoals": [
        {
          "number": "8.9.1",
          "description": "ДНБ болон түүний өсөлтөд аялал жуулчлалын салбарын нэмэгдэл өртгийн эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/tourism-gdp-proportion-of-total-gdp"
        }
      ]
    },
    {
      "number": "8.10",
      "goal": "Хүн бүрт банк, даатгал, санхүүгийн үйлчилгээний хүртээмжийг хүргэж өргөжүүлэх, түүнийг дэмжих дотоодын санхүүгийн институтийн чадавхыг бэхжүүлэх",
      "subgoals": [
        {
          "number": "8.10.1",
          "description": "(a) 100,000 насанд хүрэгчдэд ногдох арилжааны банкны салбарууд, (b) 100,000 насанд хүрэгчдэд ногдох АТМ-ын тоо",
          "iframe_url": "https://ourworldindata.org/grapher/number-of-commercial-bank-branches-per-100000-adults"
        },
        {
          "number": "8.10.2",
          "description": "Банк болон бусад санхүүгийн байгууллагад данстай эсвэл гар утсаар мөнгөний үйлчилгээ авсан насанд хүрэгчид (15 ба түүнээс дээш насны)-ийн эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/account-at-financial-institution"
        }
      ]
    },
    {
      "number": "8.a",
      "goal": "Нэн буурай хөгжилтэй орнуудад үзүүлэх худалдааны холбогдолтой техникийн туслалцааны сайжруулсан нэгдсэн хүрээ/бүтцээр дамжуулан хөгжиж буй орнууд, ялангуяа нэн буурай хөгжилтэй улс орнуудад үзүүлэх Худалдааны тусламж дэмжлэгийг нэмэгдүүлэх",
      "subgoals": [
        {
          "number": "8.a.1",
          "description": "Худалдааны үүрэг амлалт, зарцуулалтад зориулсан тусламж",
          "iframe_url": "https://ourworldindata.org/grapher/total-oda-for-aid-for-trade-by-recipient"
        }
      ]
    },
    {
      "number": "8.b",
      "goal": "2020 он гэхэд залуучуудын ажил эрхлэлтийн дэлхийн стратегийг боловсруулан хэрэгжүүлж, ОУХБ-ын Ажил хөдөлмөрийн дэлхийн гэрээ хэрэгжүүлэх",
      "subgoals": [
        {
          "number": "8.b.1",
          "description": "Хөдөлмөр эрхлэлтийг дэмжих үндэсний стратегийн хүрээнд эсвэл тусад нь боловсруулан хэрэгжүүлж байгаа залуучуудын хөдөлмөр эрхлэлтийг дэмжих үндэсний стратегитай эсэх"
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

for data in goals_data['goals']:
    create_goal_section(
        number=data["number"],
        goal=data["goal"],
        subgoals=data["subgoals"]
    )

st.divider()

st.markdown("<p style='text-align: center; color: black;'>All plots generated by Our World In Data are under CC-BY License of Fair Use.</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: black;'>2024 © Green Dot Climate</p>", unsafe_allow_html=True)