import streamlit as st
import streamlit.components.v1 as components

def create_goal_section(number, goal, subdescription, iframe_url):
    st.markdown(f"### {number}. {goal}")
    st.markdown(f"_{subdescription}_")
    components.iframe(iframe_url, height=500)

st.title('Mongolian SDG Tracker төсөл: Зорилт #7 - ')
st.write('lorem ipsum dolor')

#JSON table
goals_data = {
  "goals": [
    {
      "number": "7.1",
      "goal": "2030 он гэхэд боломжийн, найдвартай, орчин үеийн эрчим хүчний үйлчилгээгээр хүн бүрийг хангах",
      "subgoals": [
        {
          "number": "7.1.1",
          "description": "Цахилгаан эрчим хүчээр хангагдсан хүн амын эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/share-of-the-population-with-access-to-electricity"
        },
        {
          "number": "7.1.2",
          "description": "Цэвэр түлш, технологийг голчлон хэрэглэдэг хүн амын эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/access-to-clean-fuels-and-technologies-for-cooking"
        }
      ]
    },
    {
      "number": "7.2",
      "goal": "2030 он гэхэд дэлхийн эрчим хүчний хэрэглээнд сэргээгдэх эрчим хүчний эзлэх хувийг үлэмж хэмжээгээр нэмэгдүүлэх",
      "subgoals": [
        {
          "number": "7.2.1",
          "description": "Нийт эрчим хүчний эцсийн хэрэглээнд сэргээгдэх эрчим хүчний эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/share-of-final-energy-consumption-from-renewable-sources"
        }
      ]
    },
    {
      "number": "7.3",
      "goal": "2030 он гэхэд эрчим хүчний үр ашиг, хэмнэлтийн хурдыг дэлхийн түвшинд хоёр дахин нэмэгдүүлэх",
      "subgoals": [
        {
          "number": "7.3.1",
          "description": "ДНБ, анхдагч эрчим хүчээр хэмжсэн эрчим хүчний үр ашиг",
          "iframe_url": "https://ourworldindata.org/grapher/energy-intensity-of-economies"
        }
      ]
    },
    {
      "number": "7.A",
      "goal": "2030 он гэхэд цэвэр эрчим хүчний судалгаа шинжилгээ, технологи, түүний дотор сэргээгдэх эрчим хүч, эрчим хүчний үр ашиг, дэвшилтэт болон цэвэр хатуу түлшний технологийг хүртээмжтэй болгох үүднээс олон улсын хамтын ажиллагааг сайжруулж, эрчим хүчний дэд бүтэц, цэвэр эрчим хүчний технологид оруулах хөрөнгө оруулалтыг хөхүүлэн дэмжих",
      "subgoals": [
        {
          "number": "7.A.1",
          "description": "Цэвэр эрчим хүчний судалгаа, хөгжил, сэргээгдэх эрчим хүчний үйлдвэрлэл, түүний дотор хосолмол системийг дэмжих чиглэлээр хөгжиж буй орнуудад үзүүлж буй олон улсын санхүүгийн тусламж",
          "iframe_url": "https://ourworldindata.org/grapher/international-finance-clean-energy"
        }
      ]
    },
    {
      "number": "7.B",
      "goal": "2030 он гэхэд хөгжиж буй орнууд, ялангуяа нэн буурай хөгжилтэй болон жижиг арлын хөгжиж буй орнуудын иргэдийг орчин үеийн, тогтвортой эрчим хүчний үйлчилгээгээр хангах дэд бүтцийг өргөжүүлж, технологийг шинэчлэх",
      "subgoals": [
        {
          "number": "7.B.1",
          "description": "ДНБ-нд эзлэх эрчим хүчний үр ашигтай байдлыг нэмэгдүүлэх чиглэсэн хөрөнгө оруулалт болон тогтвортой хөгжлийг дэмжсэн дэд бүтэц, технологид зориулсан санхүүжилтыг хийхэд зарцуулсан гадаадын шууд хөрөнгө оруулалтын хэмжээ",
          "iframe_url": "https://ourworldindata.org/grapher/renewable-electricity-generating-capacity-per-capita"
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

for data in goals_data['goals']:
    create_goal_section(
        number=data["number"],
        goal=data["goal"],
        subgoals=data["subgoals"]
    )