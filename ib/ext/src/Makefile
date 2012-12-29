ibsources_jar := twsapi_unixmac_965.jar
ibsources_url := "http://www.interactivebrokers.com/download/$(ibsources_jar)"


.PHONY: all clean


all: $(ibsources_jar) IBJts filtervector


$(ibsources_jar):
	wget $(ibsources_url)


IBJts:
	jar -xf $(ibsources_jar)

filtervector:
	python javagenerics_filter.py

clean:
	rm $(ibsources_jar)
	rm -rf IBJts

