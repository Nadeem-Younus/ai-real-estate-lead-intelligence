from backend.services.langfuse_service import langfuse

with langfuse.start_as_current_observation(
    as_type="span",
    name="same-client-test"
):
    print("inside")

langfuse.flush()

print("done")