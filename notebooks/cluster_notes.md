The following notes describe the trends seen for each KMeans cluster. 

**Note: All ToxPrints of the form 'tp_fp\<x\>' are offset from Cheminformatics Module and ChemoTyper ToxPrint definitions by a value of 1. i.e., 'tp_fp1' is ToxPrint 2 in ChemoTyper and the Cheminformatics Modules.**

Additional Notes: As we've discussed before, KMeans clustering will favor forming small break-off clusters over breaking up large groups of chemicals. In addition, it will be biased toward placing small chemicals close to one another even if they do not have much in common. One worthwhile statistic to add to this study might be the average and standard deviation of the molecular weights of chemicals in each cluster. 

## 0*: 
- 441 members, 227 uncategorized
- No interesting NCC trends - almost entirely uncategorized or Neutral Organics (NOs)
- Most members outside of the ARN domain
- t-SNE shows some localization, with many of teh chemicals appearing in the same regions as each other, but some smaller clusters of chemicals disconnected from the main groups and spread out from one another quite a bit. 
- ToxPrints characterized by any halide bond (ToxPrint 302)
- Many ToxPrints (97 at 99.5% confidence) occur with unusual increased frequency. None of these occur in 80% of the cluster or more. 

Summary: This cluster contains many newly categorized chemicals containing halide bonds. There is not a detailed ToxPrint backbone for the cluster, but there are many ToxPrints that occur with unusual frequency for the cluster, which may be worth investigating further.

## 1:
- 156 members, 8 uncategorized - almost entirely categorized by ARN or NCC (though most NCC classifications are NO), 
- NCCs are mostly NO or uncategorized, but also include Epoxides, Alkoxysilanes, and Ethylene Glycol Ethers. 
- Dominantly in the Ethoxylated \<C6 alcohols ARN
- t-SNE shows strong logalization, with two primary visual clusters of chemicals and some mild scattering in the same regions as those clusters
- No ToxPrint backbone, 39 at 99.5% confidence. 2 of these occur in 80% or more of the chemicals: 114 and 437

Summary: This cluster is largely already categorized by ARN. There is not a definitive ToxPrint backbone, though further investigation might show commonly ocurring features.

## 2:
- 495 members, 91 uncategorized - often categorized by ARN or both
- contains a few members from *many* (22) unique NCCs, though only NOs are prominently featured. 
- Members are sorted into at least 24 ARNs as well, with Simple Lithium Compounds the most common but still making up less than 25% of classification. 
- t-SNE shows some localization, with 3 regions containing most of the members of this cluster. One is a very tight cluster, one is a looser cluster and some of its t-SNE neighbors, and one region just contains some scattered members of this KMeans. 
- ToxPrint backbone consists of 437-440, which all represent Carbon chains. 93 @ 99.5%, 2 in more than 80% of chemicals - 441 and 442 (C6 and C8 chains).

Summary: This cluster appears to be formed by chemicals containing Carbon chains with length 4+. This is the primary defining feature of the cluster, which contains chemicals sorted into many different ARNs and NCCs. It will be worthwhile to examine whether other clusters show this trend as well, however the inability to differentiate beyond the presence of carbon chains may make this a weak cluster. 

## 3*:
- 11 members, entirely uncategorized
- very few members, but all very tightly packed together in t-SNE
- ToxPrint backbone consists of 16 ToxPrints: 
    - 'tp_fp4', metal: poor metal
    - 'tp_fp45', carboxylic ester acyclic
    - 'tp_fp46', carboxylic ester aliphatic
    - 'tp_fp48', carboxylic ester alkyl
    - 'tp_fp70', carbonyl generic
    - 'tp_fp134', CS sulfide
    - 'tp_fp323', metal group 3 other generic
    - 'tp_fp337', metal group 3 other Sn generic
    - 'tp_fp339', metal group 3 other Sn organo
    - 'tp_fp342', metal group 3 other Sn sulfide 
    - 'tp_fp436', alkaneLinear_ethyl_C2(H_gt_1)
    - 'tp_fp437', chain:alkaneLinear_ethyl_C2_(connect_noZ_CN=4)
    - 'tp_fp438', chain:alkaneLinear_propyl_C3
    - 'tp_fp439', chain:alkaneLinear_butyl_C4
    - 'tp_fp440', chain:alkaneLinear_hexyl_C6
    - 'tp_fp441', chain:alkaneLinear_octyl_C8
Beyond this backbone, at 99.5% confidence only 25 ToxPrints (so 9 extra) occur with unusual increased frequency, and none are present in 80% or more of the cluster. This could indicate some stability to the backbone.

Summary: Cluster 3, while small, has a relatively clear definition and pattern defined entirely on chemicals not previously classified by either ARN or NCC. These chemicals have Sn-sulfide, carboxylic esters, and carbon chains of at least 8 carbons. This cluster could likely be meaningfully defined by structure. 

## 4:
- 126 members, 30 uncategorized
- Most members are not categorized by NCC, but those that are almost all fall into the Polynitroaromatics and/or Analines groups
- ARN categorizes about 25% of this cluster into one of three groups: nitroalkanes, chlorinated aromatic hydrocarbons, and Isophthalates, Terephthalates
- This cluster is strongly localized on the t-SNE, forming one tight cluster with only a few outlier members scattered elsewhere in the plot. 
- The Toxprint backbone is just ToxPrint 197, bond:N(=O)_nitro_C. At 99.5% confidence, 34 ToxPrints occur with unusual increased frequency. Only 196 and 586 occur in more than 80% of the cluster. 

Summary: This cluster has some semblance of a ToxPrint backbone, and its increased-frequency ToxPrints may be worth exploring. The cluster does not contribute very many newly categorized chemicals overall.

## 5: 
- 200 members, 10 uncategorized
- More than 50% of members are categorized by both ARN and NCC, though the vast majority of NCC categorizations are NO. About 20% of this cluster is categorized into the Aldehydes (Acute toxicity) NCC, 10% into Anionic Surfactants, and the rest are scattered among 7 others NCCs or uncategorized.
- ARN categorization is extremely diverse, covering more than 15 ARNS, though 1-2 ethanediols..., Aralkylaldehydes, and Linear and branched alpha-beta... account for about 1/3 of the cluster. 
- This cluster is moderately localized on the t-SNE, with most members in the same are but not tightly clustered, and interspersed significantly with non-members. 
- The ToxPrint backbone for this cluster consists of ToxPrints 437-439, with 45 ToxPRints occuring with unusually high frequency with 99.5% confidence and, in particular, the 7 ToxPrints 440, 441, 459, 463, 464, 466, and 467 all present in more than 80% of the cluster. 
    - As seen before, the first two correspond to carbon chains. All others define other features of Carbon-carbon bonding as well. 

Summary: This cluster may not have significant value in category gap-filling, due to its messy overlap with ARN and NCC categorizations and the very few uncategorized chemicals that currently belong in the cluster. However, there appears to be a relatively robust potential structural set of trends for the cluster, which could make it easy to meaningfully define or draw conclusions about. 

## 6*:
- 24 members, 20 uncategorized
- The only members categorized by NCC are in Esters (Acute toxicity)
- The only members categorized by ARN are in Salicylic acid, its salts and... (I believe that entire category is contained within this cluster)
- This cluster is strongly localized in the t-SNE, with all members in a very tight visual cluster.
- The cluster has a 12-ToxPrint backbone, and while 23 @ 99.5%, no extras are in 80% or more of the chemicals. The ToxPrint backbone is:
    - 'tp_fp34', bond:C(=O)N_carboxamide_(NHR)
    - 'tp_fp36', bond:C(=O)N_carboxamide_generic
    - 'tp_fp70', bond:C=O_carbonyl_generic
    - 'tp_fp122', bond:COH_alcohol_aromatic
    - 'tp_fp123', bond:COH_alcohol_aromatic_phenol
    - 'tp_fp128', bond:COH_alcohol_generic
    - 'tp_fp205', bond:N=N_azo_aromatic
    - 'tp_fp207', bond:N=N_azo_generic
    - 'tp_fp214', bond:NC=O_aminocarbonyl_generic
    - 'tp_fp476', chain:aromaticAlkane_Ph-C1_acyclic_generic
    - 'tp_fp585', ring:aromatic_benzene
    - 'tp_fp591', ring:fused_\[5_7\]_azulene
    
Summary: This is one of the most structurally stable clusters seen so far and is almost entirely uncategorized by ARN and NCC. The ToxPrint backbone is clear and consistent. This is likely a very good addition to the ARNs and NCCs. 

## 7 (=):
- 1 member, 0 uncategorized

Summary: Cluster 7 contains a single chemical that is sorted by ARN only into the category Esters from linear saturated dicarboxylic acid... with 35.7% confidence. The small size of the cluster, as well as the fact that its sole member is already meaningfully categorized by ARN, makes this essentially a useless cluster. It would at most be worth expert assessment of whether this chemical has been accurately sorted by the ARN random forest. 

## 8:
- 587 members, 60 uncategorized
- Only about 20% of chemicals are categorized by NCC, and almost all of them are placed in the Anionic Surfactants category. 
- ARN categorizations span more than 20 categories, with Branched carboxylic acids, Alpha-chloro aliphatic carboxy..., and Linear aliphatic ketones accounting for the largest groups (more than 50% of the total cluster). 
- A large majority of the chemicals in this cluster are in the same region of the t-SNE, but the cluster is not tightly-packed and there are multiple other tiny clusters of chemicals outside of the primary region. 
- The cluster has no ToxPrint backbone, and 100 @ 99.5% with only a single ToxPrint occurring in more than 80% of chemicals: ToxPrint 71, the generic carbonyl bond.

Summary: A significant majority of the chemicals in this cluster are already categorized by ARN into a diverse array of groups. There are a relatively large number of uncategorized chemicals in the cluster, but there is no simple structural definition for the cluster, as it appears to cover too diverse a portion of the chemical space. The cluster could be important, but will not be easily linked to meaning and may also not be of much use or meaning on its own. It may instead be worth considering uncategorized chemicals in this cluster as closely related to the ARNs or NCCs covered by teh categorized chemicals in the cluster. - could we expand any of their definitions slightly to include chemicals from this cluster? 

## 9 (=):
- 63 chemicals, 0 uncategorized - All are categorized by ARN with most additionally categorized by NCC
- Almost all of these chemicals are categorized into one of the two NCC Esters categories (Acute or Chronic toxicity) and also in NO, with a couple uncategorized.
- Nearly 50% of the chemicals are in the Linear and branched alpha-beta... ARN, another 33% are in Esters from branched or non-ar..., and the rest are distributed among Aliphatic nitriles, acrylate and mathacrylate amines, alpha-chloro aliphatic carboxy..., Brominated cycloalkanes, alcoh..., and Esters from linear saturated d...
- Despite the small group size, there are 2 distinct clusters of this KMeans on the t-SNE plot and one outlier chemical. The two clusters are very densely packed. 
- There is a 6 ToxPrint backbone, with only 18 @ 99.5% plus 3 additional ToxPrints present in more than 80% of the sample (47, 49 - bond:C(=O)O_carboxylicEster_alkyl, 441 - 8-chain). The backbone is the following:
    - 'tp_fp45', carboxylic ester aliphatic
    - 'tp_fp70', bond:C=O_carbonyl_generic
    - 'tp_fp436', 2-chain
    - 'tp_fp437', 3-chain
    - 'tp_fp438', 4-chain
    - 'tp_fp439', 6-chain

Summary: This cluster represents an interesting overlap between ARNs and NCCs, though it contributes no newly categorized chemicals to our clustering methods. 

## 10: 
-94 members, 45 uncategorized, most categorized chemicals are grouped by NCC only
- Interestingly, none of the chemicals are classified as Neutral Organics by NCC. 28% are Anilines (Acute toxicity), 12% Phenols (Acute toxicity), 3% Substituted Triazines (Acute toxicity)
- Only about 20% of the chemicals are sorted by ARN. This is divided amongst 7 categories: Unsubstituted and linear aliph..., chlorinated aromatic hydrocarb..., ortho-phthalates, aralkylamines, aromatic ethers, polycarboxylic acid monoamines, aromatic nitriles
- The t-SNE for this cluster is strongly localized, with almost all chemicals in a densely-packed visual cluster that is even well-separated from most other clusters (though it does share space with some other chemicals). 
- There is no ToxPrint backbone, but there are 37 @ 99.5%, and 12 of these are present in more than 80% of the chemicals *and* 11 of those are present in more than 95% of the chemicals. Those eleven are provided below:
    - 'tp_fp68', bond:C=O_carbonyl_ab-unsaturated_generic
    - 'tp_fp70', bond:C=O_carbonyl_generic
    - 'tp_fp75', bond:CC(=O)C_ketone_alkane_cyclic
    - 'tp_fp81', bond:CC(=O)C_ketone_alkene_cyclic_2-en-1-one
    - 'tp_fp82', bond:CC(=O)C_ketone_alkene_cyclic_2-en-1-one_generic
    - 'tp_fp85', bond:CC(=O)C_ketone_aromatic_aliphatic
    - 'tp_fp86', bond:CC(=O)C_ketone_generic
    - 'tp_fp90', bond:CC(=O)C_quinone_1_4-benzo
    - 'tp_fp91', bond:CC(=O)C_quinone_1_4-naphtho
    - 'tp_fp486', chain:aromaticAlkane_Ph-C1_cyclic
    - 'tp_fp585', ring:aromatic_benzene

Summary: This cluster provides an interesting bridge between a few NCCs and ARNs, while also covering some previously uncategorized chemicals. Although lacking a direct ToxPrint backbone, it appears that structural rules for matching into the cluster could be devised with something like "contains at least 5 of these 11 possible ToxPrints". The cluster could be a significant addition to the categorization model.

## 11: 
- 203 members, 20 uncategorized - over 75% of the chemicals are categorized by ARN, with about 50% categorized by NCC. 
- Chemicals are categorized into 16 different meaningful NCCs + NO. Widely spread across these NCCs with Anionic Surfactants, Esters (both Acute and Chronic toxicity), and Acid Chlorides seieng the greatest distributions (but all under 15%). 
- Approximately 42% of chemicals are in the Linear aliphatic ketones ARN with an additional 20% in Esters from linear saturated d... The rest are distributed amongst at least 12 other ARNs with > 10% membership. 
- The t-SNE for this cluster is moderately localized. All chemicals appear in the same region, but they are very loosely packed in that region and are interspersed significantly with chemicals from other clusters. 
- The cluster has a 5-ToxPrint backbone consisting of ToxPrint 71 and 437-440, 62 @ 99.5%, and 2 additional ToxPrints present in > 80% of the population. As is frequently seen, these 2 are the 6- and 8- chain add-ons to the backbone (441, 442). This makes this cluster's ToxPrint trends identical to cluster 2 except for the presence of ToxPrint 71.

Summary: This cluster does not contain very many uncategorized chemicals, but shows patterns similar to some previously-seen clusters, such as Cluster 2. The cluster does not agree closely with any particular NCC or ARN classification, and overlaps with many groups from both. However, there is at least some basis for deriving a structural definition of this cluster, and further investigation into additional clusters should pay attention to whether this ToxPrint backbone manages to stay unique or is duplicated.

## 12: 
- 125 members, 3 uncategorized - Nearly 95% of chemicals are categorized by NCC, with about 80% categorized by ARN as well.
- 80% of chemicals are in the Acrylates/Methacrylates (Acute toxicity) ARN, and about 90% are in the Esters (Acute toxicity) ARN, such that the majority of chemicals are in both. Many of these are also in NOs, with small (<10 %) overlaps with 6 other NCCs, including the Chronic counterparts of both major groups. 
- More than 50% of chemicals are sorted into the acrylate and methacrylate amines ARN, with another 15% in one of the ARN ester-related groups, and then a smattering of other ARN groups with low frequencies. Only about 5% of chemicals are out of domain, with another 12% sorted into miscellaneous chemistry. 
- The t-SNE is mostly strongly localized, but there are a significant number of distinct outliers. There is a single, dense cluster near the center of the t-SNE plot, but at least 20 chemicals are scattered in isolated locations near the center line of the t-SNE. 
- The ToxPrint backbone is just 71 and 467 (chain:alkeneLinear_mono-ene_ethylene_generic) with 22 @ 99.5% and 3 prints featured in more than 95% of chemicals: 46 - bond:C(=O)O_carboxylicEster_acyclic, 48 - bond:C(=O)O_carboxylicEster_alkenyl, 465 - chain:alkeneLinear_mono-ene_ehtylene_terminal

Summary: This cluster is almost entirely already categorized. Once again, this is a cluster that primarily displays NCC/ARN relationships, rather than contributing a large amount of information for filling gaps in coverage. However, the best approach for determining how this might supplement coverage gaps is likely to look at why the 3 uncategorized chemicals do not fit into the ARN/NCC definitions, to determine what is different about them. At the same time, looking at how those chemicals remain similar to existing ARN groups and NCCs should make the process for defining thsi cluster structurally/through features more clear.  

## 13 (=):
-100 members, 0 uncategorized - About 85% of chemicals are categorized by ARN and NCC both, with the rest categorized by one or the other, NCC having the larger proportion of those
- About 90% of NCC categorizations are Esters (Acute toxicity), with many of those also identified as NO. There is also less than 10% membership for Anilines and Phenols both in the Acute version, Esters (Chronic toxicity), and Hydrazines and Related Compounds.
- About 66% of ARN sorting is into Orthophthalates or Isophthalates and Teraphthalates. The rest is scattered across 6 ARNs, each representing less than 10% of the chemicals.
- The t-SNE plot for this cluster is very similar in quality to that of cluster 12, just with different locations. There is a main cluster with a couple dozen widely scattered outliers. 
- There is no ToxPrint backbone, but there are only 23 @ 99.5% and 5 ToxPrints occuring in 80% of the chemicals or more: 'tp_fp49' - bond:C(=O)O_carboxylicEster_aromatic, 'tp_fp70' - bond:C=O_carbonyl_generic, 'tp_fp436' - chain:alkaneLinear_ethyl_C2(H_gt_1), 'tp_fp476' - chain:aromaticAlkane_Ph-C1_acyclic_generic, 'tp_fp585' - ring:aromatic_benzene

Summary: This is a category that does not add to the existing coverage at all on the current inventory, but again gives a closer look at the relationships between ARNs and NCCs. It might be of interest to determine what sets these (mainly) Acute toxicity Esters apart from others in the KMeans geometry, given that there are more than 1700 Esters (Acute toxicity) in the full set. 

## 14*:
- 531 members, 116 uncategorized - NCC covers about 75% of chemicals, ARN just under 25%, overlapped to leave approximately 20% of chemicals uncategorized
- Other than NOs, no one NCC takes more than 15% of the chemicals. Instead, they are scattered across 23 different NCCs. 
- ARN categorization is likewise chaotic, with Linear aliph... and Cyclic ethers containing the most members, but both with fewer than 55 members.
- Considering the size of the cluster, the t-SNE *is* strongly localized. Almost all chemicals are in the same loosely-packed cluster of the plot which, despite its lack of density, does not appear to contain many chemicals from other clusters. There is some noise and outliers, but the main body of the cluster is genuinely clustered in the t-SNE as well. 
- The cluster has no ToxPrint backbone and 97 @ 99.5%, but it does have 2 ToxPrints appearing in more than 80% of the chemicals: 424 - chain:alkaneBranch_neopentyl_C5 and 432 - chain:alkaneCyclic_ethyl_C2_(connect_noZ). 

Summary: With the large number of uncategorized chemicals contained in this cluster, this is an important chemical for filling coverage gaps. The scattering across ARNs and NCCs suggests that this cluster may indeed represent something not adequately described by those methods. The lack of ToxPrint background may make this a challenge, but the localization of the t-SNE and the relatively rare (in earlier cluster) ToxPrint features that appear frequently in this cluster show promise. 

## 15*: 
- 242 members, 38 uncategorized - ARN covers about 66% of chemicals, NCC around 50%, but overlapped such that 1/6 of chemicals are not categorized
- Only NOs cover more than 10% of the chemicals, but the Acute Anilines, Aldehydes, Epoxides, Phenols, and Esters are all above 5%. 22 NCCs total are featured. 
- More than 25% of the chemicals are in the aromatic ethers ARN, the dominantly largest ARN classificaation. An additional 20 ARNs are featured, all containing less than 10% of the chemicals. 
- The t-SNE shows moderate localization, with 2 main clusters located very close to one another and some scattering around them. The 2 main clusters do not seem to overlap very much with other chemicals, though they each form partial portions of visual clusters in the t-SNE. Many of the chemicals outside the two main clusters form tiny clusters with each other in many different regions. 
- There is no ToxPrint backbone, with 62 @ 99.5 %. 2 ToxPrints appear in 80% or more of the population, 115 - bond:COC_ether_aliphatic__aromatic and 586 - ring:aromatic_benzene

Summary: A significant portion of this cluster is uncategorized, and there is little internal agreement with ARN or NCC. This could be an indicator that this cluster, like the previous one, is adding significant new information to our existing models. While it does not have a ToxPrint backbone, there are common ToxPrints, and examining the trends in these could allow us to derive a better structural definition for the cluster. 

## 16: 
- 222 members, 24 uncategorized - About 80% of cheicals are categorized by ARN, 20% by NCC, and about 10% are uncategorized
- NCC classifications span 9 true categories + NOs, all with minimal membership. 
- Aliphatic nitriles account for more than 50% of the chemicals, with Aromatic nitriles accounting for another 25%. The last 5% categorized by ARN is split among multiple, small ARNs with minimal representation.
- Most chemicals are in clusters in the t-SNE, however there are at least 5 distinct small clusters located far apart in the t-SNE. Many of these small clusters do appear to be isolated from non-cluster chemicals. There are also some isolated chemicals. 
- There is a 1-print ToxPrint backbone, 'tp_fp12' - bond:C#N_nitrile_generic. There are 30 @ 99.5% and only one of these appears in 80% of the chemicals or more: 'tp_fp14' - bond:C#N_nitrile. 

Summary: This seems to be a category that could be labelled "Nitriles", where the ARNs provide a slightly more specific classification. It seems, based on the t-SNE, that these chemicals may not share very much other than their Nitrile features, but it might be worth investigating the underlying structure of the cluster a little bit more. 

## 17: 
- 1 member, 1 uncategorized

Summary: Cluster 17 contains a single chemical that is not sorted into any ARN or NCC. Because this chemical has no neighbors, no generalizations can be drawn. It is a chemical with only 4 ToxPrints: 'tp_fp3', 'tp_fp436', 'tp_fp437', 'tp_fp438', 'tp_fp439', which indicate that it has a metalloid and carbon chain of length 4. This is unlikely to be a helpful cluster in any way, since there is not enough data to create generalizations for what else should be placed in the cluster. 

## 18*: 
- 142 members, 9 uncategorized - most chemicals are sorted by both ARN and NCC, with ARN again covering about 80% of chemicals and NCC covering about 70%.
- Acute Esters and Aldehydes account for between 15 and 20% of chemicals, with Chronic Esters also significantly featured. As usual, many NOs and 4 other NCCs with minimal representations. 
- Linear and branched alpha... covers almost 50% of chemicals for ARN sorting, with the rest scattered widely among 16 ARNs. 
- The t-SNE is very strongly localized, with minimal outliers and a distinct, densely-packed cluster for these chemicals
- There is a ToxPrint backbone of 'tp_fp449'- chain:alkeneBranch_mono-ene_2-butene, 'tp_fp466' - chain:alkeneLinear_mono-ene_ethylene_generic with 40 @ 99.5% and 4 of these are present in 80% or more of the chemicals. 3 of those ('tp_fp436', 'tp_fp437', 'tp_fp438') correspond to carbon chains up to length 3, and the fourth is 'tp_fp462' - chain:alkeneLinear_mono-ene_2-hexene.

Summary: This seems like a category that supplements existing ARNs. Despite the close relationship to LInear and branched alpha..., there appears to be more coverage included in this new category. There is a ToxPrint backbone and good common features that could potentially form a strong structural basis for a definition of this category. It might be worth looking into how much of the primary ARN, Linear and branched alpha..., is contained in this KMeans cluster. 

## 19*: 
- 19 chemicals, 17 uncategorized - 1 each in ARN and NCC
- The NCC chemical is in Anhydrides, Carboxylic acid
- The ARN chemical is in Benzoates
- The t-SNE is extremely localized; all chemicals form a tiny, dense cluster in the bottom-right of the t-SNE
- There is a 13-print ToxPrint backbone: 
    - 'tp_fp421', chain:alkaneBranch_isopropyl_C3
    - 'tp_fp423', chain:alkaneBranch_neopentyl_C5
    - 'tp_fp431', chain:alkaneCyclic_ethyl_C2_(connect_noZ)
    - 'tp_fp434', chain:alkaneCyclic_pentyl_C5
    - 'tp_fp435', chain:alkaneCyclic_hexyl_C6
    - 'tp_fp436', chain:alkaneLinear_ethyl_C2(H_gt_1)
    - 'tp_fp437', chain:alkaneLinear_ethyl_C2_(connect_noZ_CN=4)
    - 'tp_fp438', chain:alkaneLinear_propyl_C3
    - 'tp_fp439', chain:alkaneLinear_butyl_C4
    - 'tp_fp453', chain:alkeneCyclic_diene_cyclohexene
    - 'tp_fp455', chain:alkeneCyclic_ethene_C_(connect_noZ)
    - 'tp_fp456', chain:alkeneCyclic_ethene_generic
    - 'tp_fp601', ring:fused_steroid_generic_[5_6_6_6]
- There are only 18 @ 99.5% and the only one of those present in 80% or more of the chemical sis ToxPrint 71, bond:C=O_carbonyl_generic, which is present in many clusters. 

Summary: This is an almost completely newly categorized cluster. Despite its relatively small size, it does have a handful of chemicals with very robust similarities, which could form a strong structural basis for a new category. Especially considering that ARN classification is also a model and can be wrong, I don't believe that the adjoining NCC or ARN classification should be taken into account much, since they each only apply to a single chemical. The strong localization on the t-SNE also shows that this could be a powerful cluster to add. 

## 20*: 
- 138 chemicals, 3 uncategorized - Almost entirely categorized by both, with ARN and NCC each accounting for only a handful of chemicals not sorted by the other method
- More than 80% of chemicals are in the Esters (Acute toxicity) and Acrylates & Methacrylates (Acute toxicity) NCCs. About 10% of chemicals are in the chronic versions of those two NCCs, and there is minimal representation for another 9 NCCs. As usual, a significant portion of the chemicals are in NOs. 
- About 70% of chemicals are in the Acrylates and Methacrylate amines ARN, with about 5% in Esters from branched or non-arom... and minimal representation for another 11 ARNs. 
- The t-SNE is mostly localized, with a distinct, tight cluster at the center of the plot and some smaller clusters scattered around it. 
- There is a 3-print ToxPrint backbone with 34 @ 99.5% and only 2 of those featured in 80% of the chemicals or more: 'tp_fp45' - bond:C(=O)O_carboxylicEster_acyclic, 'tp_fp47' - bond:C(=O)O_carboxylicEster_alkenyl. The ToxPrint backbone is: 
    - 'tp_fp70', bond:C=O_carbonyl_generic
    - 'tp_fp449', chain:alkeneBranch_mono-ene_2-butene
    - 'tp_fp466', chain:alkeneLinear_mono-
    
Summary: This category appears to be an extension of the ARN/NCC related to Arcylate and Mathacrylate amines. Perhaps the NCC definition could be slightly loosened or expanded to include all of these chemicals, or this could be the broader catch-all category behind that category. It seems clear that chemicals in this cluster are at least closely related to the chemicals in that NCC.

## 21*: 
- 75 members, 37 uncategorized - Almost all categorized chemicals are categorized exclusively by NCC
- About 35% of chemicals are in Esters (Acute toxicity), with another 15% in Aminobenzothiazole Azo Dyes. The rest are scattered among Cationic (quaternary ammonium) surfactants, Esters (Chronic toxicity), and the Acute versions of Imides and Polynitroaromatics. There are no NOs in this set. 
- The only ARN classifications are Bonzoates and Aromatic nitriles. 
- The t-SNE is extremely localized, with a single tight cluster and no noise. There are signs of overlap with chemicals outside the cluster, but all of this cluster's chemicals are very tightly grouped. 
- There is a 9-print ToxPrint backbone: 
    - 'tp_fp93', bond:CN_amine_aliphatic_generic
    - 'tp_fp97', bond:CN_amine_aromatic_generic
    - 'tp_fp106', bond:CN_amine_ter-N_aliphatic
    - 'tp_fp107', bond:CN_amine_ter-N_aromatic
    - 'tp_fp108', bond:CN_amine_ter-N_aromatic_aliphatic
    - 'tp_fp109', bond:CN_amine_ter-N_generic
    - 'tp_fp205', bond:N=N_azo_aromatic
    - 'tp_fp207', bond:N=N_azo_generic
    - 'tp_fp585', ring:aromatic_benzene
- There are 40 @99.5% and 3 ('tp_fp195', 'tp_fp196', 'tp_fp436') in 80% or more of the population

Summary: With its detailed ToxPrint backbone, many uncategorized chemicals, and very clear t-SNE clustering, this is an ideal new cluster. It should be relatively easy to define structural requirements for the cluster, and possibly even for experts to give the cluster a name. With the Esters NCC so generic, this seems like a cluster that dives deeper than the general Esters label. 

## 22: 
- 472 members, 46 uncategorized - NCC covers about 70% of chemicals, ARN around 55% 
- Almost all NCC categorizations include NO, but additionally Acute Esters and Aldehydes, as well as Epoxides are featured in significant portions. 14 total NCCs represented. 
- Primary aliphatic diamines and... and Branched/cyclic dialiphatic... are the most prominently featured ARNs, accounting for about 25% of chemicals. Cyclic ethers and Esters from non-ar... are both also prominently featured, with the remainder of chemicals scattered through at least 18 more ARNs. 
- t-SNE is moderately localized - most chemicals are loosely clustered in the same region, with a few outliers. At the center of the region, there isn't too much mixing with non-cluster chemicals. 
- There is no ToxPrint backbone, there are 69 @ 99.5%, and there is only one ToxPrint in 80% or more of chemicals: 432 - chain:alkaneCyclic_ethyl_C2_(connect_noZ)

Summary: This is a slightly strange cluster, as it appears to bridge between several difference NCCs and ARNs while also containing a few uncategorized chemicals, and despite minimal clarity from ToxPrints, the t-SNE shows that these chemicals should be strongly structurally related. This would need further investigation, perhaps into the Morgan prints since those were the original basis for the t-SNE. This is a cluster certainly worth trying to define, as it contains a significant sample size in addition to some uncategorized chemicals. 

## 23
- 24 members, 6 uncategorized - only NCC categorizes any of these chemicals
- Slightly more than 70% of the chemicals are in the Polynitroaromatics (Acute toxicity) NCC, with 25% in Esters (Acute toxicity). These are the only represented NCCs. 
- The cluster is extremely localized in the t-SNE , with all chemicals tightly grouped into two small clusters at the top right. They do appear to share space with a few chemicals not in this cluster as well. 
- There is a 7 ToxPrint backbone, 25 @ 99.5%, and 11 of these appear in more than 80% of chemicals (5 in more than 90%; 'tp_fp34', 'tp_fp36', 'tp_fp70', 'tp_fp214', 'tp_fp436'). The ToxPrint backbone:
    - 'tp_fp93', bond:CN_amine_aliphatic_generic
    - 'tp_fp97', bond:CN_amine_aromatic_generic
    - 'tp_fp195', bond:N(=O)_nitro_aromatic
    - 'tp_fp196', bond:N(=O)_nitro_C
    - 'tp_fp205', bond:N=N_azo_aromatic
    - 'tp_fp207', bond:N=N_azo_generic
    - 'tp_fp585', ring:aromatic_benzene

Summary: This is a robust cluster in terms of structural definition and t-SNE localization. It is encouraging that the NCC overlap is with a specific cluster, as that could indicate that this is essentially the extension/generalization of an existing NCC. Due to the small sample size, I believe we should avoid over-defining the structural requirements for this group: i.e., the ToxPrint backbone is more likely meaningful than the features in only 90% of the group, etc. 

## 24
- 125 members, 20 uncategorized - ARN accounts for about 70% of chemicals, NCC coverage for about 55%. 
- About 15% of chemicals are in Esters (Acute toxicity), with 23% in Esters (chronic toxicity). The rest of those categorized by NCC arescattered through 16 other NCCs, with about 40% also in NO. 
- Esters from linear saturated d... account for slightly more than 20% of ARN classifications, Esters from branched or non-ar... for about 8%, and then there are 23 additional ARNs with small representation. 
- t-SNE is extremely localized. There are two true outlier chemicals, and all others are in the same region with only slight noise or overlap with other clusters. 
- There is a 7-print ToxPrint backbone, 33 @ 99.5%, and none of those are in 80%-99% of the population. The Toxprint backbone is: 
    - 'tp_fp421', chain:alkaneBranch_isopropyl_C3
    - 'tp_fp424', chain:alkaneBranch_isohexyl_pentyl_3-methyl
    - 'tp_fp426', chain:alkaneBranch_isooctyl_hexyl_2-ethyl
    - 'tp_fp436', chain:alkaneLinear_ethyl_C2(H_gt_1)
    - 'tp_fp437', chain:alkaneLinear_ethyl_C2_(connect_noZ_CN=4)
    - 'tp_fp438', chain:alkaneLinear_propyl_C3
    - 'tp_fp439', chain:alkaneLinear_butyl_C4

Summary: This cluster shows promise with its long ToxPrint backbone and localized t-SNE. The ToxPrints in this cluster are very common in other clusters, so we should ensure that this structural definition is actually unique to this cluster before implementing it. This seems to be a cluster of Esters based on the NCC and ARN trends. Based on the ToxPrint 425 and 427 in the backbone, these are all Alkyl Esters (though none of the ToxPrints require a hydroxyl - there does not appear to be a ToxPrint for this)?

## 25
- 89 members, 23 uncategorized - ARN categorizes about 60% of chemicals and NCC 45%. 
- Most NCC classifications are Anilines (Acute toxicity), but this is only about 8%. Phenols (Acute toxicity) come in at about 6%, and the rest are scattered through 8 more categroies with minimal representation. NOs account for about 20% of chemicals. 
- chlorinated aromatic hydrocarb... account for about 20% of chemicals, with aralkylamines at about 15%, and another 12 ARNs with small representation in the cluster
-t-SNE is weakly localized. There is a small primary cluster, but there are more than 19 chemicals not in that main cluster. There does not appear to be a relationship between whether those are the categorized chemicals or not. 
- There is no ToxPrint backbone, but there are only 16 @ 99.5% and 4 of those appear in more than 80% of the cluster. These are 'tp_fp474' - chain:aromaticAlkane_Ph-C1_acyclic_connect_H_gt_1, 'tp_fp475' - chain:aromaticAlkane_Ph-C1_acyclic_connect_noDblBd, 'tp_fp476' - chain:aromaticAlkane_Ph-C1_acyclic_generic, and 'tp_fp585' -ring: aromatic_benzene

Summary: The t-SNE outliers and the fact that the rings and connectors are in most, but not all, of the chemicals begs the question of why chemicals without these features appear in the cluster. This is worth delving into further to see whether maybe some chemicals should be excluded from the cluster in order to form a structural definition, or whether there is an as-yet unseen pattern here. 

## 26
- 103 members, 25 uncategorized - ARN 55%, NCC 55%
- NOs classify 30% of NCC, Phenols (Acute toxicity) about 12%, Acute Aldehydes, Anilines, and Epoxides all around 5%. Split between 6 additional NCCs. 
- 35% of chemicals in Brominated cycloalkanes, alcoh... Next largest ARN is Isophthalates, Terephthalates... with less than 6% of chemicals and chlorinated aromatic hydrocarb.. with a similar number. Glycidly ethers and ester and aromatic ethers are also represented at around 4%. 
-t-SNE is loosely localized. Cluster is interspersed thoroughly with non-cluster chemicals in all locations, but chemicals are mostly in the same quadrant of the plot, with increased density at certain locations. Uncategorized chemicals are not in the most dense areas of this arrangement, but are also not the only outliers. 
- ToxPrint 302 is in all chemicals: bond:X[any]_halide, 31 @ 99.5%, nd 2 in more than 80% of chemicals: 'tp_fp184' - bond:CX_halide_aromatic-X_generic, 'tp_fp585' - benzene

Summary: Clearly halides are a defining feature of this cluster, though the t-SNE seems to rate it as a poor cluster. There seems to be a basis for a structural backbone for this cluster, with some decetly strong associations with particular ARN and NCCs. This cluster shows promise for adding a potential net between ARNs and NCCs for categorizing chemicals just outside their coverage. 

## 27 
- 466 members, 77 uncategorized - both about 33%, ARN only about 25%, NCC only about 20%
- Nearly 50% fall in NOs, just under 5% fall in Aldehydes (Acute toxicity) and Alkoxysilanes, rest spread very thinly through 16 other NCCs
- Spread through more than 25 ARNs, 1,2-ethanediols and their carb... and Simple Lithium Compounds each contain about 12% of chemicals, but the spread is very thin through all the different ARNs involved. 
- The t-SNE is moderately localized, with most chemicals in the same region and one particular cluster having the most density, including many of the uncategorized chemicals. However, there are many outliers and chemicals not in this region, including two distinct clusters of mostly uncategorized chemicals.
- There are no ToxPrints in every member of the sample, there are 64 @ 99.5%, and only one of these is in 80% or more of the chemicals: 'tp_fp421' - chain:alkaneBranch_isopropyl_C3

Summary: This is one of the first bad-quality but large clusters observed. There is not much basis for a structural definition, the cluster does not closely mimic any ARN or NCC to form an expansion, but there are many members and a significant number of uncategorized chemicals. It might be best to dig deeper on this cluster for more information or strutural basis, as well as whether maybe there is a more robust structural definition for the main cluster seen in the t-SNE, since that does account for most of the uncategorized chemicals. 

## 28
- 213 members, 94 uncategorized - ARN categorizes about 48% and NCC about 25%
- Even NOs only account for about 15% of chemicals, but membership is less than 5% across another 12 categories, with Anilines (Acute toxicity) in the marginal lead
- chlorinated aromatic hydrocarb... account for about 13% of chemicals, with aralkylamines around 10% and then spread through 18 other ARNs 
- t-SNE is moderate-to-strongly localized, with two main clusters in the same region, though one is almost entirely made up of the uncategorized chemicals. An investigation into what differentiates these two clusters could be informative. There are also some mini outlier clusters largely composed of these uncategorized chemicals. 
- ToxPrint 586 (Benzene) is the only ToxPrint backbone, there are 58 @ 99.5%, and none of these are in 80% or more of the chemicals. 

Summary: This cluster is clearly filling gaps left by ARN and NCC, but the meaning is quite deeply buried, since ToxPrint 586 is a very common one. Splitting the two main clusters of the t-SNE apart and looking for the structural differentiation between them might be one approach for deepening the structural justification.

**This is where the Neutral Organics Error was fixed**

## 29
- 118 members, 4 uncategorized - ARN accounts for about 75%, NCC for about 20%
- Only Boron compounds, Alkoxysilanes (12%), Anionic Surfactants, and NOs are featured. 
- 70% of chemicals are in primary aliphatic diamines and... , with only 4 other ARNs represented with minimal coverage
- t-SNE is moderately-to-strongly localized, with most members clustered together in the same area, though by appearance forming the borders of other visual t-SNE clusters. Outliers are rare, though 3/4 the uncategorized chemicals are in these outliers. 
- There is a single-ToxPrint backbone of 'tp_fp93' - bond:CN_amine_aliphatic_generic. This appears in multiple previously-seen clusters, so it is not unique enough on its own to define a cluster. There are 27 @ 99.5% and 3 of these are present in 80% or more of the cluster: 'tp_fp99' - bond:CN_amine_pri-NH2_alkyl, 'tp_fp101' - bond:CN_amine_pri-NH2_generic, 'tp_fp436' - chain:alkaneLinear_ethyl_C2(H_gt_1)

Summary: This cluster mostly seems to build off of the existing ARN, so investigating whether there is a reasonable definition for the structure of that ARN may also lead to a meaningful structural definition of this cluster. Detracting from the potential meaningfulness of this cluster, there are very few uncategorized chemicals and those that are uncategorized are in outlier areas of the t-SNE. An investigation of how these chemicals got assigned to this cluster may be informative, particularly since there are so few of them. 

## 30
- 664 members, 198 uncategorized - ARN categorizes about 50%, NCC about 30%
- Almost all NCCs are in Anilines or Aldehydes, both Acute toxicity, but they are also spread across 13 NCCs
- About 25% in chlorinated aromatic hydrocarbons ARN with 13 more ARNs under 5% representation
- t-SNE is moderately localized. All chemicals are in the same general are, but with a lot of mix with out-of-cluster chemicals. There are some scattered, more distant chemicals and many of the uncategorized chemicals seem to be clustered in the same general region. 
- There is no ToxPrint backbone, 125 @ 99.5% and 0 ToxPrints in 80% or more of the chemicals. 

Summary: This is a critical cluster due to its size and number of uncategorized chemicals. However, there is a lack of a basic structural definition or even the ghost of one based on the ToxPrint process I've use so far. It would take additional delving here to get at one. The strongest NCC and ARN overlaps could potentially be used to get at this: what do Anilines, Aldehydes, and chlorinated aromatic hyrdrocarbons have in common, if anything? The t-SNE region covered is quite wide, so the definition for this cluster may end up having to be relatively broad, as I suspect will be the case for some of the very large clusters. 

## 31
- 209 members, 5 uncategorized - both cover 80% of chemicals, with ARN around 10% more and NCC around 5% more
- 85% in Esters (Acute toxicity), 75% in NO, and the rest marginally spread across 10 other NCCs
- 60 % Esters from branched or non-aro..., 20% alpha-chloro aliphatic carboxy..., and the rest spread through 9 or more ARNs at low frequency
- Strongly localized t-SNE with a very distinct, dense cluster. There are a scattering of outliers. 
- No ToxPrint backbone, 46 @ 99.5%, and 2 are in 80% or more of the chemicals: 'tp_fp70' - bond:C=O_carbonyl_generic, 'tp_fp436' - chain:alkaneLinear_ethyl_C2(H_gt_1)

Summary: This is another cluster tightly tied to the Esters title, though without the strength of the backbone in cluster 24. It should likely be contrasted with any other Ester clusters in order to determine what differentiates this one, as its actual structural core seems to be relatively weak here. There are not very many uncategorized chemicals in the cluster, which suggests that the cluster might be best defined by just slightly expanding the definition of an existing ARN or NCC. Looking at how the 5 missing chemicals fall outside of the Esters ARNs and NCCs may provide an answer to this. 

## 32
- 337 members, 59 uncategorized - 65% by ARN only, 5% by NCC only
- Anionic Surfactants and Aldehydes (Acute toxicity) each account for about 5% of chemicals. NOs apply to about 55% of chemicals. 
- Polyol amines account for about 22% of chemicals, 1,2-ethanediols and their carb... account for another 20%, and the rest is distributed across about 15 other ARNs. 
- t-SNE is weakly localized. There are 5 or 6 distinct clusters containing concentrated sets of this cluster, but plenty of chemicals from the cluster aren't in these main clusters either. The uncategorized chemicals are spread all about through the cluster regions, but there is still an overall sense of the cluster having main regions. 
- There is no ToxPrint backbone, there are 85 @ 99.5% and 3 of those are present in more than 80% of the chemicals: 'tp_fp117'-bond:COH_alcohol_aliphatic_generic, 'tp_fp128'-bond:COH_alcohol_generic, 'tp_fp129'-bond:COH_alcohol_pri-alkyl

Summary: The ToxPrints appearing highly frequently in this cluster are rarer than many others, and could potentially form a good structural basis for the cluster. Looking at these and maybe other common ToxPrints with some kind of logic tree (has either __ or __) could potentially help derive a structural definition for the cluster. The cluster contains many uncategorized members and many members overall, so determining a definition is important. The two primary ARNs are the most likely to privide insight into what such a definition should look like. 

## 33
- 19 members, 8 uncategorized - all categorized chemicals are covered by NCC, just over 50% are also covered by ARN
- 37% of chemicals are in Acrylates/Methacrylates and Esters (Chronic toxicity), but 16% are in the Acute toxicity versions of both of these as well. 5% are in Alkoxysilanes
- All ARN categorizations are in acrylate and methacrylate amines
- t-SNE is extremely localized, all 19 chemicals are in a tiny, tight cluster. 
- There is a 19-ToxPrint backbone, 29 @ 99.5%, and :
    - 'tp_fp146', bond:CX_halide_alkyl-F_perfluoro_butyl
    - 'tp_fp147', bond:CX_halide_alkyl-F_perfluoro_ethyl
    - 'tp_fp150', bond:CX_halide_alkyl-F_tetrafluoro_(1_1_1_2-)
    - 'tp_fp151', bond:CX_halide_alkyl-F_trifluoro_(1_1_1-)
    - 'tp_fp158', bond:CX_halide_alkyl-X_dihalo_(1_1-)
    - 'tp_fp159', bond:CX_halide_alkyl-X_dihalo_(1_2-)
    - 'tp_fp160', bond:CX_halide_alkyl-X_dihalo_(1_3)
    - 'tp_fp163', bond:CX_halide_alkyl-X_generic
    - 'tp_fp167', bond:CX_halide_alkyl-X_tetrahalo_(1_1_2_2-)
    - 'tp_fp168', bond:CX_halide_alkyl-X_trihalo_(1_1_1-)
    - 'tp_fp169', bond:CX_halide_alkyl-X_trihalo_(1_1_2-)
    - 'tp_fp170', bond:CX_halide_alkyl-X_trihalo_(1_2_3-)
    - 'tp_fp191', bond:CX_halide_generic-X_dihalo_(1_2-)
    - 'tp_fp272', bond:S(=O)N_sulfonamide
    - 'tp_fp273', bond:S(=O)N_sulfonylamide
    - 'tp_fp292', bond:S=O_sulfonyl_generic
    - 'tp_fp295', bond:S~N_generic
    - 'tp_fp301', bond:X[any]_halide
    - 'tp_fp436', chain:alkaneLinear_ethyl_C2(H_gt_1)

Summary: This appears to be a specific subset of Acrylates/Methacrylates with a robust and easy structural definition based on the lengthy ToxPrint backbone. This cluster is probably ready to be defined as-is, though paring the ToxPrint backbone might also make it slightly more genralizable. Many of the ToxPrints in the backbone have not been seen in any of the previous clusters either, so they may not even all be needed to isolate this cluster.  

## 34
- 556 members, 144 uncategorized - 50% categorized by ARN only, just under 25% categorized by NCC with 8% categorized by both. 
- Almost all NCC categorizations are in Alkoxysilanes but with scattered small representation for 13 other NCCs and 32% in NOs
- ARN categorization is extremely varied. Simple Lithium compounds are the most common, but with only about 8% of chemicals and more than 20 other ARNs represented as well. 
- t-SNE is moderate-to-weakly localized. There is a region that the cluster is mostly homed in, but with little density and spread to other regions. The uncategorized chemicals do appear to form a few specific clusters with one another, some in the primary region and others as more outlier clusters. 
- There is no ToxPrint backbone, 95 @ 99.5%, and the only ToxPrint in 80% or more of the set is 'tp_fp436' - chain:alkaneLinear_ethyl_C2(H_gt_1), which is extremely common. 

Summary: The basic version of the structural definition for this cluster is insufficient, between the lack of backbone and extremely common high-frequency ToxPrint. Such a significant portion of the cluster is uncategorized that this does not seem to be a natural extension of an existing NCC or ARN. A deeper dive into a potential structural or physicochemical explanation for this cluster would absolutely be necessary to give it definition. The cluster is certainly worth working to flesh out, based on its large size and large number of uncategorized chemicals. 

## 35
- 189 members, 76 uncategorized - 25% categorized by ARN and 45% categorized by NCC
- 15 NCCs are represented but NOs is *not*. Anilines (Acute toxicity) was about 15%, Polynitroaromatics (Acute toxicity) around 12%, and Phenols (Acute toxicity) about 10%
- Only 8 ARNs are represented, but nitroalkanes are the most common with only about 9%. 
- t-SNE is very localized. With very few exceptions, the chemicals all fall in the same, dense region. The uncategorized chemicals form a distinct cluster within this regional cluster as well. This could indicate that exploring whether the uncategorized chemicals have a specific structural backbone of their own could be of interest. 
- There is a 2-ToxPrint backbone: 'tp_fp195'-bond:N(=O)_nitro_aromatic, 'tp_fp196'-bond:N(=O)_nitro_C. There are 48 @ 99.5% and the only print in more than 80% of chemicals is 586, the Benzene ring ToxPrint. *bears similarity to clusters 4 and 21

Summary: This is an interesting cluster with some basis for a structural definition, though effort should be made to find the distinction between cluster 4 and this cluster. This seems to bridge a gap between different ARNs and NCCs rather than being an extension of any individual category. The cluster is decently-sized, with a significant portion of uncategorized chemicals, and the localization of the uncategorized chemicals on the t-SNE forms another definite point of interest. 

## 36
- 168 members, 7 uncategorized - ARN categorizes about 90% and NCC 85%
- 75% Esters (Acute toxicity), 73% NOs, spread among 14 more categories all under 5%
- Esters from linear saturate d... and Esters from branched or non-aro... account for 33% and 22%, repectively alpha-chloro aliphatic carboxy... is also featured prominently, with smaller representation for 12 other ARNs. 
- t-SNE is moderately localized, with a cluster containing most of the chemicals but the cluster is fairly loose with many outliers and a decent amount of noise/interspresion with non-cluster chemicals. The core of the cluster does appear to be mostly separate from outside chemicals. 
- The ToxPrint backbone is just 'tp_fp436' - chain:alkaneLinear_ethyl_C2(H_gt_1), with 24 @ 99.5% and of those, 4 are in 80% or more of the chemicals: 'tp_fp70' - bond:C=O_carbonyl_generic, 'tp_fp437'-chain:alkaneLinear_ethyl_C2_(connect_noZ_CN=4), 'tp_fp438'-chain:alkaneLinear_propyl_C3, 'tp_fp439'-chain:alkaneLinear_butyl_C4. 

Summary: This cluster has decent membership and matches well with ARN and NCC esters mostly, so it could potentially be yet another expansion of the category Esters. However, this cluster has no unique defining features observed yet, as its main ToxPrints are extremely common in similar clusters already seen, and in most clusters seen already in general. It would take further investigation to determine whether this cluster actually adds any interesting information or has any unique structural features, or whether it is just the result of the KMeans algorithm trying to chop up a large block of Esters and ester-like compounds. 

## 37*
- 34 members, 14 uncategorized - 50%, 33% ARN
- About 23% Anilines (Acute toxicity), about 10% Phenols, and some Diazoniums and Esters (both acute), and Vinyl Sulfones
- Almost all ARN clssifications are Benzoates, with 2 chemicals sorted into other categories. Almost 50% of chemicals are out of domain for the ARN model. 
- Localization for this group is difficult to classify due to small cluster size. Members form about 4 clusters with one or two lone chemicals. The clusters are tight, but they are also very small and contained in larger clusters of non-members. 
- There is a 6-member ToxPrint backbone, 37 @ 99.5%, and only one of those is in more than 80% of the chemicals, ToxPrint 587 - ring:aromatic_biphenyl. The ToxPrint backbone is:
    - 'tp_fp34', bond:C(=O)N_carboxamide_(NHR)
    - 'tp_fp36', bond:C(=O)N_carboxamide_generic
    - 'tp_fp70', bond:C=O_carbonyl_generic
    - 'tp_fp214', bond:NC=O_aminocarbonyl_generic
    - 'tp_fp476', chain:aromaticAlkane_Ph-C1_acyclic_generic
    - 'tp_fp585', ring:aromatic_benzene

Summary: This cluster is small with a simple, but interesting and unique (so far), ToxPrint backbone and a large proportion of uncatgeorized chemicals outside the domain of existing ARNs. It seems this cluster should be easy to derive a strong definition for and could definitely add to coverage for existing chemical groups. There seems to be some overlap with NCCs and Benzoates, but the cluster could certainly be introducing a new category which overlaps with those others, and is not too strongly overlapped with either the Benzoates ARN or the Anilines NCC.  

## 38*
- 48 members, 33 uncategorized - NCC categorizes just over 25%, ARN only about 12%
- Almost all NCCs are Dichlorobenzidine-based Pigments, with a few Esters (Acute toxicity)
- Isophthalates, Teraphthalates is the only ARN with more than one member, representing about 8% of chemicals. 75% of the cluster is out of the ARN domain. 
- t-SNE is very strongly localized. The entire cluster forms one small visual cluster with no outliers. There are signs of outsider chemicals located very close to cluster members, though. 
- There is a 14-print ToxPrint backbone with 32 @ 99.5% and none of those present in more than 80% of the population:
    - 'tp_fp34', bond:C(=O)N_carboxamide_(NHR)
    - 'tp_fp36', bond:C(=O)N_carboxamide_generic
    - 'tp_fp70', bond:C=O_carbonyl_generic
    - 'tp_fp73', bond:CC(=O)C_ketone_aliphatic_acyclic
    - 'tp_fp74', bond:CC(=O)C_ketone_aliphatic_generic
    - 'tp_fp86', bond:CC(=O)C_ketone_generic
    - 'tp_fp87', bond:CC(=O)C_ketone_methyl_aliphatic
    - 'tp_fp204', bond:N=N_azo_aliphatic_acyclic
    - 'tp_fp205', bond:N=N_azo_aromatic
    - 'tp_fp207', bond:N=N_azo_generic
    - 'tp_fp214', bond:NC=O_aminocarbonyl_generic
    - 'tp_fp516', group:aminoAcid_aminoAcid_generic
    - 'tp_fp566', group:ligand_path_5_bidentate_aminopropanal
    - 'tp_fp585', ring:aromatic_benzene

Summary: This is a small cluster of almost entirely newly categorized chemicals with a robust potential for a ToxPrint backbone, and powerful localization on t-SNE. Although currently not containing many members, this is a great candidate for a category supplementing the existing ARNs and NCCs. 

## 39
- 151 members, 11 uncategorized - ARN categorizes about 80% of chemicals, NCC about 30%
- All NCC categorizations include NO, 13 total NCCs represented but mostly in small percentages, Anionic Surfactans and Nonionic Surfactants each represent about 10% of the set.
- 19 ARNs are represented, with Organic phosphonic acids, salt... representing about 26% of chemicals, Ethoxylated \<C6 \> alcohols... representing about 20%, and all other catgeories representing less than 5%
- t-SNE is moderately localized; there are three main clusters with a few outliers. The 3 clusters are not very dense and 2/3 are close to or connected to other visual clusters. It's possible these correspond closely to the ARN categorization trends already seen for this set. 
- There is a 4 print ToxPrint backbone of very common ToxPrints, with 41 @ 99.5% and 2 of those present in 80% or more of chemicals, also very common ToxPrints. Those two are included as the last in this list, since they are very similar to those in the backbone: 
    - 'tp_fp436', chain:alkaneLinear_ethyl_C2(H_gt_1)
    - 'tp_fp437', chain:alkaneLinear_ethyl_C2_(connect_noZ_CN=4)
    - 'tp_fp438', chain:alkaneLinear_propyl_C3
    - 'tp_fp439', chain:alkaneLinear_butyl_C4
    - 'tp_fp440', chain:alkaneLinear_hexyl_C6
    - 'tp_fp441', chain:alkaneLinear_octyl_C8

Summary: This cluster would require further investigation to establish a meaningful structural definition, as these ToxPrints are also common to multiple other clusters already and there are no features seen in this analysis to differentiate this cluster from others. The NCC overlaps do appear to be relatively new, especially the nonionic surfactants, so these might suggest an approach to the cluster. The multi-cluster t-SNE suggests to me that with Morgan fingerprints and Jaccard metric, this cluster might more reasonably be split into three smaller clusters. There are not very many uncategorized chemicals in the cluster either, so it does not appear to be of critical interest. 

## 40 
- 499 members, 127 uncategorized - 60% categorized by ARN and 12% by NCC
- About 20% of chemicals are NOs, no other NCC appears in more than 5% of chemicals and 17 NCCs are represented
- aralkylamines and chlorinated aromatic hydrocarbons... each represent about 15% of chemicals, with hydrocarbyl siloxanes at about 8% and at least 17 ARNs with smaller representations
- t-SNE is weakly localized. There are about 11 sub-clusters visually, and while some are located near one another, others are not in the same area. This could indicate that while some of the chemicals are closely related to one another, there will not be many global trends for chemicals in the cluster. 
- There is no ToxPrint backbone, there are 90 @ 99.5%, and only two are present in 80% or more of chemicals: 'tp_fp585'- ring:aromatic_benzene, 'tp_fp587' - ring:aromatic_phenyl. 

Summary: This cluster does not yet have any structural definition. It is a very large category with a significant portion of uncategorized chemicals meaning that it is important, but the t-SNE, NCC, and ARN information that we already have does not aid strongly in a definition. Considerable additional investigation into this cluster would likely be necessary to use it in any meaningful way. 

## 41*
- 163 members, 39 uncategorized - NCC ~ 60%, ARN ~30%
- 45% of chemicals are Phenols (Acute toxicity), 12% are in Phenols (Chronic toxicity) and similar numbers in NOs, 15 NCCs are featured, including Benzotriazole-hindered phenols
- Only about 10% of chemicals are considered out of the ARN domain, but most are in miscellaneous chemistry. Bisphenol A (BPA) derivatives are about 8% of chemicals with the largest representation, and all other ARNs have fewer than 5% of chemicals. 
- The t-SNE is strongly localized, with one main cluster and only a few outliers, all in the same general region. There is evidence of non-member chemicals close to the main cluster, but overall it is dense and strongly isolated from most other visual clusters. 
- There is a 5-print ToxPrint backbone, 48 @ 99.5%, and only 1 of those is in 80% or more of the population, Toxprint 423 - chain:alkaneBranch_t-butyl_C4. ToxPrint backbone:
    - 'tp_fp423', chain:alkaneBranch_neopentyl_C5
    - 'tp_fp437', chain:alkaneLinear_ethyl_C2_(connect_noZ_CN=4)
    - 'tp_fp475', chain:aromaticAlkane_Ph-C1_acyclic_connect_noDblBd
    - 'tp_fp476', chain:aromaticAlkane_Ph-C1_acyclic_generic
    - 'tp_fp585', ring:aromatic_benzene

Summary: This is a significantly sized cluster with many newly classed chemicals, and the ToxPrint backbone seems to be distinct from those seen previously. There are strong associations with preexisting NCCs (Phenols), so it might be worth exploring whether this could be an extension of that catgeory, though the phenols do not cover every chemical in the category, or even all of the categorized chemicals. The t-SNE supports that this is a robustly defined cluster, and it could likely be moved forward easily pending review of the ToxPrint backbone by an expert. 

## 42
- 284 members, 23 uncategorized - NCC categorizes 95%, ARN about 25%
- 87% of chemicals are Phenols (Acute toxicity), with 8 more ARNs at fewer than 10% of chemicals
- chlorinated aromatic hydrocarbons are about 8% of chemicals, with more than 14 more ARNs represented minimally. About half of chemicals are in miscellaneous chemistry, with just under 25% out of the ARN domain. 
- the t-SNE is very weakly localized. The chemicals are in the same half of the t-SNE, but are extremely widely and loosely spread on that half. 
- ToxPrint 129 - bond:COH_alcohol_generic is the only fully common ToxPrint. There are 74 at 99.5% and 3 in more than 80 % of chemicals: 'tp_fp122' - bond:COH_alcohol_aromatic, 'tp_fp123' - bond:COH_alcohol_aromatic_phenol, 'tp_fp585' - ring:aromatic_benzene. 

Summary: This is a cluster that agrees strongly with existing NCCs but poorly with the t-SNE. This could be a good example of where the Euclidean/KMeans definition matches NCCs better than the Spectral Clusters that were also experimented with, and which share the Jaccard metric with the t-SNE. This is most likely a generalization of the Phenols category, in which case a structural definition should potentially be possible. 

## 43
- 102 members, 6 uncategorized - ARN categorizes 92%, NCC 58%
- Nearly all, if not all NCC categorizations are into one of the Esters categories as well as NOs, with Esters (Chronic toxicity) representing about 40% of chemicals. 4 more NCCs are represented barely. 
- 2 chemicals are sorted into other ARNs, while all of the rest are in Esters from linear saturated d... A small number of chemicals are considered out of the ARN domain. 
- The t-SNE shows moderate-to-strong localization, with all chemicals in a single, loose cluster. The cluster of chemicals in this KMeans group forms the edges of other t-SNE visual clusters, rather than being spatially separated from outside chemicals - thus, there are closely related chemicals that are not in this cluster. 
- There is a 5 ToxPrint backbone of very common ToxPrints, 42 @ 99.5%, and 5 of those in 80% or more of the population. Those five are: 'tp_fp45' - bond:C(=O)O_carboxylicEster_acyclic, 'tp_fp46' - bond:C(=O)O_carboxylicEster_aliphatic, 'tp_fp48' - bond:C(=O)O_carboxylicEster_alkyl, 'tp_fp440' - chain:alkaneLinear_hexyl_C6, 'tp_fp441' - chain:alkaneLinear_octyl_C8. The ToxPrint backbone is:
    - 'tp_fp436', chain:alkaneLinear_ethyl_C2(H_gt_1)
    - 'tp_fp437', chain:alkaneLinear_ethyl_C2_(connect_noZ_CN=4)
    - 'tp_fp438', chain:alkaneLinear_propyl_C3
    - 'tp_fp439', chain:alkaneLinear_butyl_C4
    - 'tp_fp70', bond:C=O_carbonyl_generic

Summary: This category appears to be a clear extension of the NCCs and ARNs for Esters. The 6 chemicals that are not categorized by the existing methods should be examined to see how they relate to Esters. The ToxPrint backbone is not enough to explain what differentiates this cluster from other major Ester clusters, so that will also require additional analysis, potentially hingeing on the very common but not ubiquitous ToxPrints. 

## 44 
- 188 chemicals, 1 uncategorized - About 48 % NCC and 97% ARN
- Similar to cluster 43, approximately all NCCs are in Esters and NOs with Chronic toxicity dominant at about 30%. 8 additional NCCs with minor representation. 
- All meaningful ARNs are Esters from linear saturated d..., about 3% are miscellaneous chemistry, and less than 1% are out of domain. 
- t-SNE is strongly localized, just to the right of cluster 43. This cluster is more tightly grouped than 43. The center is isolated from outside chemicals, but the edges contain chemicals from other clusters. 
- The 9 - ToxPrint backbone has significant overlap with cluster 43. There are 45 @ 99.5% and there is only 1 in more than 80% of the population - ToxPrint 442 - chain:alkaneLinear_octyl_C8. 
    - 'tp_fp45', bond:C(=O)O_carboxylicEster_acyclic
    - 'tp_fp46', bond:C(=O)O_carboxylicEster_aliphatic
    - 'tp_fp48', bond:C(=O)O_carboxylicEster_alkyl
    - 'tp_fp70', bond:C=O_carbonyl_generic
    - 'tp_fp436', chain:alkaneLinear_ethyl_C2(H_gt_1)
    - 'tp_fp437', chain:alkaneLinear_ethyl_C2_(connect_noZ_CN=4)
    - 'tp_fp438', chain:alkaneLinear_propyl_C3
    - 'tp_fp439', chain:alkaneLinear_butyl_C4
    - 'tp_fp440', chain:alkaneLinear_hexyl_C6

Summary: The notes for this cluster are extremely similar to those for cluster 43 because they are very similar clusters from all steps in this analysis. A contrast analysis between them might help illuminate what makes each cluster distinct, not only from one another, but also from the rest of the data. This particular cluster does not contain many uncategorized chemicals, so it may be of lesser importance in extending the NCC/ARN landscape. 

## 45
- 168 members, 7 uncategorized - both ARN and NCC cover about 80% of the set
- Although 15 other NCCs are mildly represented, Esters (Acute toxicity) account for more than 75% of the chemicals. Most chemicals are also in NOs. 
- On the other hand, ARN categorization is much less uniform. 25% in Alpha-chloro aliphatic carboxy..., 20% in Esters from branched or non-... and 15% in Esters from linear saturated d... with 9 other ARNs represented in smaller proportions. 
- The t-SNE is weakly localized, with a hint of a cluster near the left center of the plot but plenty of outliers, noise, and scatter around. 
- There is no ToxPrint backbone, 29 @ 99.5%, and only ToxPrint 71 - bond:C=O_carbonyl_generic in 80% of the population. 

Summary: This is a challenging cluster. It appears that the cluster must mostly contain Esters. An examination of the Acute toxicity Ester NCC rules might help create a structural definition for the cluster, as ToxPrints and t-SNE are currently not providing much assistance. 

## 46*
- 36 members, 32 uncategorized  - ARN for maybe 2% and NCC 3%
- Only the two Ester NCCs are represented
- 2 Chemicals are sorted meaningfully by ARN (ortho-phthalates and chlorinated aromatic hydrocarb...), and 3 are in miscellaneous chemistry
- The t-SNE is very strongly localized, but it's easy for this to be true due to the small cluster size. There are other chemicals tightly paired with the cluster on the t-SNE. 
- There is a 9 ToxPrint backbone, 29 @ 99.5%, and 3 of those in more than 80% of the population: 'tp_fp34'- bond:C(=O)N_carboxamide_(NHR), 'tp_fp36'- bond:C(=O)N_carboxamide_generic, 'tp_fp214' - bond:NC=O_aminocarbonyl_generic. The backbone is:
    - 'tp_fp70', bond:C=O_carbonyl_generic
    - 'tp_fp122', bond:COH_alcohol_aromatic
    - 'tp_fp123', bond:COH_alcohol_aromatic_phenol
    - 'tp_fp128', bond:COH_alcohol_generic
    - 'tp_fp205', bond:N=N_azo_aromatic
    - 'tp_fp207', bond:N=N_azo_generic
    - 'tp_fp476', chain:aromaticAlkane_Ph-C1_acyclic_generic
    - 'tp_fp585', ring:aromatic_benzene
    - 'tp_fp591', ring:fused_[6_6]_naphthalene

Summary: This is a small cluster of almost entirely previously uncategorized chemicals. It has an unusual and thorough ToxPrint backbone. After review by an expert, this could be a great addition for expanding NCC and ARN coverage. It is worth considering whether the category might be generalized a little by determining whether all the ToxPrints are necessary or not. 

## 47*
- 42 members, 27 uncategorized - about 25% by NCC and 8% by ARN
- All NCCs are in Cationic (quaternary ammonium) surfactants, a couple also in Esters (Chronic toxicity). No other NCC representation. 
- All chemicals are within the ARN domain, but very few are outside of miscellaneous chemistry about 6% Acyl derivatives from alpha-am... and 2% from Linear aliphatic ketones
- The t-SNE has strong localization, but again, this is common for tiny clusters. All chemicals are in a tight cluster, but they lie on a cluster that includes many outsider chemicals that are also tightly packed
- There is a 10-ToxPrint backbone and 38 @ 99.5% with none in 80% or more of the chemicals:
    - 'tp_fp34', bond:C(=O)N_carboxamide_(NHR)
    - 'tp_fp36', bond:C(=O)N_carboxamide_generic
    - 'tp_fp70', bond:C=O_carbonyl_generic
    - 'tp_fp214', bond:NC=O_aminocarbonyl_generic
    - 'tp_fp436', chain:alkaneLinear_ethyl_C2(H_gt_1)
    - 'tp_fp437', chain:alkaneLinear_ethyl_C2_(connect_noZ_CN=4)
    - 'tp_fp438', chain:alkaneLinear_propyl_C3
    - 'tp_fp439', chain:alkaneLinear_butyl_C4
    - 'tp_fp440', chain:alkaneLinear_hexyl_C6
    - 'tp_fp441', chain:alkaneLinear_octyl_C8
 
 Summary: This is another cluster with very strong potential for extending the NCCs and ARNs. There is a ToxPrint backbone with some very common ToxPrints and others that seem likely to be enough to differentiate this category. The t-SNE and the overlap with a small NCC category also show promise. 

 ## 48 
 - 99 chemicals, 7 uncategorized - 85% by ARN and 30% NCC
 - 10 NCCs are represented, with about 20% in Esters (Acute toxicity) and 18% in NOs. The rest make up less than 10% of the chemicals each. 
 - 17 ARNs with less than 8% representation, but about 33% are in aromatic ethers
 - t-SNE is moderately localized. There are two clusters that are relatively dense but separated from one another, and about a dozen outlier chemicals. 
 - 586 - ring:aromatic_benzene is the only ToxPrint in all members. There are only 17 @ 99.5% and ring:aromatic_biphenyl is in more than 80% of the chemicals. 

 Summary: This cluster does not have an easy, distinct structural backbone based on the preliminary analysis. The wide spread of associated NCCs and ARNs shows that this is likely a bridging category between multiple categories, especially since the NCC spread is so wide. 

 ## 49
 - 501 members, 107 encategorized - 55% by ARN and 25% by NCC
 - Imides and Anhydrides, carboxylic acid have the most representation but under 10%. NOs account for about 50% of chemicals. 
 - 45% of the chemicals are out of the ARN domain while 33% are in Unsubstituted and linear aliph... 12 other ARNs have minor representation in the cluster
 - The t-SNE is moderately-to-strongly localized. Almost all chemicals share one large, but decently loose cluster. There are few outliers, especially considering the large size of the cluster. The uncategorized chemicals show indication of being clustered within the cluster. 
 - There is no ToxPrint backbone, 115 @ 99.5%, and only 1 in more than 80% of the chemicals: 71 - bond:C=O_carbonyl_generic.

 Summary: This could be a phenomenal cluster for expanding the existing NCCs and ARNs, based on size, number of newly classified chemicals, and t-SNE agreement. However, the ToxPrint analysis is not showing promise yet for generating a structural definition. Further investigation into ToxPrint and Morgan fingerprint trends would be needed to finish defining this cluster. The main ARN category might help with this investigation. 

 ## 50
 - 52 members, 18 uncategorized - 25% NCC, 40% ARN
 - Acute toxicity Anilines and Phenols both have just over 10% representation, with 4 other NCCs represented in small proportions. 
 - 33% of chemicals are in miscellaneous chemistry and about 28% are in arlakylamines. 4 more ARNs have mild representation. 
 - t-SNE is moderately localized given the size of the cluster. There is a main cluster that is small, but it forms the border of a larger cluster and there are many outliers. 
 - ToxPrint  - ring:aromatic_benzene is the only one common to all members, which is not an unusual print for isolating the cluster from others. There are only 24 at 99.5% and 'tp_fp97'- bond:CN_amine_aromatic_generic, 'tp_fp103' - bond:CN_amine_sec-NH_aromatic, 'tp_fp105' - bond:CN_amine_sec-NH_generic, 'tp_fp587' - ring:aromatic_phenyl are in more than 80% of compounds. 

 Summary: This cluster is not strongly grounded in the ARNs and NCCs, so it might form a bridge in the coverage gaps of the two. However, the cluster has relatively few members, making trends more difficult to trust. The current ToxPrint backbone is not sufficient to differentiate the cluster, but the common ToxPrints have not been seen as commonly in other clusters and might help form a structural definition. The large proportion of chemicals in miscellaneous chemistry suggests that these are primarily chemicals that were just underrepresented in the original ARN study, so finding more members of this cluster might help flesh out a robust definition. 
 