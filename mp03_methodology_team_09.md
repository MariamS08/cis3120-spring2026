

### 6.1 Ticker-list rationale

#TODO: For each industry, justify any modifications to the seeded ticker list. Identify what the seeded list undercounts or overcounts and explain how your changes address those limitations.*
#The seeded ticker list shows both industries, but it was changed in order to show the location-based activity that was going.
#For financial services, the original list focused on money-center, regional banking institutions and didnt really go indepth on other pyshical infrastructure chnages like data centers, operations hubs, and corporate office relocations. So in order to fix this the team made sure to cover accross banking, asset management, insurance, and payment networks in oder to ensure a wide variety of location-driven events
# For travel and hospitality, the seeded list already had the hotels, arilines, cruise lines, and online travel platforms, but since these gave different locations. So the final list was done in order to maintain balance accross the assets and network bases, making sure that the property level and route are represented 

### 6.2 Search-phrase rationale

*TODO: For each industry, justify any modifications to the seeded phrase list. Note any phrases that returned high-volume false positives or missed event categories the team considered important.*

* The seeded phrase lists were made to be used in corporate disclosures of location-based events, while testing the team saw the differences that were going and emerging across the industries.
* for financial services, there were certain phrases that didn't quite catch the meaning that they were going for so the team decided to improve on the phrases so they could more accurately emphasize the physical location.
* The travel and hospitality, there were some terms that were not fitting and gave irrelevant marketing results, in order to fix this the team prioritized more operationally specific phrases. 

### 6.3 Window-experiment results

*TODO: Insert the populated `window_results` table here (as Markdown) and explain why the chosen window is appropriate. Address the cost ceiling explicitly.*

### 6.4 Stage 3 classification quality per industry

*TODO: For each industry, document observed precision and any patterns in the Stage 3 classifications (false positives, false negatives, ambiguous cases). Use small numerical examples where possible.*
* The financial services have had pretty fair amounts to high precision after increasing the ticker and the phrase list. Most have turn into postive outcomes. For example there would be 14 relevant events out of 20 classifications. 
* As for Travel & Hospitality it gave a lower precision since it gave promotional or renovation and it gave better fitting for the expansion events. Postives involved hotel openings, resorts, and property.
### 6.5 Limitations

*TODO: Identify limitations the team encountered and discuss how each affects the comparative reflection.*
