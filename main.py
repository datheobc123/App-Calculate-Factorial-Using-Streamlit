import streamlit as st

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def main():
    st.title("Factorial Calculator")
    num = st.number_input("Enter a number: ", min_value=0, max_value=1000)
    if st.button("Calculate"):
        result = fact(num)
        st.write(f"The factorial of {num} is {result}")

if __name__ == "__main__":
    main()
