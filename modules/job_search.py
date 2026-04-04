def search_jobs(keywords, location="", num_results=10):
    jobs = get_mock_jobs()
    seen = set()
    unique_jobs = []
    for job in jobs:
        key = job["title"] + job["company"]
        if key not in seen:
            seen.add(key)
            unique_jobs.append(job)
    return unique_jobs


def get_mock_jobs():
    return [
        {
            "title": "QA Engineer",
            "company": "Revolut",
            "location": "Tbilisi, Georgia",
            "description": "We are looking for a QA Engineer to join our rapidly growing team. You will be responsible for designing and executing test plans, identifying bugs, and ensuring product quality across web and mobile platforms.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "2 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "Senior QA Engineer",
            "company": "TBC Bank",
            "location": "Tbilisi, Georgia",
            "description": "TBC Bank is seeking a Senior QA Engineer with strong experience in test automation. You will lead QA efforts for our digital banking products and work closely with development teams.",
            "via": "hr.ge",
            "link": "https://hr.ge",
            "posted": "1 day ago",
            "source": "hr.ge"
        },
        {
            "title": "Automation QA Engineer",
            "company": "Bank of Georgia",
            "location": "Tbilisi, Georgia",
            "description": "Join our engineering team as an Automation QA Engineer. You will build and maintain automated test suites using Selenium and Python, and integrate them into our CI/CD pipelines.",
            "via": "jobs.ge",
            "link": "https://jobs.ge",
            "posted": "3 days ago",
            "source": "jobs.ge"
        },
        {
            "title": "QA Lead",
            "company": "Betsson Group",
            "location": "Remote",
            "description": "Betsson Group is hiring a QA Lead to oversee quality assurance across multiple product teams. You will define QA strategy, mentor junior engineers, and drive automation initiatives.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "5 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "Manual QA Tester",
            "company": "Andersen Lab",
            "location": "Tbilisi, Georgia",
            "description": "We are looking for a detail-oriented Manual QA Tester to join our team. You will execute test cases, report bugs, and collaborate with developers to ensure high software quality.",
            "via": "vacancies.ge",
            "link": "https://vacancies.ge",
            "posted": "1 day ago",
            "source": "vacancies.ge"
        },
        {
            "title": "QA Engineer — Mobile",
            "company": "Glovo",
            "location": "Tbilisi, Georgia",
            "description": "Glovo is looking for a Mobile QA Engineer to test our iOS and Android applications. Experience with Appium or XCUITest is a plus.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "4 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "SDET Engineer",
            "company": "Epam Systems",
            "location": "Remote",
            "description": "EPAM is seeking an SDET to design and implement test automation frameworks. You will work with cross-functional teams on enterprise-level software products.",
            "via": "Google Jobs",
            "link": "https://jobs.epam.com",
            "posted": "2 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Automation Engineer",
            "company": "Wargaming",
            "location": "Tbilisi, Georgia",
            "description": "Wargaming is hiring a QA Automation Engineer for our game platform team. You will develop automated tests for backend services and APIs using Python and pytest.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "6 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "Junior QA Engineer",
            "company": "Sweeft Digital",
            "location": "Tbilisi, Georgia",
            "description": "Great opportunity for a Junior QA Engineer to grow in a dynamic tech company. You will learn test automation, work on real projects, and be mentored by senior engineers.",
            "via": "hr.ge",
            "link": "https://hr.ge",
            "posted": "Today",
            "source": "hr.ge"
        },
        {
            "title": "QA Engineer — Fintech",
            "company": "Credo Bank",
            "location": "Tbilisi, Georgia",
            "description": "Credo Bank is looking for a QA Engineer with experience in fintech products. You will test payment systems, APIs, and mobile banking apps in a regulated environment.",
            "via": "vacancies.ge",
            "link": "https://vacancies.ge",
            "posted": "3 days ago",
            "source": "vacancies.ge"
        },
        {
            "title": "QA Engineer — API Testing",
            "company": "Booking.com",
            "location": "Remote",
            "description": "Booking.com is seeking a QA Engineer specializing in API testing. You will validate REST APIs, write automated tests using Postman and Python, and ensure backend reliability at scale.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "2 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "Performance QA Engineer",
            "company": "Criteo",
            "location": "Remote",
            "description": "Join Criteo as a Performance QA Engineer. You will design and run load tests using JMeter and Gatling, analyze results, and work with teams to optimize system performance.",
            "via": "Google Jobs",
            "link": "https://www.criteo.com/jobs/",
            "posted": "1 week ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer — E-commerce",
            "company": "Joom",
            "location": "Remote",
            "description": "Joom is hiring a QA Engineer for our e-commerce platform. You will test web and mobile apps, maintain regression suites, and ensure smooth customer experiences.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "4 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "Test Automation Engineer",
            "company": "Paysera",
            "location": "Remote",
            "description": "Paysera is looking for a Test Automation Engineer to strengthen our QA team. You will build automation frameworks from scratch and integrate them into our DevOps pipeline.",
            "via": "Google Jobs",
            "link": "https://www.paysera.com/v2/en-GB/jobs",
            "posted": "3 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer — Gaming",
            "company": "Playtika",
            "location": "Remote",
            "description": "Playtika seeks a QA Engineer with gaming industry experience. You will test mobile games, track defects, and work closely with game designers and developers.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "5 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer",
            "company": "Stagwell",
            "location": "Remote",
            "description": "Stagwell is looking for a QA Engineer to join our growing digital agency. You will test web applications and ensure product quality for our diverse client base.",
            "via": "Google Jobs",
            "link": "https://www.stagwellglobal.com/careers/",
            "posted": "2 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "Senior Test Engineer",
            "company": "N26",
            "location": "Remote",
            "description": "N26 is hiring a Senior Test Engineer for our mobile banking platform. You will drive test automation and champion quality across engineering teams.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "1 week ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Analyst",
            "company": "Siemens",
            "location": "Remote",
            "description": "Siemens is seeking a QA Analyst to support software quality for industrial automation products. You will create test plans and execute manual and automated tests.",
            "via": "Google Jobs",
            "link": "https://new.siemens.com/global/en/company/jobs.html",
            "posted": "6 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer — Blockchain",
            "company": "Bitfinex",
            "location": "Remote",
            "description": "Bitfinex is looking for a QA Engineer with interest in blockchain and crypto products. You will test trading platforms, wallets, and APIs in a fast-paced environment.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "3 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — SaaS",
            "company": "Pipedrive",
            "location": "Remote",
            "description": "Pipedrive is hiring a QA Engineer for our CRM platform. You will own quality for key product areas and write automated tests.",
            "via": "Google Jobs",
            "link": "https://www.pipedrive.com/en/jobs",
            "posted": "4 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Proxify",
            "location": "Remote",
            "description": "Proxify connects top QA Engineers with leading tech companies worldwide. Apply now to join our talent network and get matched with exciting remote opportunities.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "Today",
            "source": "LinkedIn"
        },
        {
            "title": "Automation Test Engineer",
            "company": "GlobalLogic",
            "location": "Remote",
            "description": "GlobalLogic is seeking an Automation Test Engineer to work on enterprise software projects using Selenium, TestNG, and CI/CD tools.",
            "via": "Google Jobs",
            "link": "https://www.globallogic.com/careers/",
            "posted": "5 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer — Healthcare",
            "company": "Infermedica",
            "location": "Remote",
            "description": "Infermedica is looking for a QA Engineer to ensure quality of our AI-powered healthcare platform. Experience with API testing is a plus.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "1 week ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — Cloud",
            "company": "DataStax",
            "location": "Remote",
            "description": "DataStax is hiring a QA Engineer for our cloud database products. You will design test strategies for distributed systems.",
            "via": "Google Jobs",
            "link": "https://www.datastax.com/company/careers",
            "posted": "3 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Toptal",
            "location": "Remote",
            "description": "Toptal is looking for a top QA Engineer to join our elite freelance network. Work with the world's leading companies on challenging software projects.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "2 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — AdTech",
            "company": "PubMatic",
            "location": "Remote",
            "description": "PubMatic is hiring a QA Engineer for our advertising technology platform. You will test high-throughput systems and validate data pipelines.",
            "via": "Google Jobs",
            "link": "https://pubmatic.com/careers/",
            "posted": "4 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Lemonade",
            "location": "Remote",
            "description": "Lemonade is seeking a QA Engineer to help us build the future of insurance. You will test our AI-driven platform and ensure a seamless experience for customers.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "6 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — EdTech",
            "company": "Preply",
            "location": "Remote",
            "description": "Preply is looking for a QA Engineer to ensure quality across our language learning platform.",
            "via": "Google Jobs",
            "link": "https://preply.com/en/careers",
            "posted": "1 week ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Deel",
            "location": "Remote",
            "description": "Deel is hiring a QA Engineer to support our global HR platform. You will test payment flows, compliance features, and integrations across 150+ countries.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "3 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — Travel",
            "company": "Kiwi.com",
            "location": "Remote",
            "description": "Kiwi.com is looking for a QA Engineer to test our travel booking platform. You will write automated tests and validate complex booking flows.",
            "via": "Google Jobs",
            "link": "https://www.kiwi.com/us/pages/content/careers",
            "posted": "5 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Contentful",
            "location": "Remote",
            "description": "Contentful is seeking a QA Engineer for our content platform. You will ensure product quality through manual and automated testing.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "2 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — Logistics",
            "company": "Sennder",
            "location": "Remote",
            "description": "Sennder is hiring a QA Engineer for our digital freight platform. You will test complex logistics workflows, APIs, and integrations.",
            "via": "Google Jobs",
            "link": "https://www.sennder.com/careers",
            "posted": "4 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Personio",
            "location": "Remote",
            "description": "Personio is looking for a QA Engineer to ensure quality of our HR software. You will own test automation for core product features.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "1 week ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — Security",
            "company": "Recorded Future",
            "location": "Remote",
            "description": "Recorded Future is hiring a QA Engineer for our threat intelligence platform. You will ensure reliability of our data feeds and dashboards.",
            "via": "Google Jobs",
            "link": "https://www.recordedfuture.com/careers",
            "posted": "3 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Miro",
            "location": "Remote",
            "description": "Miro is seeking a QA Engineer to help us deliver a world-class collaborative whiteboard platform.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "5 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — IoT",
            "company": "Canonical",
            "location": "Remote",
            "description": "Canonical is looking for a QA Engineer with interest in IoT and embedded systems. You will test Ubuntu Core and related tools.",
            "via": "Google Jobs",
            "link": "https://canonical.com/careers",
            "posted": "6 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Typeform",
            "location": "Remote",
            "description": "Typeform is hiring a QA Engineer to ensure quality of our form and survey platform.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "2 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — Data",
            "company": "Airbyte",
            "location": "Remote",
            "description": "Airbyte is looking for a QA Engineer to validate our data integration platform. You will test connectors, pipelines, and UI.",
            "via": "Google Jobs",
            "link": "https://airbyte.com/careers",
            "posted": "1 week ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Hotjar",
            "location": "Remote",
            "description": "Hotjar is seeking a QA Engineer to help deliver our user behavior analytics platform.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "4 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — Payments",
            "company": "Paddle",
            "location": "Remote",
            "description": "Paddle is hiring a QA Engineer for our payments infrastructure. You will test billing flows, tax calculation, and merchant integrations.",
            "via": "Google Jobs",
            "link": "https://www.paddle.com/careers",
            "posted": "3 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Remote.com",
            "location": "Remote",
            "description": "Remote.com is looking for a QA Engineer to support our global employment platform.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "Today",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — AI",
            "company": "Hugging Face",
            "location": "Remote",
            "description": "Hugging Face is seeking a QA Engineer to test our AI model hub and developer tools.",
            "via": "Google Jobs",
            "link": "https://huggingface.co/jobs",
            "posted": "5 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "monday.com",
            "location": "Remote",
            "description": "monday.com is hiring a QA Engineer for our work management platform. You will own quality for key product areas.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "1 week ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — Media",
            "company": "Dailymotion",
            "location": "Remote",
            "description": "Dailymotion is looking for a QA Engineer for our video streaming platform. You will test video playback and ad delivery.",
            "via": "Google Jobs",
            "link": "https://www.dailymotion.com/en/careers",
            "posted": "4 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Loom",
            "location": "Remote",
            "description": "Loom is seeking a QA Engineer to help us deliver a seamless async video communication experience.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "3 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — PropTech",
            "company": "Homeday",
            "location": "Remote",
            "description": "Homeday is hiring a QA Engineer for our real estate platform. You will ensure quality of property listings and valuation tools.",
            "via": "Google Jobs",
            "link": "https://www.homeday.de/en/careers/",
            "posted": "6 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Factorial HR",
            "location": "Remote",
            "description": "Factorial HR is looking for a QA Engineer to ensure quality of our HR management platform.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "2 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — Supply Chain",
            "company": "Flexport",
            "location": "Remote",
            "description": "Flexport is seeking a QA Engineer for our supply chain platform. You will test freight booking, tracking, and customs workflows.",
            "via": "Google Jobs",
            "link": "https://www.flexport.com/careers/",
            "posted": "1 week ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Phrase",
            "location": "Remote",
            "description": "Phrase is hiring a QA Engineer for our localization platform. You will test translation workflows and integrations.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "5 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — InsurTech",
            "company": "wefox",
            "location": "Remote",
            "description": "wefox is looking for a QA Engineer for our insurance platform. You will test policy management, claims, and payment flows.",
            "via": "Google Jobs",
            "link": "https://www.wefox.com/en/careers",
            "posted": "3 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Brex",
            "location": "Remote",
            "description": "Brex is seeking a QA Engineer for our corporate finance platform. You will ensure quality of expense management and banking features.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "4 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — LegalTech",
            "company": "Ironclad",
            "location": "Remote",
            "description": "Ironclad is hiring a QA Engineer for our contract management platform. You will test document workflows and e-signature integrations.",
            "via": "Google Jobs",
            "link": "https://ironcladapp.com/careers/",
            "posted": "1 week ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Veriff",
            "location": "Remote",
            "description": "Veriff is looking for a QA Engineer to ensure quality of our identity verification platform.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "2 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — FoodTech",
            "company": "Deliveroo",
            "location": "Remote",
            "description": "Deliveroo is hiring a QA Engineer for our food delivery platform. You will test ordering, payment, and dispatch flows.",
            "via": "Google Jobs",
            "link": "https://careers.deliveroo.co.uk/",
            "posted": "5 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Pitch",
            "location": "Remote",
            "description": "Pitch is seeking a QA Engineer to help us build the best presentation tool in the world.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "3 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — Climate",
            "company": "Planetly",
            "location": "Remote",
            "description": "Planetly is looking for a QA Engineer to support our carbon management platform.",
            "via": "Google Jobs",
            "link": "https://www.planetly.com/careers",
            "posted": "6 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Smallpdf",
            "location": "Remote",
            "description": "Smallpdf is hiring a QA Engineer to ensure quality of our PDF productivity platform.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "4 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — HR Tech",
            "company": "Workmotion",
            "location": "Remote",
            "description": "Workmotion is seeking a QA Engineer for our global employment platform.",
            "via": "Google Jobs",
            "link": "https://www.workmotion.com/careers",
            "posted": "1 week ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Scoro",
            "location": "Remote",
            "description": "Scoro is looking for a QA Engineer to ensure quality of our business management platform.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "2 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — MarTech",
            "company": "Supermetrics",
            "location": "Remote",
            "description": "Supermetrics is hiring a QA Engineer for our marketing data platform. You will test data connectors and reporting integrations.",
            "via": "Google Jobs",
            "link": "https://supermetrics.com/careers",
            "posted": "3 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Omnisend",
            "location": "Remote",
            "description": "Omnisend is seeking a QA Engineer for our email and SMS marketing platform.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "5 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — DevTools",
            "company": "Raycast",
            "location": "Remote",
            "description": "Raycast is looking for a QA Engineer to help us build the best productivity tool for developers.",
            "via": "Google Jobs",
            "link": "https://www.raycast.com/careers",
            "posted": "4 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Printify",
            "location": "Remote",
            "description": "Printify is hiring a QA Engineer for our print-on-demand platform.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "1 week ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — CRM",
            "company": "Copper",
            "location": "Remote",
            "description": "Copper is seeking a QA Engineer for our Google Workspace CRM.",
            "via": "Google Jobs",
            "link": "https://www.copper.com/careers",
            "posted": "6 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Lokalise",
            "location": "Remote",
            "description": "Lokalise is looking for a QA Engineer to ensure quality of our localization platform.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "3 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — HealthTech",
            "company": "Kry",
            "location": "Remote",
            "description": "Kry is hiring a QA Engineer for our digital healthcare platform. You will test video consultations and booking flows.",
            "via": "Google Jobs",
            "link": "https://www.kry.se/en/careers/",
            "posted": "5 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Maze",
            "location": "Remote",
            "description": "Maze is seeking a QA Engineer to ensure quality of our user research platform.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "2 days ago",
            "source": "LinkedIn"
        },
        {
            "title": "QA Engineer — WealthTech",
            "company": "Bitpanda",
            "location": "Remote",
            "description": "Bitpanda is hiring a QA Engineer for our investment platform. You will test trading flows and asset management features.",
            "via": "Google Jobs",
            "link": "https://www.bitpanda.com/en/career",
            "posted": "4 days ago",
            "source": "Google Jobs"
        },
        {
            "title": "QA Engineer",
            "company": "Usercentrics",
            "location": "Remote",
            "description": "Usercentrics is looking for a QA Engineer for our consent management platform.",
            "via": "LinkedIn",
            "link": "https://www.linkedin.com/jobs/",
            "posted": "1 week ago",
            "source": "LinkedIn"
        }
    ]


def filter_jobs_by_location(jobs, candidate_location):
    if not candidate_location:
        return jobs
    candidate_location = candidate_location.lower()
    location_keywords = candidate_location.replace("(utc+4)", "").replace("(utc+3)", "").strip().split(",")
    location_keywords = [l.strip() for l in location_keywords]
    relevant = []
    for job in jobs:
        job_location = job["location"].lower()
        job_title = job["title"].lower()
        if any(word in job_location for word in ["remote", "anywhere", "worldwide"]):
            job["location"] = "🌍 Remote"
            relevant.append(job)
            continue
        if any(loc in job_location for loc in location_keywords if loc):
            relevant.append(job)
            continue
        if "remote" in job_title:
            relevant.append(job)
            continue
    if not relevant:
        return jobs
    return relevant
