ACUTE=1
NX=100
DT=1.e-6
NT=100
CU0=1000
CV0=500

VTK=1
OUTNAME="acute=$(ACUTE)_nx=$(NX)_dt=$(DT)_nt=$(NT)_cu0=$(CU0)_cv0=$(CV0)"
OUTFILE="$(OUTNAME).out"
OUTDIR="tests/$(OUTNAME)"

FREEFEM=FreeFem++-nw

all: help

help:
	@echo "Usage:\n\
	       * 'make test' to run current test (see parameters in Makefile)\n\
	       * 'make summary' to summarize results\n"
	@echo "Example:\n\
		make test NX=200"

test:
	@echo "Running FreeFem++ test, saving output to $(OUTFILE)"
	$(FREEFEM) ks_acute.edp -acute $(ACUTE) -nx $(NX) -dt $(DT) -nt $(NT) -cu0 $(CU0) -cv0 $(CV0) -vtk $(VTK) > $(OUTFILE) &


move:
	@echo "Moving all vtk files and output to $(OUTDIR)"
	@mkdir -p $(OUTDIR)
	@mv *.vtk *.out $(OUTDIR)


summary:
	@for i in *.out; do\
		echo "Test file: $$i =================>"; \
		grep "max.u.* Positivity broken" $$i -A2 -B4 | head -n7 | grep -v computing; \
	done

