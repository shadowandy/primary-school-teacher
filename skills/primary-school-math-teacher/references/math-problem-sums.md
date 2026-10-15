# Mathematics — problem sums

**This is not MOE syllabus.** It is an account of how Singapore problem sums are taught in the classroom, so it carries no authority over what a level covers. The syllabus names Pólya's four steps and "the use of heuristics" and stops there; this file is the classroom layer underneath that — the named concepts a Singapore child is actually taught to recognise, and the method for each. Treat the concept names and methods as classroom practice, and `math.md` as the authority on what is in a level and what is out.

A child who is weak at problem sums usually understands the chapter fine. What they lack is the skill of comprehending the question, linking it to the right concept, and applying that concept correctly — which is why the same child scores Paper 1 and crashes Paper 2. That skill is trainable, and this file is what to train.

## K-C-A

Three steps, in order, on every problem sum.

**Keywords.** Pull out the phrases that carry the structure, and every number — all given numbers matter. The recurring ones: *more than*, *less than*, *twice the*, *equals to*, *at first*, *in the end*, *of the remainder*, *has X times more*, *has X times less*. Then check the child can say what each one means, which is the [guiding question](#guiding-questions) layer.

Most children understand the words and still cannot write the maths, so the keyword step is not finished until the phrase has become an expression. Drill the translation itself:

| Phrase | Written as |
|---|---|
| A has 20% more than B | A = 120% of B, so B = 100u and A = 120u |
| A has 1/5 as many as B | A = 1u, B = 5u |
| A has 1/3 of B | A = 1u, B = 3u |

**Concept.** Link the keywords to one named concept below. A keyword maps to a concept, not to a chapter:

| Cue in the question | Concept |
|---|---|
| "of the remainder" | [Remainder (branching)](#remainder-branching) |
| a fraction of one quantity *equals* a fraction of another | [Equal fractions](#equal-fractions) |
| "more than" / "less than" in a fractions question, or a before-and-after scenario | [Model drawing](#model-drawing) |
| one part unchanged, the other spent or added to | [Constant part](#constant-part) |
| internal transfer — A gives to B | [Constant total](#constant-total) |
| ages, "in N years' time" | [Constant difference](#constant-difference) |
| both parts change, by different amounts | [Everything changed](#everything-changed) |
| two packing or buying conditions, one leaving extra and one short | [Excess and shortage](#excess-and-shortage) |
| two rates of spending, compared at a later moment | [Difference](#difference) |
| equal numbers of two items, or a fixed bundle | [Grouping](#grouping) |
| coins, notes, or price per unit | [Number × Value](#number--value) |
| two item types, a known total count and a known total value | [Guess and check / assumption](#guess-and-check--assumption) |
| two people each spending a different fraction of their own amount | [Units and parts](#units-and-parts) |
| "in the end" + "find the number at first" | [Working backwards](#working-backwards) |
| two hypothetical conditions, both counterfactual | [Double if](#double-if) |

Linking reliably needs the child to understand *why* the concept holds, not just the mapping. Internal transfer is the one to demonstrate physically: hand the child some erasers, count both piles, pass some across, count again. The total is unchanged — and the child has seen why.

**Apply.** Run the concept's method, then check the answer against the question. The most common waste is working correctly all the way to 1 unit and handing in 1 unit when the question asked for something else. Three applications carry most of the failures and are worth drilling on their own: knowing when to multiply and when to divide the fractions in branching, making the *numerators* equal in equal fractions, and cross multiplying in units and parts.

Where two methods both work, the faster one is still worth teaching — assumption beats tabulated guess and check, and at P6 algebra often beats a model.

## Guiding questions

When a child asks for help, answer with a question that carries a clue, not with the solution. The clue is what separates a guiding question from a blank stare.

- *Reading it*: What do you understand from this sentence? What are the keywords? What is the question asking for?
- *Solving it*: How should you represent this — model, or ratio? What method will you use? Why that way?
- *After*: How do you check your answer? Can you solve it another way? What other question types would this method work on?

The answers also tell you whether the child knows or is performing knowing.

## Practice discipline

Less is more. Fewer questions, each fully understood, beats a past paper skimmed against a thin answer key — which teaches copying.

- Have the child write the **concept** beside each question, not the chapter. "Equal fractions concept", never "Fractions".
- Have them write the reason for each step. Slower, and it is what prevents the careless slips.
- Mark, then collect the concepts they were weak in, and pull more questions on *those* concepts — from other papers, or by changing the numbers in the same question. Repeat until they can solve it unaided.

Thirty minutes on one question fully understood beats thirty minutes on ten skimmed.

Three moves shape the set of questions itself:

- **Order it by increasing difficulty.** Confidence comes from clearing the easy ones first; a set that opens hard teaches the child that the concept is beyond them.
- **Fade the help.** Walk the first few questions through aloud, then hand over more of each solution, until the child is working unaided. Reduce the support deliberately rather than all at once.
- **Show a wrong solution and ask the child to find the error.** Spotting someone else's slip is how a child learns to see their own.

## Pitch

`math.md` governs what a level covers; these are the boundaries this file runs into most.

- **Model drawing carries P1-P5.** Letters for unknowns are P6. At P6, algebra is often the faster route, but the syllabus allows only simple linear expressions, whole-number coefficients, no brackets — so a method that cross-multiplies a bracket (as [Everything changed](#everything-changed) and [Double if](#double-if) do) stays in **units**, where it is unit arithmetic rather than algebra.
- **Ratio is Standard P6 only.** Every ratio-based concept here — constant part, constant total, constant difference, everything changed, double if — is out of reach at Foundation P6, which has no ratio and no algebra. Set those at Standard P6, or recast them as models.
- **Branching needs fraction × fraction**, which is P5. Below that, run [Remainder](#remainder-branching) as a model instead.
- Equal fractions, units and parts, and the ratio concepts land at P5-P6. Excess and shortage, difference, grouping, number × value and guess and check work from P4 upward, within that level's number range.

---

# The concepts

## Remainder (branching)

**Cue**: "of the remainder" — a second fraction taken from what is left, not from the whole.

**Method**: draw a branch diagram. The whole splits at the first fraction; the leftover branch splits again at the second. Each branch carries a fraction *of the branch above it*, so the fraction of the **total** is the product along the branch — which is why branching needs fraction × fraction.

> John spent 3/5 of his money on books and 1/3 of the remainder on a wallet. What fraction of his total money was left?
>
> ```
> Total  ─┬─ 3/5           books
>         └─ 2/5  ─┬─ 1/3  wallet   = 1/3 × 2/5 = 2/15
>           (rem.) └─ 2/3  leftover = 2/3 × 2/5 = 4/15
> ```
>
> Remainder after books = 1 − 3/5 = 2/5. Leftover after the wallet = 1 − 1/3 = 2/3 of that remainder.
> Fraction left = 2/3 × 2/5 = **4/15**.
>
> Continuing: if $16 was left, 4 units = $16, so 15 units = $16 ÷ 4 × 15 = **$60**.

**Below P5**, do it as a model: cut the bar into 5 units, label 3 units books and 2 units remainder, then cut every unit into 3 to get 15. The wallet is 1/3 × 6 = 2 of those, leftover is 6 − 2 = 4, so 4/15. Branching is faster and is what to move the child toward once fraction × fraction is available.

## Equal fractions

**Cue**: a fraction of one quantity is stated *equal to* a fraction of another.

**Method**: make the **numerators** the same — not the denominators. The denominators are then the ratio. This is the step children get backwards.

> 5/7 of the male dancers = 2/3 of the female dancers, 87 dancers in all. How many more females?
>
> 5/7 = 10/14, 2/3 = 10/15, so Males : Females = 14 : 15.
> 29u = 87, 1u = 3. Females exceed males by 1u = **3**.

The same move handles a remainder compared against a total, once branching has produced the remainder's fraction:

> Lena spent $16 on jeans, then 1/6 of her remaining money on a pizza, leaving 1/2 of her money. How much had she at first?
>
> ```
> Total  ─┬─ $16 (jeans)
>         └─ remainder ─┬─ 1/6  pizza
>                       └─ 5/6  leftover
> ```
>
> Leftover = 5/6 of the remainder, and that is 1/2 of the total. Make the numerators match: 5/6 of Remainder = 5/10 of Total, so Remainder : Total = 6 : 10 = 3 : 5.
> The $16 is the gap: 5u − 3u = 2u = $16, 1u = $8, total 5u = **$40**.

## Model drawing

**Cue**: "more than" or "less than" inside a fractions question, or a before-and-after scenario.

**Method**: draw both bars with the stated difference, convert the fractions to a common denominator, cut both bars into that many units, and track where the stated difference sits — the extra block gets cut by the fraction along with everything else.

> Jenny had 150 more cupcakes than Denise. Jenny gave away 1/5 of hers and Denise ate 3/4 of hers, leaving Jenny 208 more than Denise. How many had Denise at first?
>
> 1/5 = 4/20, 3/4 = 15/20 — cut both bars into 20u, with Jenny carrying an extra 150:
>
> ```
> At first   J [        20u        ][ 150 ]
>            D [        20u        ]
>
> Left       J [    16u    ][ 120 ]        keeps 4/5 of each piece
>            D [5u]                        keeps 1/4
>            J's bar exceeds D's by 208
> ```
>
> Jenny keeps 4/5, so 4/5 × 150 = 120 of the extra survives: Jenny has 16u + 120, Denise has 5u.
> The gap is 16u − 5u + 120 = 11u + 120 = 208, so 11u = 88, 1u = 8, and Denise had 20u = **160**.

## Constant part

**Cue**: one part is untouched while the other is spent or added to.

**Method**: scale both ratios so the **unchanged** part has the same number of units in each. The change then falls entirely on the other part.

> Ali and Billy have money in the ratio 5 : 6. After Billy spent $16 the ratio became 3 : 2. How much has Billy in the end?
>
> Ali is constant: 5 : 6 = 15 : 18, and 3 : 2 = 15 : 10.
> 18u − 10u = 8u = $16, 1u = $2. Billy ends with 10u = **$20**.

## Constant total

**Cue**: internal transfer — A gives to B, nothing enters or leaves.

**Method**: carry a Total column, and scale both ratios so the **total** matches.

> Ali and Billy have money in the ratio 5 : 4. After Ali gave Billy $20 they have equal amounts. How much has Billy in the end?
>
> Before, A : B : Total = 5 : 4 : 9 = 10 : 8 : 18. After, 1 : 1 : 2 = 9 : 9 : 18.
> Ali fell 10u − 9u = 1u = $20. Billy ends with 9u = **$180**.

## Constant difference

**Cue**: ages, or any pair changing by the same amount — "in N years' time".

**Method**: carry a Difference column and scale both ratios so the **difference** matches. Two people age together, so the gap never moves.

> Ali and Billy's ages are in the ratio 4 : 7. In 3 years they will be 3 : 5. How old is Billy now?
>
> Before, A : B : Difference = 4 : 7 : 3 = 8 : 14 : 6. After, 3 : 5 : 2 = 9 : 15 : 6.
> Ali gained 9u − 8u = 1u = 3 years. Billy is 14u = **42**.

## Everything changed

**Cue**: both parts change, by different amounts — nothing is constant, not the parts, the total or the difference. Typically the last 5-mark question on the paper.

**Method**: tabulate Before, Change, After in units; write the After column against the given final ratio; cross multiply.

> Ali's money to Billy's was 2 : 1. Ali saved another $60 and Billy spent $150, and the ratio became 4 : 1. How much had Ali at first?
>
> | | Before | Change | After |
> |---|---|---|---|
> | A | 2u | +60 | 2u + 60 |
> | B | 1u | −150 | 1u − 150 |
>
> (2u + 60) : (1u − 150) = 4 : 1, so 1 × (2u + 60) = 4 × (1u − 150).
> 2u + 60 = 4u − 600, so 2u = 660. Ali had 2u = **$660**.

## Excess and shortage

**Cue**: two conditions, one leaving something over and the other falling short. Both may be excesses, or both shortages.

**Method**: find the per-group difference between the two conditions, then distribute the excess and the shortage over it to get the number of groups.

> Tom packed 5 balls per bag with 8 left over; at 7 per bag he would need 4 more. How many bags, and how many balls?
>
> Per bag: 7 − 5 = 2. Bags from the excess: 8 ÷ 2 = 4. Bags from the shortage: 4 ÷ 2 = 2. Total **6 bags**.
> Balls: 6 × 5 + 8 = **38**, checked by 6 × 7 − 4 = 38.

The same shape with a cost per item:

> Mary needed $8 more for 12 pens, and had $4 left after 9 pens.
>
> 12 − 9 = 3 pens account for $8 + $4 = $12, so a pen is $4. She had 4 × 12 − 8 = **$40**, checked by 4 × 9 + 4 = $40.

**When the number of groups differs between the conditions, this method does not apply** — list and match instead:

> Packed in 4s, 3 books left over; packed in 6s, still 3 left over. Least number of books?
>
> 7, 11, 15, 19, 23… and 9, 15, 21, 27… → **15**.

## Difference

**Cue**: a redistribution, or two different rates of spending compared at one later moment.

**Method**: find the total difference and the per-unit difference; divide.

> Marbles packed equally into 10 bags; 4 bags tore and their marbles went equally into the other 6, which then held 20 more each. How many marbles altogether?
>
> The 6 bags gained 6 × 20 = 120, which came from 4 bags, so each bag held 120 ÷ 4 = 30. Total 30 × 10 = **300**.

> Alice and Betty got equal amounts. Alice spent $20 a day, Betty $25. When Alice had $157 left, Betty had $82. How much did each receive?
>
> Per day: $25 − $20 = $5. Total gap: $157 − $82 = $75. Days: 75 ÷ 5 = 15.
> Each received 15 × 20 + 157 = **$457**, checked by 15 × 25 + 82 = $457.

## Grouping

**Cue**: equal numbers of two items, or a repeating bundle.

**Method**: build one group, find its value, divide to get the number of groups. Where the counts are unequal, strip the excess first; where they are *equally many* of items given out at different rates, group by the LCM.

> Mark bought equal numbers of shorts and shirts for $100; a shirt is $8, shorts $12. How much on shirts?
>
> One group = $8 + $12 = $20. Groups: 100 ÷ 20 = 5. Shirts: 5 × 8 = **$40**.

> John bought 2 more pairs of shorts than shirts, $124 in total, same prices.
>
> Strip the extra: 12 × 2 = $24, leaving 124 − 24 = $100 of equal pairs. 100 ÷ 20 = **5 shirts**, and 5 + 2 = **7 pairs of shorts**.

> A class has equal boys and girls. 2 lollipops per 3 girls, 5 per 7 boys; boys got 4 more than girls. How many students?
>
> LCM of 3 and 7 is 21. Per 21 girls: 2 × 7 = 14. Per 21 boys: 5 × 3 = 15. Difference 1 per group.
> Groups: 4 ÷ 1 = 4. Students: 2 × 4 × 21 = **168**.

A group may also be the span over which a bonus is paid, and then the division leaves a remainder to convert back:

> Mary makes $2.50 a bottle, plus a $10 bonus for every 50 bottles. How many bottles must she sell to make $450?
>
> One group of 50 bottles = 50 × 2.50 + 10 = $135. Groups: 450 ÷ 135 = 3 remainder $45.
> The $45 earns no bonus, so it is 45 ÷ 2.50 = 18 more bottles.
> Total: 3 × 50 + 18 = **168 bottles**.

## Number × Value

**Cue**: coins, notes, or a price per unit. Count alone is not enough — multiply number by value.

**Method**: express each count in units, multiply by its value, and compare or total the values.

> 50-cent coins to $1 coins in the ratio 3 : 1, total value $12.50. How many coins?
>
> One group: 3 × $0.50 + 1 × $1 = $2.50. Groups: 12.50 ÷ 2.50 = 5. Coins: 5 × 4 = **20**.

> James has 44 more 20-cent than 50-cent coins, and the 50-cent coins are worth $2 more. How much has he?
>
> 50c: u coins, worth $0.5u. 20c: (u + 44) coins, worth $(0.2u + 8.8).
> 0.5u − (0.2u + 8.8) = 2 → 0.3u = 10.8 → u = 36.
> Total = 0.5 × 36 + 0.2 × 36 + 8.8 = **$34**.

> Cherries cost $0.50/kg more than grapes. $312 collected in all; 3/4 as much cherries as grapes by mass; grapes brought in $24 more than cherries. Mass of grapes, and cost per kg of cherries?
>
> Cherries : Grapes = 3 : 4 by mass. Cherries earned (312 − 24) ÷ 2 = $144, grapes $168.
> Per mass unit: cherries $144 ÷ 3 = $48, grapes $168 ÷ 4 = $42, differing by $6 — which is $0.50 × the unit mass, so 1 unit = 6 ÷ 0.5 = 12 kg.
> Grapes: 12 × 4 = **48 kg**. Grapes cost 168 ÷ 48 = $3.50/kg, so cherries are **$4.00/kg**.

## Guess and check / assumption

**Cue**: two item types with a known total count and a known total value or difference.

**Method**: assume the extreme — all of one type — then swap one and read the per-swap change. Divide the gap by it. Faster and more systematic than tabulating guesses, and it still ends in a check.

> 8 students; each girl got 5 pencils, each boy 2; 22 pencils in all. How many boys?
>
> Suppose 8 girls: 8 × 5 = 40. Suppose 7 girls and 1 boy: 7 × 5 + 1 × 2 = 37.
> Each boy costs 3 pencils. Gap: 40 − 22 = 18. Boys: 18 ÷ 3 = **6**.
> Check: 2 girls and 6 boys give 2 × 5 + 6 × 2 = 22. ✓

> 100 two-dollar and five-dollar notes; the five-dollar notes are worth $290 more. How much money?
>
> Suppose 100 fives: difference $500. Suppose 99 fives and one two: 99 × 5 − 1 × 2 = $493 — each swap cuts the difference by $7.
> 500 − 290 = 210, so 210 ÷ 7 = 30 twos and 70 fives. Total 30 × 2 + 70 × 5 = **$410**.

## Units and parts

Also called simultaneous equations. **Cue**: two people each spending a different fraction of their *own* amount.

**Method**: let one person's amount be **units** and the other's **parts**, chosen so each fraction divides exactly. Form two equations — one from the starting situation, one from the final — scale one so a variable matches, then add or subtract.

> Amy and Billy had $400 together. Amy spent 1/4 of hers, Billy 2/5 of his, leaving $255 between them. How much did Amy spend?
>
> Amy = 4u, Billy = 5p. Then 4u + 5p = 400.
> Left: Amy 3u, Billy 3p, so 3u + 3p = 255 → u + p = 85 → 4u + 4p = 340.
> Subtracting, p = 60, so u = 85 − 60 = 25. Amy spent 1u = **$25**.

> Ahmad and Bernard had $240 together. Ahmad spent 2/3 of his, Bernard 3/5 of his, and Bernard then had $8 more than Ahmad. How much did they spend altogether?
>
> Ahmad = 3u, Bernard = 5p: 3u + 5p = 240.
> Left: Ahmad u, Bernard 2p, so 2p − u = 8 → 6p − 3u = 24.
> Adding, 11p = 264, p = 24. Then 5p = 120, 3u = 120, u = 40.
> Spent: 2u + 3p = 80 + 72 = **$152**.

## Working backwards

**Cue**: a final value given, the starting value asked for — "in the end", "at first".

**Method**: undo each step in reverse, inverting every operation. For two people exchanging, use a table with a row per stage and fill it upward from the end.

> A bus left the interchange. At stop 1, 1/4 alighted and 5 boarded. At stop 2, 1/2 alighted and 20 boarded. It then carried 60. How many left the interchange?
>
> Before stop 2's boarding: 60 − 20 = 40; before the alighting: 40 × 2 = 80.
> Before stop 1's boarding: 80 − 5 = 75; that is 3/4 of the start, so 75 ÷ 3 × 4 = **100**.

> Amy and Betty have 48 sweets between them. Amy gave 1/4 of hers to Betty; Betty then gave 1/3 of her total to Amy; they ended equal. How many had each at first?
>
> Draw the table with a row per stage, fill the End row first, and work upward.
>
> End: 48 ÷ 2 = 24 each.
> Betty gave away 1/3, so she kept 2/3: before she gave, 24 ÷ 2 × 3 = 36, leaving Amy 48 − 36 = 12.
> Amy kept 3/4, so at first: 12 ÷ 3 × 4 = **16**, and Betty had 48 − 16 = **32**.
>
> | | Amy | Betty |
> |---|---|---|
> | Start | 16 | 32 |
> | after Amy → Betty | 12 | 36 |
> | End | 24 | 24 |

## Double if

**Cue**: two hypothetical conditions, both counterfactual — neither describes what actually happened.

**Method**: write each condition in units, then force the quantity that is common to both to the same number of units, and equate.

> A farmer sells 2 chickens and 3 ducks daily: 50 chickens remain when the ducks run out. Selling 3 chickens and 2 ducks daily: 25 chickens remain when the ducks run out. How many ducks, and how many chickens?
>
> Case 1 — Chicken : Duck = 2u : 3u. Case 2 — 3u : 2u. The ducks sell out in both, so match them at 6u: Case 1 becomes 4u : 6u, Case 2 becomes 9u : 6u.
> Chickens: 4u + 50 = 9u + 25 → 5u = 25 → 1u = 5.
> Ducks: 5 × 6 = **30**. Chickens: 5 × 4 + 50 = **70**, checked by 5 × 9 + 25 = 70.

> If Sam gives Terry $350 he will have 4 times Terry's money; if he gives $550 he will have thrice. How much has Sam?
>
> From the first if, S : T = 4u : 1u, so at the start S : T = (4u + 350) : (1u − 350).
> Under the second if, S : T = (4u + 350 − 550) : (1u − 350 + 550) = (4u − 200) : (1u + 200) = 3 : 1.
> 3 × (1u + 200) = 1 × (4u − 200) → 3u + 600 = 4u − 200 → 1u = 800.
> Sam has 4u + 350 = **$3550**.

---

A child may reach the same answer by another route, and more than one method is often right. More methods means more tools in the exam, so a correct alternative is to be credited and added to, not corrected toward the method here.
