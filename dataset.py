import json

def create_career_dataset():
    # Generate 500 career guidance Q&A pairs
    data = []
    
    # STEM Careers
    stem_base = [
        ("I love chemistry and math. What career should I consider?", "Based on your interest in chemistry and math, consider careers in chemical engineering, pharmacology, materials science, or data science."),
        ("What can I do with a physics degree?", "Physics opens doors to research, engineering, data analysis, finance, or technology consulting."),
        ("I'm good at biology. What are my options?", "Biology leads to medicine, research, biotechnology, environmental science, or pharmaceutical work."),
        ("What careers use mathematics daily?", "Mathematics is used in finance, data science, engineering, cryptography, and actuarial science."),
        ("I want to work in technology. What should I study?", "Technology careers benefit from computer science, engineering, mathematics, or information systems studies."),
        ("What can I do with an engineering degree?", "Engineering offers paths in design, manufacturing, consulting, project management, or research."),
        ("I'm interested in environmental science. What jobs are available?", "Environmental science leads to conservation, consulting, research, policy work, or renewable energy."),
        ("What careers combine science and business?", "Consider biotechnology management, pharmaceutical sales, technical consulting, or science policy."),
        ("I like computer science but not programming. What options exist?", "CS skills apply to project management, systems analysis, technical writing, or product management."),
        ("What can I do with a statistics degree?", "Statistics leads to data analysis, market research, quality control, or biostatistics.")
    ]
    
    # Healthcare Careers
    healthcare_base = [
        ("I enjoy biology and helping people. What career is good for me?", "Your combination of biology interest and desire to help people makes you ideal for healthcare careers like medicine, nursing, physical therapy, or biomedical research."),
        ("What healthcare careers don't require medical school?", "Consider nursing, physical therapy, occupational therapy, medical technology, or healthcare administration."),
        ("I want to help people but don't like blood. What options do I have?", "Consider counseling, social work, physical therapy, speech therapy, or healthcare administration."),
        ("What can I do with a psychology degree?", "Psychology leads to counseling, human resources, research, social work, or organizational development."),
        ("I'm interested in mental health. What careers are available?", "Mental health careers include counseling, social work, psychology, psychiatry, or therapy specializations."),
        ("What healthcare jobs have good work-life balance?", "Consider radiology, pathology, dermatology, or outpatient specialties for better work-life balance."),
        ("I want to work in healthcare but not with patients directly. What options exist?", "Consider medical research, healthcare administration, medical writing, or pharmaceutical work."),
        ("What can I do with a nursing degree besides bedside nursing?", "Nursing opens doors to administration, education, research, consulting, or specialized practice areas.")
    ]
    
    # Business & Finance
    business_base = [
        ("I'm interested in business and economics. What careers should I explore?", "Business and economics knowledge opens paths to financial analysis, consulting, marketing, entrepreneurship, investment banking, or business development."),
        ("What can I do with a finance degree?", "Finance leads to banking, investment analysis, corporate finance, financial planning, or insurance."),
        ("I want to start my own business. What should I study?", "Entrepreneurship benefits from business administration, marketing, finance, or industry-specific knowledge."),
        ("What careers are available in marketing?", "Marketing offers digital marketing, brand management, market research, advertising, or sales roles."),
        ("I'm good with numbers and people. What career fits?", "Consider financial advising, sales, business analysis, or customer success management."),
        ("What can I do with an MBA?", "An MBA opens doors to management, consulting, finance, marketing, or executive leadership roles."),
        ("I want to work in consulting. What skills do I need?", "Consulting requires analytical thinking, communication skills, business knowledge, and problem-solving abilities.")
    ]
    
    # Creative & Arts
    creative_base = [
        ("I'm artistic and creative. What career options do I have?", "Creative talents can lead to graphic design, web design, animation, marketing, architecture, interior design, or multimedia production."),
        ("What can I do with an art degree?", "Art degrees lead to design, illustration, teaching, museum work, or creative direction."),
        ("I like both science and art. Can I combine them in a career?", "Absolutely! Consider scientific illustration, medical animation, data visualization, architectural design, industrial design, or science communication."),
        ("What careers are available in media and entertainment?", "Media careers include film production, journalism, broadcasting, social media, or content creation."),
        ("I want to work in fashion. What are my options?", "Fashion offers design, merchandising, marketing, styling, or retail management opportunities."),
        ("What can I do with a music degree?", "Music leads to performance, education, production, therapy, or music business roles.")
    ]
    
    # Law & Government
    law_base = [
        ("Can I do law if I'm not good at math?", "Absolutely! Law requires strong analytical thinking, reading comprehension, and communication skills rather than advanced math."),
        ("What can I do with a law degree besides practicing law?", "Law degrees lead to business, consulting, government, compliance, or policy work."),
        ("I'm interested in politics. What career paths exist?", "Politics offers campaign management, policy analysis, government relations, or public administration."),
        ("What careers are available in criminal justice?", "Criminal justice leads to law enforcement, corrections, legal assistance, or security work.")
    ]
    
    # Technology
    tech_base = [
        ("I want to work in tech but don't know programming. What options do I have?", "Tech careers without programming include product management, technical writing, UX research, digital marketing, data analysis, or tech sales."),
        ("What can I do with a computer science degree?", "CS leads to software development, data science, cybersecurity, systems analysis, or technology management."),
        ("I'm interested in cybersecurity. What should I study?", "Cybersecurity benefits from computer science, information systems, or specialized security certifications."),
        ("What careers are available in data science?", "Data science offers analysis, machine learning, business intelligence, or research opportunities.")
    ]
    
    # General Career Advice
    general_base = [
        ("What careers have good job security and growth potential?", "Healthcare, technology, data analysis, and skilled trades typically offer strong job security. Specific roles include software development, nursing, data science, cybersecurity."),
        ("I want a career that allows remote work. What options do I have?", "Remote-friendly careers include software development, digital marketing, technical writing, graphic design, data analysis, online education, consulting."),
        ("What careers pay well without requiring a college degree?", "High-paying careers without degrees include skilled trades, sales, real estate, or technology certifications."),
        ("I want to make a difference in the world. What careers allow this?", "Impact careers include healthcare, education, non-profit work, environmental science, or social work.")
    ]
    
    # Combine all base questions
    all_bases = [stem_base, healthcare_base, business_base, creative_base, law_base, tech_base, general_base]
    
    # Generate variations to reach 500
    for base_list in all_bases:
        for q, a in base_list:
            data.append({"input": q, "output": a})
            
            # Add variations
            variations = [
                f"Can you tell me about {q.lower()}",
                f"What about {q.lower()}",
                f"I'm wondering about {q.lower()}",
                f"Help me understand {q.lower()}",
                f"Could you explain {q.lower()}",
                f"I need advice on {q.lower()}",
                f"What would you recommend for {q.lower()}",
                f"I'm curious about {q.lower()}",
                f"Tell me more about {q.lower()}",
                f"I have questions about {q.lower()}"
            ]
            
            # Add up to 10 variations per question
            for i, var in enumerate(variations):
                if len(data) < 498:  # Leave room for out-of-domain
                    data.append({"input": var, "output": a})
                if i >= 9:  # Limit variations
                    break
    
    # Ensure exactly 500 by trimming or adding
    while len(data) > 498:
        data.pop()
    
    # Add out-of-domain examples
    data.extend([
        {"input": "What's the weather like today?", "output": "I'm designed to help with career and education guidance. I can't provide weather information, but I'd be happy to help you explore career options!"},
        {"input": "How do I cook pasta?", "output": "I specialize in career and education advice rather than cooking. However, if you're interested in culinary careers, I can discuss culinary arts or food science!"}
    ])
    
    with open('career_dataset.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Dataset created with {len(data)} examples")
    return data

if __name__ == "__main__":
    create_career_dataset()