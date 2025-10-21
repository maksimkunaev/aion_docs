# Hallucination Detection Test Examples

## 1. Factual Contradictions (Easy Level)

### Historical Dates
```
"World War II ended in 1945. The Marshall Plan to rebuild Europe was announced in 1944 to help countries recover from the war."
```
**Issue:** Marshall Plan was announced in 1947, not 1944

### Basic Math
```
"The company's revenue grew 25% from $100M to $130M this quarter."
```
**Issue:** 25% of $100M = $125M, not $130M

### Geography
```
"Paris is the capital of France. The famous Eiffel Tower in Paris was built in Rome during the 1889 World's Fair."
```
**Issue:** Eiffel Tower is in Paris, not Rome

### Technology
```
"The iPhone was first released in 2007 by Apple. Steve Jobs announced this revolutionary device in 2008 at the annual conference."
```
**Issue:** Announcement (2007) cannot be after release date

## 2. Logical Inconsistencies (Medium Level)

### Biological Logic
```
"All birds can fly. Penguins are birds. Penguins live in Antarctica where they swim underwater to catch fish and never leave the ground."
```
**Issue:** Contradicts "all birds can fly"

### Temporal Logic
```
"Einstein published his theory of relativity in 1905. This theory was influenced by Newton's work on quantum mechanics from 1687."
```
**Issue:** Newton didn't work on quantum mechanics (20th century concept)

### Causal Logic
```
"The patient's blood pressure dropped to dangerous levels after taking the medication. This improvement in cardiovascular health was concerning to doctors."
```
**Issue:** Dangerous drop isn't "improvement"

## 3. Fake Citations (Hard Level)

### Legal Cases
```
"In Smith v. Johnson (2023), the Supreme Court ruled that AI-generated content cannot be copyrighted. This landmark decision in 487 U.S. 234 established new precedent for intellectual property law."
```
**Issue:** Completely fabricated case

### Academic Papers
```
"According to a study by Williams et al. in the Journal of Advanced Computing (2024), neural networks demonstrate vegetative electron microscopy capabilities."
```
**Issue:** "Vegetative electron microscopy" is nonsensical

### Medical Research
```
"Research published in Nature Medicine (2024) by Dr. Anderson shows that eating small rocks provides essential minerals. The study followed 500 participants over 6 months."
```
**Issue:** Dangerous and false medical advice

## 4. Scientific Impossibilities (Medium Level)

### Physics Violations
```
"The new car engine achieves 150% energy efficiency by converting heat back into gasoline through thermodynamic reversal."
```
**Issue:** Violates conservation of energy

### Chemistry Errors
```
"Water (H2O) can be split into hydrogen and helium using standard electrolysis at room temperature."
```
**Issue:** Water doesn't contain helium

### Biology Nonsense
```
"Humans can photosynthesize like plants by eating chlorophyll supplements, eliminating the need for food."
```
**Issue:** Human biology doesn't support photosynthesis

## 5. Real vs Fake Mixed (Advanced Level)

### Tech Company Facts
```
"Google was founded in 1998 by Larry Page and Sergey Brin. The company's first office was located in a garage in Menlo Park. In 2001, Google acquired YouTube for $1.65 billion."
```
**Issue:** Google acquired YouTube in 2006, not 2001

### Celebrity Information
```
"Elon Musk founded Tesla Motors and serves as CEO. He also founded SpaceX in 2002. In 2023, he became the first person to travel to Mars on a SpaceX mission."
```
**Issue:** No one has traveled to Mars yet

### Historical Events
```
"The Berlin Wall was built in 1961 and fell in 1989. It separated East and West Berlin during the Cold War. The wall was 12 feet high and made entirely of concrete and steel."
```
**Issue:** Wall wasn't "entirely" concrete and steel (included barbed wire, guards, etc.)

## 6. Subtle Misrepresentations (Expert Level)

### Medical Advice
```
"Aspirin helps prevent heart attacks by thinning the blood. Doctors recommend taking 325mg daily for all adults over 40 as a preventive measure."
```
**Issue:** Not recommended for ALL adults - requires individual assessment

### Legal Interpretation
```
"The First Amendment protects all forms of speech in the United States without any exceptions or limitations."
```
**Issue:** There are established exceptions (incitement, defamation, etc.)

### Investment Advice
```
"Diversified index funds always outperform individual stocks over any 10-year period, making them risk-free investments."
```
**Issue:** No investment is truly "risk-free"

## 7. Fabricated Statistics (Medium Level)

### Health Statistics
```
"Recent studies show that 94% of people who drink coffee daily live longer than non-coffee drinkers. The study followed 50,000 participants for 20 years."
```
**Issue:** Highly specific fake statistic

### Economic Data
```
"The GDP of Monaco increased by 847% in 2023, making it the fastest-growing economy globally."
```
**Issue:** Impossible growth rate for developed economy

### Technology Usage
```
"According to Pew Research (2024), 89% of teenagers now prefer AI tutors over human teachers for learning mathematics."
```
**Issue:** Likely fabricated statistic and source

## 8. Date/Timeline Errors (Easy Level)

### Recent Events
```
"The COVID-19 pandemic began in 2019 and was declared over by the WHO in 2021."
```
**Issue:** WHO didn't declare it "over" in 2021

### Technology Timeline
```
"Facebook was founded by Mark Zuckerberg in 2004. Instagram, also created by Zuckerberg, launched in 2008."
```
**Issue:** Instagram was founded by Kevin Systrom and Mike Krieger in 2010

## 9. Measurement Errors (Easy Level)

### Distance/Size
```
"The distance from New York to Los Angeles is approximately 500 miles by air."
```
**Issue:** Actually ~2,500 miles

### Weight/Mass
```
"An average elephant weighs about 500 pounds, making them one of the lighter large mammals."
```
**Issue:** Elephants weigh 4,000-14,000 pounds

## 10. Authority Misattribution (Medium Level)

### Quote Attribution
```
"As Albert Einstein famously said, 'The internet is becoming the town square for the global village of tomorrow.'"
```
**Issue:** Einstein died in 1955, before the internet

### Book/Author Errors
```
"In his masterpiece '1985', George Orwell predicted the rise of social media surveillance."
```
**Issue:** Book is "1984", not "1985"

## Testing Strategy

**Easy Level:** Start with obvious contradictions
**Medium Level:** Test logical reasoning
**Hard Level:** Challenge domain expertise
**Expert Level:** Require deep knowledge to detect

Use these examples to validate your detector's ability to catch different types of hallucinations across various domains and difficulty levels.