import streamlit as st
import requests

label_map = {
    0: "Negative 😠",
    1: "Neutral 😐",
    2: "Positive 😊"
}

st.set_page_config(page_title="Comment Sentiment", page_icon="💬")
st.title("💬 Sentiment Analyzer (via Flask API)")

comment = st.text_area("📝 Your Comment", placeholder="Type something like: 'This product is amazing!'")

if st.button("Analyze Sentiment"):
    if not comment.strip():
        st.warning("Please enter a valid comment.")
    else:
        try:
            response = requests.post("http://localhost:5000/predict", json={"text": comment})
            result = response.json()

            if "prediction" in result:
                pred = result["prediction"]
                probs = result["probabilities"]

                st.subheader("🔍 Sentiment Result")
                st.success(f"**{label_map[pred]}**")

                st.markdown("#### 🔢 Probabilities")
                for i, prob in enumerate(probs):
                    st.write(f"{label_map[i]}: {prob:.2%}")
            else:
                st.error(f"API error: {result.get('error', 'Unknown error')}")

        except Exception as e:
            st.error(f"Error contacting prediction service: {str(e)}")


# Optional: Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit By Kajoot")