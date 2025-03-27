import os
from ldclient import LDClient, Context

SDK_KEY = os.getenv('LAUNCHDARKLY_SDK_KEY')

def setup_feature_flag():
    """
    Set up LaunchDarkly client and demonstrate feature flag usage
    """
    # Validate SDK Key
    if not SDK_KEY:
        raise ValueError("LaunchDarkly SDK Key is not set. Set LAUNCHDARKLY_SDK_KEY environment variable.")
    
    # Initialize LaunchDarkly client
    ldclient = LDClient(SDK_KEY)

    # Create a user context
    # In a real app, this would be a unique user identifier
    user_context = Context.builder('user-123').\
        name('Test User').\
        build()

    # Check if feature flag is enabled
    show_new_feature = ldclient.variation(
        "new-dashboard-feature",  # Must match flag key in LaunchDarkly
        user_context,             # User context
        False                     # Default value if flag can't be evaluated
    )

    # Demonstrate feature flag logic
    if show_new_feature:
        print("🟢 New feature is ENABLED!")
        # Your new feature implementation would go here
        return "New Feature Content"
    else:
        print("🔴 New feature is DISABLED")
        # Fallback to existing implementation
        return "Original Feature Content"

def main():
    try:
        result = setup_feature_flag()
        print(f"Feature result: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()