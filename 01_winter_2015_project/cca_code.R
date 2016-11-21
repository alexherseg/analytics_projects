# Alejandro Hernandez
# Chicago CCA Project

# library contains the cca model function
library(candisc)
# for EDA
library(dplyr)

# datasets: crime, business_licenses, and vacant_properties
crime <- read.csv('crime_cca.csv', header=T)
cor(crime)
bsn_lcns <- read.csv('bsn_lcns_cca.csv', header=T)
cor(bsn_lcns)
vacant_buildings <- read.csv('vacant_buildings_cca.csv', header=T)
cor(vacant_buildings)

# removes the first column, which contains the zip codes
#row.names(crime) <- crime[,1]
c <- crime[,-1]
c
dim(c) # 30 variables
names(c) <- c('c1','c2','c3','c4','c5','c6','c7','c8','c9','c10',
		'c11','c12','c13','c14','c15','c16','c17','c18','c19','c20',
		'c21','c22','c23','c24','c25','c26','c27','c28','c29','c30')
cor(c)
#row.names(bsn_lcns) <- bsn_lcns[,1]
b <- bsn_lcns[,-1]
dim(b) # 19 variables

row.names(vacant_buildings) <- vacant_buildings[,1]
names(vacant_buildings)
v <- vacant_buildings[,-1]
dim(v) # 8 variables
cor(v)


# creates the cca model
cca_model <- cancor(b, c)
# (cca_model$cancor**2) # canonical r squared
# results summary
summary(cca_model)
names(cca_model$scores)
# more output
cca_model$structure
plot( x=cca_model$scores$X[,1], 
	y=cca_model$scores$X[,2])
text( x=cca_model$scores$X[,1], 
	y=cca_model$scores$X[,2],
	labels=row.names(bsn_lcns),
	pos=1)
diff <- cca_model$scores$X[,1]
cols <- c('red','black')[(diff>0)+1]
barplot(diff, col=cols, horiz=F)

diff <- cca_model$scores$Y[,1]
cols <- c('red','black')[(diff>0)+1]
barplot(diff, col=cols, horiz=F)

# creates the second cca model
cca_model2 <- cancor(v, b)
summary(cca_model2)
cca_model2$structure
cor(v)
names(b) <- c('b1','b2','b3','b4','b5','b6','b7','b8','b9',
			'b10','b11','b12','b13','b14','b15','b16',
				'b17','b18','b19')
cor(b)

names(v) = c('x1','x2','x3','x4','x5','x6','x7','x8')
y <- cca_model2$scores$X[,1]
vif(lm(x1 ~ x2 + x3+ x4+ x5+ x6+ x7 +x8, v))

redundancy(cca_model2)
# -------------------------------------------------------------------------
crime.pca <- princomp(c, cor = TRUE, scores = TRUE); crime.pca
plot(crime.pca)
summary(crime.pca)
crime.pca$scores
crime.pca$loadings
plot(crime.pca$scores)

bldg_prmts <- read.csv('cleaned_building_permits.csv', header=T)

d <- bldg_prmts[,-1];
d <- d[,-12:-23] # removes empty columns
dim(d) # 11 variables

cca_model3 <- cancor(v, d)
summary(cca_model3)
cca_model3$structure

cca_model4 <- cancor(v, c)
summary(cca_model4)
cca_model4$structure

# deceptive practice: 	identity theft $300 and under or $300+, credit card fraud, counterfeiting document,
#						forgery, theft of labor/services, counterfeiting a document, fraud or confidence game,
#						illegal use of cash card, theft of prop, bad check, 
# weapons violation:	unlawful possesion of handgun, possesion of handgun without FOID, unlawful use of dangerous weapon,
#						carrying in a restricted area 
# other offense: 		parole violation, harrasment by telephone, violate order of protection, animal abuse/neglect,
# 						telephone threat, violation of civil no contact order, sex offender failed to register
# offense involving children:	child abuse, neglect, 
# liquor law violation:	license violation, consumption by minor, possesion by minor, endangering a child, child abandonment
# interference with public officer: resisting arrest, obstruction of justice, aiding arrestee escape, 
# intimidation: 		extortion, educational intimidation
# other narcotics violation: 	intoxicating compounds
# non-criminal: 		license violation