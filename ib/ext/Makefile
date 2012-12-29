srcdir := ./src/IBJts/java/com/ib/client/
modules := $(addsuffix .py, $(notdir $(basename $(wildcard $(srcdir)*.java))))


.PHONY: all cfg clean clean-modules src


all: src cfg $(modules)


cfg:
	cd ../../ && sudo python setup_config.py install

clean:
	rm -f *.pyo
	rm -f *.pyc
	cd src && $(MAKE) clean


src:
	cd src && $(MAKE)


$(modules):
	j2py -i $(addprefix $(srcdir), $(addsuffix .java, $(basename $@))) -o $@ -c ib.cfg -c ib.cfg.$(basename $@) -s

modules-clean: clean-modules
clean-modules:
	rm -rf $(modules)

