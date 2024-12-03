# Surfacing community conversations: Ethical federated data exchange for streamlined signal detection in an ecosystem of research communities


## 1. Professional background

*Your professional background (If applicable, we would like to know about previous entrepreneurial experience, relevant organizations you may have started, and/or milestones you have achieved so far).*

I am a Senior Research Community Manager with a PhD in Informatics and expertise in both qualitative and quantitative research methods, including programming. In 2020, I founded [Open Research Calendar](https://openresearchcalendar.org), a community-driven calendar of open research events that broadcasts submissions via LinkedIn, Twitter, and email round-ups. This tool has shared over 1,400 events and gathered more than 250 email subscribers, thereby improving coordination, reach and accessibility of opportunities in this space. Our growth has been entirely organic, and with [support from the UK Reproducibility Network](https://www.ukrn.org/2020/09/18/ukrn-open-research-calendar-cobadge/), to expand our broadcasting capacity. Additionally, as a postdoctoral researcher at the University of Oxford (2018-2023), I developed infrastructure, strategy, and training to lower the barriers to open science in brain imaging, founding [Open WIN](http://win.ox.ac.uk/open) and facilitating annual cohorts of open science ambassadors.

At the Alan Turing Institute (2023-present), I develop strategies to empower AI and data science communities, focusing on decentralizing power and promoting reproducibility best practices. My work involves qualitative stakeholder analysis to shape engagement objectives and success metrics, alongside creating computational tools—such as databases, software, and visualizations—that enhance community management, track community health, and improve stakeholder visibility (see [Turing Environment and Sustainability Stakeholder Map](https://cassgvp.kumu.io/alan-turing-institute-environment-and-sustainability)). 

My professional practice is shaped by my personal values which prioritise transparency, access to information, and equitable engagement, in alignment with my contributions to [The Turing Way](https://book.the-turing-way.org/index.html) handbook on reproducible, ethical and collaborative data science. I have an extensive background in equality, diversity and inclusivity (EDI) work, as past chair of the [CSCCE EDI special interest group](https://www.cscce.org/community/sigs/) and current Co-Chair of the [Turing Gender Equality Network Group](https://www.turing.ac.uk/about-us/equality-diversity-and-inclusion/EDI-framework). 


## 2. The problem

*A problem in communication among scientists*

Scientists increasingly use community-based communication to share information and learn from each other. This communication happens over an increasing number of channels (Yammer, Slack, Viva Engage, Teams, Email, Blogs, X, BlueSky, Mastodon, LinkedIn…) and is often siloed in communities. This leads to information overload for individuals watching across multiple channels and communities, and as pathways for sharing *between* communities relies on motivated interconnected individuals, a high risk that critical sentiment is not more broadly accessible at an ecosystem level in real time. Without an ecosystem perspective of community conversations, we have a biased perception of the priorities and interests of the scientific community, limited by our individual connectivity. 

We could introduce significant efficiencies in how we identify community-specific and sector-wide trends and challenges in real time through the introduction of a **federated ecosystem of community signalling tools**, that is, a way to identify critical conversation areas within communities, and surface them at an ecosystem level. Such a system would benefit individual scientists by reducing the time spent on information gathering, improving cross-disciplinary insights, and connecting them more effectively with individual communities where they can participate in relevant conversations. For communities, this ecosystem level surfacing would improve their visibility and engagement, and provide ecosystem-wide perspectives on which to develop strategy. At a sector level, an ecosystem perspective would enable more informed decision making and resource allocation, support long-term strategic planning, facilitate collective problem solving and improve equity in contributions. Achieving the aims of this proposal would scaffold a more interconnected and efficient ecosystem of research communities, where cross-disciplinary collaboration thrives, critical signals are detected and acted upon faster, and communities of all sizes can benefit from shared knowledge and data. 

A central component of this proposal is the movement of community data out of individual silos and into a shared space. There are significant ethical risks associated with such a proposal, particularly with regard to data privacy and the potential to compound existing biases in the research ecosystem. In order to bring us closer to an ethical and justice oriented research ecosystem, and to ensure the success of this proposal, we would allocate significant resourcing to appropriately defining and addressing the ethical implications of this tool as part of the ongoing technical development work. 


## 3. The solution

*Your proposed solution to this problem (We expect that your ideas are a starting point for future iterations. Please let us know explicitly if you are flexible and willing to collaboratively shape your idea prior to starting a potential fellowship at Astera)*


### Aim

This proposal aims to develop mechanisms to surface and share important signals (“conversations”) between communities. Signals could represent high interest conversations, resources, priority concerns, or specific areas of interest defined by the communities who participate in the ecosystem, for example signals relating to the adoption of open science practices. Identified signals would be volunteered to an ecosystem level, and shared publicly via interactive graphs to facilitate exploration of themes and communities.


### AI Community Relationship Manager (CoRM)

Signals would be detected within communities via a specialised open source AI Community Relationship Manager (CoRM), developed as a core component of this project. The CoRM would leverage large language models, deep neural networks and machine learning to gather and analyse text-based signals using “community intelligence” methodologies applied in industry. These tools function well over community data sources relevant to commercial interests (e.g. slack, discourse, linkedIn, GitHub), but require expansion to capture signals from sources relevant to research communities, such as Zenodo, ORCID and DataCite. 

To function at the community level, the CoRM will require access to the community’s communications tools, and will therefore have access to data which would be highly valuable in the performance of stakeholder management, strategic planning and community health analysis. In order to maximise the uptake of the CoRM into communities, we will work to maximise the return from this data access and integrate features which are valuable for community managers, with a low adoption barrier and high degree of user-led design following a product-led-growth strategy, for example through community ambassadors, to maximise reach and scalability across diverse research communities.


### Federation to decentralise power

Individual communities would volunteer data to the ecosystem level via a federated data management system. By this model, the raw data used to identify signals would not move higher than the community level, with only a summarised signal ‘output’ shared to the ecosystem. The federated communities would therefore retain full data rights and the power to review signals before they are shared to the ecosystem. As analysis will be conducted on the community (‘client’) side, all code will be visible to the communities themselves, with an emphasis on transparency and explainability of the analysis. Individuals within communities would also be given the opportunity to consent via ORCID to link their activity to identified signals, so they can gain acknowledgement for their participation and contributions. As at the community level, individuals will be able to review where their participation has been identified and asked for explicit opt-in consent for their participation to be individually acknowledged at the ecosystem level. 


### Ethical considerations

There are significant ethical issues which require careful consideration in this proposal in regards to:

1. Community intelligence analysis; 
2. Data exchange or "Data-as-a-Service" tool models; 
3. Infrastructure requirements for federated analysis. 

The effective and transparent handling of these issues, along with co-creation of appropriate mitigation policies and procedures with the community, will be essential to achieving the vision of equitable participation in ecosystem level dialogue. We expect the ethical understanding and mitigation activity to evolve in research and practice, as an embedded feature of the work. 


#### Community intelligence

Community intelligence tools are deployed in industry to understand the buying signals of potential customers based on how they interact with the brand and competitors in community spaces. This intelligence can then be used to position the product to the customer, with a predicted conversation rate. Undertaking this analysis requires that customer behaviour is monitored across different platforms, for example using browser cookies or direct analytics on brand-managed forums. This raises issues around consent and the potential for data collection without explicit awareness. There is also a potential for harm if community members feel as though they are being monitored or surveilled, leading to a “chilling effect” where individuals alter their behaviour or withdraw from the community as a result of perceived monitoring. This can lead to less honesty in interactions, fewer collaborative efforts, and the potential loss of valuable insights. More importantly, however, the perceived impact of surveillance could be damaging to the community and the trust they have worked hard to develop, undermining its integrity and ability to operate. Harm can also be done to individuals and communities if there is perceived or real misuse of the insights gained via community intelligence, such as them being used for commercial gain, to target and position misinformation, manipulate community or individual behaviour without knowledge, or target and stigmatise individuals or vulnerable groups. The potential for misuse means significant attention must be afforded to security of data compiled for community intelligence analysis, to minimise vulnerability to breaches or theft. There must also be high levels of accountability and transparency around the algorithms which are deployed to compile intelligence, to ensure they are appropriate for the identified purpose and there is sufficient recourse for challenging on the grounds of data misuse. 


#### Data exchange models

Data exchange models are a common arrangement in the digital economy, where users provide their data in exchange for the provision of a service. They are a feature of “freemium” technology, where there is no user charge for accessing a website or app (e.g. Facebook or Google) or discounts are offered (e.g. supermarket loyalty schemes). The data collected based on the users’ interaction with that service is used to understand behaviour and/or sold to third parties to improve marketing. The main ethical concerns with such models relate to:



* Lack of informed consent from individual data providers regarding how their data will be processed;
* Risks of re-identification or privacy violations;
* Potential for bias, discrimination or inequitable access in the use of “freemimum” services;
* Monetization of data in ways that conflict with its intended use.
* Misalignment of perceived value of the data between the company and individual, with the corporate benefit not clearly communicated to the data providers.


#### Federation infrastructure

As described above, federation of data and analysis can return significant power to data providers by removing the necessity for raw data transfer out of the originating group. This reduces risks associated with data breach and individual privacy. However, the infrastructure requirements for federated analysis (described below) can themselves impose biases in who is able to participate in the federated data exchange. Without consideration of this requirement, we risk surfacing only the interests of communities with sufficient resources to conduct federated analysis, which will further compound inequalities of participation in research. Some communities will already have the infrastructure for data exchange in place and may be able to piggy-back this activity onto their existing services with a low initial and long term cost.  This should not, however, be assumed to be the case for all communities, and costs should be minimised to enable equitable participation. 


##### Data Storage

Local or cloud-based data storage will be required to handle data to be processed by the signal detection tools. Communities will need to ensure sufficient storage capacity, scalability, and quick access to data for real-time processing.


##### Security Infrastructure

Strong security protocols will be essential to safeguard local sensitive community data. This includes data encryption, secure access controls, identity management, and protection against unauthorised access or cyber threats.


##### Data Analysis 

Each community will need sufficient computational power to run the signal detection algorithms, including processing capacity, memory, and storage for large datasets. This could involve local servers or cloud-based solutions depending on data and algorithms developed. More complex analyses may require high-performance computing (HPC) resources or distributed computing frameworks.


##### Software and Tools

Communities will require access to the signal detection algorithms which will be embedded in the CoRM. These tools and the CoRM should be integrated into the community’s existing workflows to maximise efficiency of use, and may require software licences or access to specific libraries. 


##### Network Infrastructure

Adequate network bandwidth will be necessary to support the transfer of signals and other data between the community and ecosystem layers. This may involve high-speed internet or private networks to minimize latency and improve the security of data transfers.


### Mitigation plan

We propose to capture, analyse and report on our ethical work using AI assurance techniques and standards, as [recommended for the practical implementation of the ethical principles](https://www.techuk.org/resource/techuk-paper-ethics-in-action-from-white-paper-to-workplace.html) that underpin the pro-innovation approach to AI regulation, as described in the [UK Government AI White Paper](https://www.gov.uk/government/publications/ai-regulation-a-pro-innovation-approach/white-paper). This process would produce structured arguments relating to our ethical goals, alongside evidence to support the claim that mitigation activity is proportionate to the scale of risk. Below we summarise the proposed mitigation activity for the ethical themes discussed above, with the expectation that these will be refined through our engagement and ethical analysis. 


#### Transparency and Accountability

It is essential that the intended purpose of the algorithms used to surface community conversations are transparent and co-designed with the community to support their needs and can be reviewed for accuracy in meeting this goal. We intend for the codebase underlying the CoRM to be open source and supported by training and model evaluation data to evaluate accuracy of results. We will also provide accessible documentation describing features of the algorithms, such that they can be reviewed by contributors without software engineering experience. This level of transparency will ensure that we can be held accountable for the analysis performed, and individual communities can trust the outcomes. 

We will be transparent about any downstream use of the data volunteered into the ecosystem, and ensure this use is aligned with the primary goals of the service to surface the interests, needs and perspectives of individual communities to an ecosystem level. We will co-design parameters for data re-use with the community, including acceptable licensing terms. We will explore other requirements for data access which the community may require inorder to have sufficient trust in our tool, for example exclusive reuse within a Trusted Research Environment or community review of data access requests. We intend to maximise the reproducibility of any downstream analysis conducted by ourselves and set a high barrier for computational reproducibility testing. 

A central principle of the tool will be to return significant value through participation in the ecosystem, to both communities and individuals. Transparent documentation of activities to uncover and build value will ensure that there is a clear and proportionate benefit to data contributors at the individual and community level.


#### Risk of Misuse and Bias

We will embed the ethical use of this tool and associated data as a core feature of development by empowering an ethical operations working group to advise on the design and implementation of appropriate safeguards. The working group may employ an “ethical red teaming” approach, where a diverse community explores thought and code-based experiments how misuse could occur, to then design and test mitigations. We would actively foster continuous updates and bidirectional feedback between individuals, communities and ecosystem level to refine mitigation strategies to minimise the risk of misuse.

Acknowledging the infrastructure requirements for federated analysis, we anticipate there will be a bias in uptake of our tool by higher resource communities, leading to a biased view of the conversation in the ecosystem. To minimise this bais, we will intentionally develop light-weight tools which require minimal resourcing and will have the additional benefit of being low carbon. We will also explore the benefit of shared or subsidised infrastructure, including for the provision of security protocols for safe data transfer from low-resource communities. We will additionally take responsibility for processing signals from publically available data sources such as DataCite and LinkedIn, thereby removing the burden of this large amount of data processing from communities. We will pass the processed signals into the ecosystem and also to the community level, so individual communities can monitor for relevant signals to build their own engagement pipelines. 

We are aware that a significant proportion of large language AI models are trained on English language data, and accordingly our analysis models will be best fit for communities where the conversation is happening in English, so there will be a bias towards surfacing conversations which are happening in English. We will actively support and contribute to efforts to debias natural language processing through partnerships with diverse communities, and seek to maximise the use of available non-English algorithms. We will also investigate translation of community signals, so they can be shared at the ecosystem level in languages other than English. 


#### Privacy and Consent

We will work with communities to ensure that notices about data collection were sufficiently prominent and linked to clear and effective explanations about the purpose, value and methods of data processing employed, with low-friction routes to participate in decisions around data practices. We will trial such notices with close partners and monitor for chilling, with awareness that this specific effect could be highly detrimental to the communities we aim to serve. 

We will manage explicit opt-in consent for the transfer of identifiable engagement activity via ORCID authorisation, and provide a direct link for individuals to verify the engagement data they wish to share publicly, for example confirming posts they have interacted with. Risk of re-identification from anonymised data would be mitigated by federated analysis. 


#### Security

We will incorporate appropriate safety protocols to protect data analysed at the ecosystem and levels from breach, unauthorized access, or theft. We will make recommendations for appropriate security at the community level, and support the deployment of appropriate infrastructure where it does not already exist. 


## 4. Existing solution landscape

*The landscape of competitive products and services, and how your solution differs*

This proposal describes the development of existing community intelligence tools to facilitate the ethical surfacing of research community conversations into an ecosystem-level representation. To the best of our knowledge, there are no tools which attempt to deliver a similar wholistic activity. Comparison can instead be made against the component parts of: 1) the CoRM; 2) ecosystem level mapping of research conversations and contributors.


### Community Intelligence tools and CRMs

There are closed- and open source tools available to acquire community intelligence such as [Common Room](https://www.commonroom.io) (closed source) and [Savannah](https://www.savannahhq.com) (open source). These tools are primarily designed for sales teams and do not offer integrations with the varied data sources relevant to signals relevant to research activity, for example through ORCID integration. We have explored feasibility of developing these tools to fit the needs of research communities and we are confident in extensibility to meet our need. These tools are delivered to provide information about a limited community and as such they do not support federated analysis. The findings of these tools are not readily shared by industry to produce an acccesisble ecosystem perspective, and they are not widely adopted by research community managers as [CRMs in general are not well adopted](https://www.cscce.org/2022/04/22/aprils-community-call-recap-exploring-crms-for-community-management/). 


### Ecosystem mapping

Our primary understanding of research activity at an ecosystem level is delivered by tools to support the “[rapidly emerging field of Research Analytics](https://analyticssummit.uky.edu/#/?lang=en)”. Such tools are designed to facilitate data-informed decision-making in the development of research strategy, and draw primarily on traditional research outputs and indexers. For example, Clarivate (Web of Science) use their metrics to identify [emerging trends in research](https://discover.clarivate.com/Research_Fronts_2023_EN) based journal on publication activity. Other actors in this space include Scopus, CrossRef and the freely available [OpenAlex](https://openalex.org/). There is also an increasing number of tools to generate collaboration graphs based on co-authorship, for example [VOSViewer](https://www.vosviewer.com/) and [CollabNext](https://hbcumsi.research.gatech.edu/collabnext-tool). A limitation of these tools, however, is that they rely primarily on journal outputs, with supporting data from grant awards, conference proceedings, books, patents, and dissertations. Such a focus means there is a time delay between the actual performance of research and the indexing, which reduces the possibility to contribute to or shaping ongoing discussions. There are also issues of bias in output indexing, for example [Carivate’s recent decision to no longer index publications in eLife and other journals](https://retractionwatch.com/2024/10/24/elife-latest-in-string-of-major-journals-put-on-hold-from-web-of-science/), and a known bias in what research is [published](https://pmc.ncbi.nlm.nih.gov/articles/PMC6573059/#:~:text=Publication%20bias%20is%20defined%20as,strength%20of%20the%20study%20findings.) and [cited](https://journals.sagepub.com/doi/10.1177/01410768221075881?icid=int.sj-abstract.citing-articles.1) and [funded](https://www.science.org/doi/10.1126/sciadv.aaw7238).

Other mapping activities have been domain focused, for example mapping related to the Open Science landscape. These have primarily used static data, provided limited interactivity in results, and have been limited in scope. Previous open science mapping activities:

* [The Research Software Alliance list of research software communities](https://urssi.us/blog/2020/03/11/the-research-software-alliance-resa-and-the-community-landscape/?ref=investinopen.org) (2019). 
* [Access2Perspectives map of open science resources](https://access2perspectives.pubpub.org/pub/uwl451tj/release/3) (2022). 
* [Open Future map of open science organisation Twitter followers](https://openfuture.pubpub.org/pub/fields-of-open#mapping-the-movement-with-twitter-data) (2023) 
* [UNESCO open science capacity building index](https://www.unesco.org/en/open-science/grid) (2023). 
* [NumFOCUS Map of Open Source research software projects ](https://www.opensource.science/?ref=investinopen.org)(proof of concept 2024). 
* [Invest in open mapping of the research software ecosystem](https://investinopen.org/blog/nnouncing-150-000-award-to-ioi-to-advance-understanding-of-the-research-software-ecosystem/) (grant awarded September 2024). 

As these trends show, there is a movement towards larger and more interactive ecosystem mapping projects, but none have focused on understanding the conversations happening within communities as the primary indicator of emerging priorities.


## 5. Professional skills and gaps

*Your skills, gaps in your skills that you have identified, and how these gaps might be complemented by team members or future team members. We value your honest self-assessment.*

Successful delivery of this project will require expertise in: 1) research community management (RCM); 2) research software engineering in the deployment of AI analysis of natural language for signal detection (Large Language Models) and understanding complex patterns in data (Deep Neural Networks) and federated data analysis; 3) ethical deployment of AI tools. 

I am highly skilled in RCM and well connected into RCM communities via the Centre for Scientific Collaboration and Community Engagement ([CSCCE](https://www.cscce.org)) as past [Co-Chair of the Special Interest Groups for EDI and Open Science](https://www.cscce.org/community/sigs/). This experience and connections make me well positioned to grow our community of users and contributors, and lead the design of the CoRM as a tool to facilitate RCM activities. To achieve the desired level of deployment and engagement, I would grow capacity in RCM, Product Management and Project Management through additional future team members. 

I have a good working knowledge of the principles of AI and federated data analysis through my experience as a neuroscientist and through managing communities employing AI methods at The Alan Turing Institute, the UK’s National Institute for AI and Data Science. The technical complexity of the proposed analysis would require production level expertise and resourcing, for which I would draw on consultant research software engineers following a Request for Tender and community connections, for example via the [Software Sustainability Institute](http://software.ac.uk/). 

I am well versed in ethical issues relating to EDI and data privacy (see for example this [framework I built for sharing brain imaging research data](https://open.win.ox.ac.uk/pages/open-science/community/Open-WIN-Community/docs/data/)), and well connected to practitioners interested in ethical AI deployment in both research (via [The Turing Way](https://book.the-turing-way.org/index.html)) and industry (via and [The Turing Way Practitioners Hub](https://www.turing.ac.uk/turing-way-practitioners-hub), see for example this recent meeting I facilitated on [Open Source, Ethics, & Innovation in AI](https://www.linkedin.com/posts/ariellebennett_had-such-a-fantastic-time-at-open-source-activity-7267531318568144896-JeeS?utm_source=share&utm_medium=member_desktop)). I am also well versed in tools which can be used to appropriately document ethical analysis such as the [Trustworthy and Ethical Assurance platform](https://alan-turing-institute.github.io/AssurancePlatform/), and closely connected to their developers. I would use this understanding and connections to ensure that the resourcing devoted to addressing ethical constraints was appropriately matched to meet the complexity of the issues. In future expansions of the team, I would engage a lead with specific responsibility for delivery and integration of ethics-related work packages. 


## 6. Open sourcing

*Openness of code, data, and other resources is strongly preferred. If you believe that keeping some resources proprietary is necessary for the success of your project, please explain what you intend to keep proprietary, how doing so would increase your project's value for the public good, and whether making it open instead necessarily precludes that impact.*

This project would be open by design, to maximise transparency, equitable engagement, robust delivery, and ultimately trust in the tool, vision and mission of this work. Code would be shared on the maximally permissive licence acceptable to the community of developers (preference for MIT for ease of reuse), and documentation/training would be released CC-BY-4.0 to ensure appropriate acknowledgement of contributions. Appropriate licensing and restrictions around the reuse of data volunteered to the ecosystem level would be discussed with the community, to minimise concerns relating to misuse. 


## 7. Quarterly milestones

*Quarterly milestones you would like to achieve in a 1-year fellowship*

Q1. Set up
* Software development consultants engaged
* Key AI ethics and community management practitioner stakeholders engaged
* Prototype testing communities engaged (n = 2-3)
* First draft of prototype tool requirements
* Community documentation, roadmap and contribution routes published.

Q2. Prototype deployed
* Prototype deployed in testing communities
* Governance drafted
* UX and design testing
* Contributor engagement routes in use

Q3. Community Hackathon
* Priority aims and outputs agreed
* CoRM onboarding materials prepared and tested

Q4. Sustainability
* Growth and engagement strategy formalised
* Governance finalised
* Analysis of Y1 ecosystem data published
* Funding for Y2-4 secured


## 8. Budget

*Budget (include major expense categories (compute costs, equipment, travel, etc)and personnel costs broken down by individual employees/contractors)*


<table>
  <tr>
   <td><strong>Item</strong>
   </td>
   <td><strong>Budget USD</strong>
   </td>
  </tr>
  <tr>
   <td><em>Travel, subsistence & event registrations</em>
   </td>
   <td>$25,500.00
   </td>
  </tr>
  <tr>
   <td><em>Computer equipment, hosting, ORCID consortium membership</em>
   </td>
   <td>$14,500.00
   </td>
  </tr>
  <tr>
   <td><em>Consultancy</em>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>    Software engineering, UX and branding
   </td>
   <td>$170,000.00
   </td>
  </tr>
  <tr>
   <td>    Legal and accounting services for incorporation as non-profit in UK
   </td>
   <td>$26,000.00
   </td>
  </tr>
  <tr>
   <td>    Event management (20% of event cost)
   </td>
   <td>$19,000.00
   </td>
  </tr>
  <tr>
   <td><em>Residential community ethics hackathon (n=30)</em>
   </td>
   <td>$95,000.00
   </td>
  </tr>
  <tr>
   <td><strong>Total</strong>
   </td>
   <td><strong>$350,000.00</strong>
   </td>
  </tr>
</table>


[Full details on linked sheet (not to be shared with application)](https://docs.google.com/spreadsheets/d/16RtDarkOvDMUg2f4PZg9x76Z-WXe8Epk9twVAIe-yRI/edit?usp=sharing)


## 9. Attendance mode

*Whether you prefer to be on-site, remote, or hybrid.*

Remote attendance plus four on-site weeks in Berkley. 
