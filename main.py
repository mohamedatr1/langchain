from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
load_dotenv()  # take environment variables from .env.


def main():
    information = """
    Sheikh Mohamed Bachir El Ibrahimi or Bachir El Ibrahimi, born on June 13, 1889 has Ouled Brahem (Algeria) and died on May 20, 1965 has Setif (Algeria), is a muslim scholar, journalist, writer, historian, linguist and poet algerian, traveling companion and successor ofAbdelhamid Ben Badis at the head of theassociation of Algerian Muslim Ulemas.

He is the father of the Algerian doctor and politician Ahmed Taleb Ibrahimi.

Biography

Mohamed Bachir El Ibrahimi at the end of his life
Mohamed Bachir El Ibrahimi was born on June 13, 1889 (14 chawwal 1306 AH) has Ouled Brahem in the douar of the Awlād Ibrāhīm of the tribe arabic righa Dhahra (tribe of Ras-El-Oued and its surroundings) in a family descended from the prophet Mohammed[1],[2],[3] where he begins his religious learning by memorizing the Quran at the age of 8 and studying a few texts (moutoun) case law (fiqh) malikite with his father and uncle.

Cairo and Medina (1911-1916)
In 1911 (1330 AH), he leaves to join his family at Medina via Cairo (where he stayed for 3 months during which he met Egyptian poets Ahmed Chawqi and Hafez Ibrahim). In the second holy city of Islam, he studies the Muwatta of theimam Malik and case law (fiqh) malikite under the patronage of sheikh Abdelaziz al-Tounissi and the Sahih Muslim under that of Hussain Ahmed Madani, tutelary figure of deobandism and Indian nationalist activist. It also receives influence from students of religious science (toulab al-ilm) came from Chinguetti. Finally, he begins to memorize several collection of poems thus giving him a certain eloquence, useful for the rest of his career[4].

Damascus (1916-1920)
In 1916, political unrest in Hejaz (arab revolt, siege of Medina) push him to leave the region to settle in Damascus, where he continued his religious learning at the umayyad Mosque alongside scholars (ulema) Mohammed Al-Khidr Hussein (ar), Djamal ad-Dine al-Qassimi (in) and Badreddine al-Hassani (ar)[4].

In 1919, he participated in the founding of theArab Academy of Damascus with Muhammad Kurd Ali[4].

Return to Algeria (1920-1924)
After his return to Algeria in 1920 (1338 AH), he works to disseminate the reform (al-islah) and religious education in the city of Setif, where he holds a mosque which is not affiliated with the French colonial authorities[4].

The reform movement and the association of Algerian Muslim ulama
When in 1924, his friend Abdelhamid Ben Badis met at Medina comes to submit the idea of creating the Algerian reform movement (al-harakat al-islah al-djaza'iriyyah), he accepts enthusiastically. The first mission entrusted to him by the movement was to go and preach in eastern Algeria, which he achieved with some success by opening several Koranic schools (madaris) free and by chaining sermons (khoutab) captivating[4].

His activities, within the reform movement then from 1931 of theassociation of Muslim Ulemashe attracted the hostility of certain notables and Sufis who demanded that the colonial authorities take measures against him. It's done in 1939, when they decide to exile him to Aflou after publishing an article anti-colonialist signed with his pen in the newspaper El-islah. After the death of Ben Badis in 1940, he was elected head of the association of Muslim ulama while he was still in a situation of house arrest. This ended on December 28, 1942 following the allied landing in North Africa but El Ibrahimi was arrested again after the events of May 1945. Released a year later, he resumed his public activities and wrote harsh articles against French colonialism and its "agents" in the columns of the newspaper El-bassir, reopened in 1947[4].

After independence 1962
After the independence of Algeria in 1962, he assumes the responsibilities ofimam and of khatib in the ketchaoua Mosque but, opposed to the self-managing socialist regime of Ben Bella, he experiences house arrest again and dies in this situation on May 20, 1965, less than a month before coup d'état overthrowing Ben Bella.


Tomb of El Ibrahimi
Tribute

There Mohamed Bachir El Ibrahimi Mosque has Bou Saada.
The mosque of Bou Saada is baptized Mohamed Bachir El Ibrahimi Mosque
THEBordj Bou Arreridj University bears his name
The École Normale Supérieure of Kouba bears his name
    """
    summary_template = """
    given the information {information}, about a person i want you to create:
    1. A short summary 
    2. two interesting facts about them
    3. A list of their achievements
    4. A list of their personal life
    5. A list of their professional life
"""
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatGroq(temperature=0, model_name="llama-3.1-8b-instant",)
    #llm = ChatOllama(model="qwen2.5-coder:3b", temperature=0)
    #LangChain Expression Language (LCEL)
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information":information})
    print(response.content)
if __name__ == "__main__":
    main()
