import streamlit as st
import streamlit.components.v1 as components

def create_goal_section(number, goal, subdescription, iframe_url):
    st.markdown(f"### {number}. {goal}")
    st.markdown(f"_{subdescription}_")
    components.iframe(iframe_url, height=500)

st.title('Зорилт 6. Баталгаат ундны ус ')

st.write('Хүн бүрд ус, ариун цэврийн байгууламжийг хүртээмжтэй хүргэж, тэдгээрийн тогтвортой менежментийг хангах')

#JSON table
goals_data = {
  "goals": [
    {
      "number": "6.1",
      "goal": "2030 он гэхэд хүн бүрийг ундны аюулгүй, боломжийн үнэтэй усаар хангах",
      "subgoals": [
        {
          "number": "6.1.1",
          "description": "Аюулгүй, баталгаат ундны усны үйлчилгээгээр хангагдсан хүн амын эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/proportion-using-safely-managed-drinking-water"
        }
      ]
    },
    {
      "number": "6.2",
      "goal": "2030 он гэхэд хүн бүрийг тэгш хүртээмжтэй, эрүүл ахуйн шаардлага хангасан ариун цэврийн байгууламжид хамруулж, охид, эмэгтэйчүүд, эмзэг бүлгийнхний хэрэгцээ шаардлагыг онцгойлон анхааран үзэж ил задгай биеэ засах явдлыг зогсоох",
      "subgoals": [
        {
          "number": "6.2.1",
          "description": "Эрүүл ахуйн шаардлага хангасан ариун цэврийн үйлчилгээгээр хангагдсан хүн амын эзлэх хувь (гар угаах саван, ус, угаалтуурыг хамруулна )",
          "iframe_url": "https://ourworldindata.org/grapher/share-using-safely-managed-sanitation"
        }
      ]
    },
    {
      "number": "6.3",
      "goal": "2030 он гэхэд дэлхийн түвшинд бохирдлыг бууруулах, хог хаях ажиллагааг халах, аюултай химийн бодис, материалыг гаргах явдлыг хамгийн бага түвшинд хүргэх, цэвэрлэгдээгүй бохир ус хувь хэмжээг хоёр дахин бууруулах, усыг дахин боловсруулж, цэвэршүүлэх явдлыг [x] хувиар нэмэгдүүлэх замаар усны чанарыг сайжруулах",
      "subgoals": [
        {
          "number": "6.3.1",
          "description": "Дахин боловсруулж, сайтар ариутгасан бохир усны эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/wastewater-safely-treated"
        },
        {
          "number": "6.3.2",
          "description": "Хүний ​​эрүүл мэндэд эрсдэлгүй байгалийн чанартай ус хүлээн авагчдын эзлэх хувь"
        }
      ]
    },
    {
      "number": "6.4",
      "goal": "2030 он гэхэд бүх салбарт усны хэрэглээний үр ашгийг үлэмж хэмжээгээр нэмэгдүүлж, усны хомсдолоос гаргах үүднээс цэвэр усны тогтвортой олборлолт, хангамжийг хангаж, усны хомсдолоос өртсөн хүн амын тоог үлэмж хэмжээгээр бууруулах",
      "subgoals": [
        {
          "number": "6.4.1",
          "description": "Ус ашиглалтын үр ашигт гарч буй өөрчлөлт, хугацаагаар",
          "iframe_url": "https://ourworldindata.org/grapher/water-productivity"
        },
        {
          "number": "6.4.2",
          "description": "Усны хомсдол: тогтоогдсон цэвэр усны нөөцөд хэрэглэсэн цэвэр усны эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/freshwater-withdrawals-as-a-share-of-internal-resources"
        }
      ]
    },
    {
      "number": "6.5",
      "goal": "2030 он гэхэд тохиромжтой гэж үзвэл хил дамнасан хамтын ажиллагаагаар дамжуулан бүх түвшинд усны нөөцийн нэгдсэн менежментийг нэвтрүүлэх",
      "subgoals": [
        {
          "number": "6.5.1",
          "description": "Усны нөөцийн нэгдсэн менежмент (УННМ)-ийн хэрэгжилтийн зэрэг (0- 100)",
          "iframe_url": "https://ourworldindata.org/grapher/implementation-of-integrated-water-resource-management"
        },
        {
          "number": "6.5.2",
          "description": "Усны хамтын ажиллагаанд зориулсан зохицуулалттай хил дамнасан усны ай сав газрын эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/water-basins-cooperation-plan?country=~MNG"
        }
      ]
    },
    {
      "number": "6.6",
      "goal": "2020 он гэхэд устай холбоотой экосистем, түүний дотор уул, ой, намагшсан газар, гол мөрөн, уст давхарга, нуурыг хамгаалах, сэргээх",
      "subgoals": [
        {
          "number": "6.6.1",
          "description": "Устай холбоотой экосистемд гарсан өөрчлөлт, хугацаагаар",
          "iframe_url": "https://ourworldindata.org/grapher/share-of-land-covered-by-lakes-and-rivers?tab=chart&country=~MNG"
        }
      ]
    },
    {
      "number": "6.A",
      "goal": "2030 он гэхэд ус, ариун цэврийн байгууламжтай холбоотой үйл ажиллагаа, хөтөлбөр, түүний дотор ус хураах, цэвэршүүлэх, усны үр ашиг, бохир усыг цэвэрлэх, дахин ашиглах технологийн чиглэлээр хөгжиж буй орнуудад үзүүлдэг олон улсын хамтын ажиллагаа, чадавх бэхжүүлэх дэмжлэг туслалцааг өргөжүүлэх",
      "subgoals": [
        {
          "number": "6.A.1",
          "description": "Засгийн газрын зардалд тусгасан ус ариун цэврийн байгууламжид зориулсан хөгжлийн албан ёсны тусламжийн хэмжээ",
          "iframe_url": "https://ourworldindata.org/grapher/total-oda-for-water-supply-and-sanitation-by-recipient"
        }
      ]
    },
    {
      "number": "6.B",
      "goal": "Усны болон ариун цэврийн байгууламжийн менежментийг боловсронгуй болгох чиглэлээр орон нутгийн хамт олны оролцоог дэмжих, бэхжүүлэх",
      "subgoals": [
        {
          "number": "6.B.1",
          "description": "Ус болон ариун цэврийн менежментийн чиглэлээр орон нутгийн иргэдийн оролцоог хангах тогтсон үйл ажиллагааны бодлого, журамтай орон нутгийн засаг захиргааны нэгжийн эзлэх хувь",
          "iframe_url": "https://ourworldindata.org/grapher/share-of-countries-with-procedures-for-community-participation-in-water-sanitation-management?country=~Central+and+Southern+Asia+%28UN%29"
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