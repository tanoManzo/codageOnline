from os import write
import streamlit as st
st.title("Bonjour")
st.write("choisir votre tipe de dragon")
option = st.selectbox(
     'How would you like to be contacted?',
     ('feu', 'nature', 'eau','vent','terre','métal','glace'))

st.write('tu as choisi:', option)
if option=='feu':
    st.image("https://th.bing.com/th/id/OIP.1VUsnCB6XEBu1lrcOZ_TYQHaEK?pid=ImgDet&rs=1")
    st.write("D'après la légende, le dragon du feu représenté sur le drapeau gallois date de l'époque du roi Vortigern. Les fondations de la forteresse que le roi faisait construire à Dinas Emryn s'effondrant continuellement, il fit venir à la cour le jeune Merlin qui se nommait alors encore Emrys.")
if option=='nature':
    st.image("https://cdn.shopify.com/s/files/1/1163/0056/products/radix_the_living_root-1024x768_1024x1024.jpg?v=1571667834")
    st.write("Des origines mal définies Il est difficile de déterminer une origine géographique ou historique aux dragons. Leur apparition semble dater des premières civilisations, peut-être même du Paléolithique supérieur.")
if option=='eau':
    st.image("https://th.bing.com/th/id/R.029ed599ac84276d0dcba351400b0b08?rik=O9Sscc3y0bRJqA&riu=http%3a%2f%2fimages.4ever.eu%2fdata%2fdownload%2fdessins%2fcreature-de-leau%2c-un-dragon-deau-174624.jpg&ehk=LpT3aJhfIAMrz8FUMOInlnYHMUMdVVEYeTZkV7Cs1fA%3d&risl=&pid=ImgRaw&r=0")
    st.write("Le Dragon d'eau, ou de son nom complet Physignathus cocincinus est originaire d'Asie du Sud-Est. On le rencontre dans les forêts au climat humide et chaud du Cambodge, dans le sud de la Chine, de Thaïlande ou encore au Vietnam près des points d'eau. C'est un lézard diurne appartenant à la famille des agamidés.")
if option=='vent':
    st.image("https://th.bing.com/th/id/R.89a7c39241f5f279b8dc187f2758ab38?rik=EhfSnct%2bah6wiQ&riu=http%3a%2f%2fi.neoseeker.com%2fmgv%2f420572-mhdude%2f572%2f29%2fmiddle_1226666349_display.jpg&ehk=xSObKweODig%2fOyQjU%2fIZ6J%2fn4alou8gE76Bp167U9BA%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1")
    st.write("Les drapeaux eux-mêmes sont appelés habituellement les chevaux du vent. Ils flottent au vent et emportent les prières au ciel comme le cheval volant dans le vent. Le garuda et le dragon tirent leur origine de la mythologie indienne pour le premier et de la chinoise pour le second.")
if option=='terre':
    st.image("https://th.bing.com/th/id/R.171c8f3b826a0c43a72963eb4664c457?rik=SInDgTRyXJphYw&riu=http%3a%2f%2femeraude1977.e.m.pic.centerblog.net%2fo%2fe2f7466b.png&ehk=ohP7LOVybw%2f1OF8nyB5OUp0Dl7a9kJWpsAUwAmimgRY%3d&risl=&pid=ImgRaw&r=0")
    st.write("Le dragon de terre est le cinquième élément du cycle sexagésimal chinois. Il est appelé wuchen ou wou-tch’en en chinois (chinois traditionnel et simplifié : 戊辰 ; pinyin : wùchén), mujin en coréen, boshin en japonais et mậu thìn en vietnamien. Il est précédé par le lièvre de feu et suivi par le serpent de terre. À la tige céleste wu e…")
if option=='métal':
    st.image("https://th.bing.com/th/id/R.b878d2e5737827feb8e469b885e76d5d?rik=5pWG2wtXmEWX9g&riu=http%3a%2f%2ffc02.deviantart.net%2ffs49%2fi%2f2009%2f165%2f6%2f4%2fmetal_dragon_by_StrainedEye.jpg&ehk=0EGFvJ%2bGvPybwf9VjLId%2fHWKkTUV0YxVLkZPXfaAiyA%3d&risl=&pid=ImgRaw&r=0")
    st.write("Le dragon de métal est le dix-septième élément du cycle sexagésimal chinois. Il est appelé gengchen, ou keng-tch’en en chinois (chinois traditionnel et simplifié : 庚辰 ; pinyin : gēngchén) gyeongin en coréen, koshin en japonais et canh thin en vietnamien. Il est précédé par le lièvre de terre et suivi par le serpent de métal.")

st.write("à la tige céleste geng est associé le yáng et l élément du métal, et à la branche terrestre chen, le yáng, l'élément métal, et le signe du dragon. Dans la symbolique des cinq éléments, le gengchen correspond donc au « bois qui donne naissance au métal. »")
if option=='glace':
    st.image("https://i.pinimg.com/originals/79/c9/b0/79c9b0303b4740dff4947b6bad94ccd3.jpg")
    st.write("Dragon de glace Dragon de glace est un recueil de nouvelles fantastiques de l'écrivain américain George R. R. Martin publié en France en 2011. Ce recueil n'a pas d'équivalent en langue anglaise.")