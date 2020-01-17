TESTS = 25 50 75 100 150 200
NTITER=200

all:
	echo "Usage:"\
	       * 'make tests' to run all tests"
	       * 'make summary' to summarize results

tests:
	for i in $(TESTS); do\
		echo "Test nx=$$i"; \
		FreeFem++-nw ks_acute-specialQuad.edp -nx $$i -nt $(NTITER) > test_nx=$$i.out; \
	done

summary:
	for i in $(TESTS); do\
		echo "Test nx=$$i =================>"; \
		grep "max.u.* Positivity broken" test_nx=$$i.out -A2  | head -n4; \
	done
