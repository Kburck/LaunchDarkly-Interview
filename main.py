import ldclient
from ldclient.config import Config
from ldclient.context import Context  # ✅ Import Context correctly
import time

# Replace with your LaunchDarkly SDK key
LD_SDK_KEY = "sdk-c19409a5-2c85-4514-b2e0-2445a0910b59"

# Replace with your feature flag key from LaunchDarkly
FEATURE_FLAG_KEY = "sample-feature"

def main():
    # Initialize the LaunchDarkly client
    ldclient.set_config(Config(LD_SDK_KEY))

    if ldclient.get().is_initialized():
        print("LaunchDarkly client initialized successfully!")
    else:
        print("LaunchDarkly client failed to initialize.")
        return

# Use LaunchDarkly Context instead of a dictionary
 
user = (
    Context.builder("example-user")
    .set("email", "user@example.com")
    .set("role", "admin")  # Change role to "member" or "guest" to test targeting
    .build()
)



    def check_feature():
        """Checks if the feature flag is enabled or disabled."""
        flag_enabled = ldclient.get().variation(FEATURE_FLAG_KEY, user, False)

        if flag_enabled:
            print("🚀 Feature is ON: Showing the new feature!")
        else:
            print("❌ Feature is OFF: Hiding the new feature.")

    print("Listening for feature flag changes... Press Ctrl+C to stop.")

    try:
        while True:
            check_feature()
            time.sleep(5)  # Check the flag every 5 seconds
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        ldclient.get().close()

if __name__ == "__main__":
    main()
