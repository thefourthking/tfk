

import junit.framework.TestCase;
import junit.framework.TestSuite;

public class  lab_1Test extends TestCase {

private lab_1 calcEngine;

/**

* For initializing the values.

* Initialization of the variables can be done here.

*/

protected void setUp() throws Exception {

super.setUp();

}

/**

* For cleaning the values.

* Dereference/Uninitialization/freeing memory can be done here.

*/




protected void tearDown() throws Exception {

super.tearDown();

}

/**

* Constructor for CalculationTest.

* @param arg0

*/

public lab_1Test(String arg0) {

super(arg0);

calcEngine = new lab_1();

}

// test case method name should start with test.

public final void testAdd() {

assertEquals(calcEngine.add(20, 30), 5);

}

// test case method name should start with test.

public final void testSubtract() {

assertEquals(calcEngine.subtract(60, 30), 30);

}

// test case method name should start with test.

public final void testMultiply() {

assertEquals(calcEngine.multiply(100, 3), 300);

}

// test case method name should start with test.

public final void testDivide() {

assertEquals(calcEngine.divide(333, 3), 111);

try {

assertEquals(calcEngine.divide(100, 0), 20);

} catch (Exception e) {

// Exception is expected so asserting for true.

assertTrue(true);

}

}

public static void main(String[] args) {

junit.textui.TestRunner.run(lab_1Test.suite());

}

private static TestSuite suite() {

TestSuite suite = new TestSuite("Test for Engine.Calculation.java");

//$JUnit-BEGIN$

suite.addTestSuite(lab_1Test.class);

//$JUnit-END$

return suite;

}

}

//Sample JUnit code to run in text mode (CLI – command line).

/*
public static void main(String[] args) {

junit.textui.TestRunner.run(CalculationTest.suite());

}

private static TestSuite suite() {

TestSuite suite = new TestSuite(“Test for Engine.Calculation.java”);

//$JUnit-BEGIN$

suite.addTestSuite(CalculationTest.class);

//$JUnit-END$

return suite;

}*/
