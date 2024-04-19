import streamlit as st
import streamlit.components.v1 as components

def create_goal_section(number, goal, subdescription, iframe_url):
    st.markdown(f"### {number}. {goal}")
    st.markdown(f"_{subdescription}_")
    components.iframe(iframe_url, height=500)

st.title('Mongolian SDG Tracker төсөл: Зорилт #10 - ')
st.write('lorem ipsum dolor')

#JSON table
goals_data = {
  "goals": [
    {
      "number": "10.1",
      "goal": "2030 он гэхэд бага орлоготой хүн амын 40 хувийн орлогын өсөлтийг үндэсний дунджаас дээгүүр түвшинд аажмаар хүргэж, хадгалах",
      "subgoals": [
        {
          "number": "10.1.1",
          "description": "Хүн амын нийт хэрэглээнд хамгийн бага хэрэглээтэй 40 хувийн хүн амын орлого, зарлагын эзлэх хувийн жингийн өөрчлөлт (өсөлт)",
          "iframe_url": "https://ourworldindata.org/grapher/annual-growth-income-consumption-poorest-vs-total-population?country=~MNG"
        }
      ]
    },
    {
      "number": "10.2",
      "goal": "2030 он гэхэд нас, хүйс, хөгжлийн бэрхшээл, арьс өнгө, яс үндэс, удам угсаа, шашин шүтлэг, эдийн засгийн болон бусад байр сууриасаа үл хамааран хүн бүрийг нийгэм, эдийн засаг, улс төрийн амьдралд эрх тэгш оролцох боломжоор хангаж, дэмжих",
      "subgoals": [
        {
          "number": "10.2.1",
          "description": "Дундаж орлоготой 50 хувиас доогуур амьжиргаатай хүн амын эзлэх хувь, хүйсээр, насны бүлгээр, хөгжлийн бэрхшээлтэй иргэдээр",
          "iframe_url": "https://ourworldindata.org/grapher/relative-poverty-share-of-people-below-50-of-the-median"
        }
      ]
    },
    {
      "number": "10.3",
      "goal": "Ялгаварлан гадуурхсан хууль журам, бодлого, зан заншлыг халж, энэ талын хууль тогтоомж, бодлого, үйл ажиллагааг хөхүүлэн дэмжих замаар тэгш боломж бололцоог бүрдүүлж, тэгш бус байдлыг бууруулах",
      "subgoals": [
        {
          "number": "10.3.1",
          "description": "Олон улсын хүний эрхийн хуулиар хориглосон ялгаварлан гадуурхах явдлын аль нэг тохиолдлоор сүүлийн 12 сарын дотор гадуурхагдсан, доромжлуулснаа хувьдаа мэдэрсэн гэж мэдүүлсэн хүн амын эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/share-of-the-population-reporting-having-felt-discriminated-against"
        }
      ]
    },
    {
      "number": "10.4",
      "goal": "Санхүү, цалин, нийгэм хамгааллын бодлогыг батлан хэрэгжүүлж, тэгш байдлыг аажмаар хангах",
      "subgoals": [
        {
          "number": "10.4.1",
          "description": "ДНБ-нд цалин, нийгмийн хамгааллын шилжүүлгийн эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/labor-share-of-gdp"
        },
        {
          "number": "10.4.2",
          "description": "Бодлогыг батлан хэрэгжүүлсэний дараах нөлөө",
          "iframe_url": "https://ourworldindata.org/grapher/gini-coefficient-after-vs-before-tax-wb-scatter?country=~MNG"
        }
      ]
    },
    {
      "number": "10.5",
      "goal": "Дэлхийн санхүүгийн зах зээл, институтийг зохицуулах, тэдэнд хяналт шинжилгээ хийх ажлыг сайжруулж, энэ талын дүрэм журмын хэрэгжилтийг хангах",
      "subgoals": [
        {
          "number": "10.5.1",
          "description": "Санхүүгийн тогтвортой байдлын үзүүлэлт"
        }
      ]
    },
    {
      "number": "10.6",
      "goal": "Илүү үр дүнтэй, хариуцлагатай, хууль ёсны институтийг бий болгох үүднээс дэлхийн олон улсын эдийн засаг, санхүүгийн институтийн шийдвэр гаргах үйл ажиллагаанд хөгжиж буй орнуудын төлөөллийг нэмэгдүүлж, байр сууриа илэрхийлэх боломжоор хангах",
      "subgoals": [
        {
          "number": "10.6.1",
          "description": "Олон улсын байгууллагад хөгжиж буй орнуудын гишүүнчлэл, санал өгөх эрхийн эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/proportion-of-members-of-developing-countries-in-international-organizations?country=~MNG"
        }
      ]
    },
    {
      "number": "10.7",
      "goal": "Төлөвлөлт, зохицуулалт сайтай шилжилт хөдөлгөөний бодлого хэрэгжүүлэх замаар хүмүүсийн зохион байгуулалттай, аюулгүй, байнгын, хариуцлагатай шилжилт хөдөлгөөнийг дэмжих",
      "subgoals": [
        {
          "number": "10.7.1",
          "description": "Гадаадад олсон жилийн нийт орлогод тухайн ажилтны ажилд ороход зарцуулсан зардлын эзлэх хувь"
        },
        {
          "number": "10.7.2",
          "description": "Шилжин суурьших сайн бодлогыг хэрэгжүүлдэг эсэх",
          "iframe_url": "https://ourworldindata.org/grapher/facilitate-orderly-safe-migration"
        },
        {
          "number": "10.7.3",
          "description": "Шилжин суурьших явцад нас барсан, сураггүй болсон хүмүүсийн тоо"
        },
        {
          "number": "10.7.4",
          "description": "100,000 оршин суугч хүн амд ногдох дүрвэгсдээр хүлээн зөвшөөрөгдсөн нийт хүмүүсийн тоо",
          "iframe_url": "https://ourworldindata.org/grapher/number-of-refugees-per-100000"
        }
      ]
    },
    {
      "number": "10.A",
      "goal": "Дэлхийн худалдааны байгууллагын хэлэлцээрт нийцүүлэн хөгжиж буй орон, ялангуяа нэн буурай хөгжилтэй улс орнуудад онцгой ба ялгавартай хандах зарчмыг хэрэгжүүлэх",
      "subgoals": [
        {
          "number": "10.A.1",
          "description": "Импортын тэг тарифтай нэн буурай хөгжилтэй болон хөгжиж буй орнуудын импортод ногдуулсан тарифын эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/proportion-tariff-lines-applied-to-imports-from-ldcs"
        }
      ]
    },
    {
      "number": "10.B",
      "goal": "Улс орны үндэсний төлөвлөгөө, хөтөлбөртэй нийцүүлэн хэрэгцээ шаардлага өндөр байгаа улс орнууд, ялангуяа нэн буурай хөгжилтэй орнууд, Африкийн орнууд, жижиг арлын хөгжиж буй орнууд, далайд гарцгүй орнуудад өгөх хөгжлийн албан ёсны тусламж, оруулах санхүүгийн урсгал, түүний дотор гадаадын шууд хөрөнгө оруулалтыг дэмжих",
      "subgoals": [
        {
          "number": "10.B.1",
          "description": "Хөгжилд зориулсан хөрөнгийн нийт урсгал хүлээн авагч болон хандивлагч орнуудаар, урсгалын төрлөөр (хөгжлийн албан ёсны тусламж, гадаадын шууд хөрөнгө оруулалт болон бусад орлого)",
          "iframe_url": "https://ourworldindata.org/grapher/total-assistance-for-development-by-recipient"
        }
      ]
    },
    {
      "number": "10.C",
      "goal": "2030 он гэхэд шилжин суурьшигчдын хийдэг мөнгөн гуйвуулгын гүйлгээний төлбөрийг 3 хувиас бага түвшинд хүртэл бууруулж, 5 хувиас дээш төлбөртэй мөнгө гуйвуулах үйлчилгээг зогсоох",
      "subgoals": [
        {
          "number": "10.C.1",
          "description": "Мөнгөн гуйвуулгын дүнд эзлэх гуйвуулгын зардал"
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
            st.markdown("⚠️ Not available ⚠️")

for data in goals_data["goals"]:
    create_goal_section(
        number=data["number"],
        goal=data["goal"],
        subgoals=data["subgoals"]
    )