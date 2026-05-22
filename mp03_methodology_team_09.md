

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
    industry	             window_days	     candidate_count	         event_count	    estimated_cost_usd
0	Financial Services	        360	                  84	                     3	                0.006886
1	Travel and Hospitality	    360	                  59	                     8	                0.310000

The chosen window length was 360 days. This was selected because the shorter windows did not produce enough usable financial services events. At the max window of 360 days financial services only produced 3 location events, while travel and hospitality produced more than the target threshold. The estimated cost remained below $3.00. The API cost was controlled by filtering EDGAR candidates by ticker before stage 3 classification, which prevented the model from classifying every raw EDGAR result.

### 6.4 Stage 3 classification quality per industry

*TODO: For each industry, document observed precision and any patterns in the Stage 3 classifications (false positives, false negatives, ambiguous cases). Use small numerical examples where possible.*
* The financial services have had pretty fair amounts to high precision after increasing the ticker and the phrase list. Most have turn into postive outcomes. For example there would be 14 relevant events out of 20 classifications. 
* As for Travel & Hospitality it gave a lower precision since it gave promotional or renovation and it gave better fitting for the expansion events. Postives involved hotel openings, resorts, and property.
### 6.5 Limitations

*TODO: Identify limitations the team encountered and discuss how each affects the comparative reflection.*
One limitation that we as a team encountered was the financial services pipeline only producing 3 geocoded events, even at the 360 day window ceiling. This made the sample size of the financial services pipeline smaller when compared to the travel and hospitality pipeline.

Another limitation that we faced was the EDGAR search depending heavily on the selected ticker and phrase lists. Even though the list was expanded, the financial services ticker list still missed a lot of companies.
