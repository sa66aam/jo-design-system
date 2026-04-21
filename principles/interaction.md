# Interaction

How controls should behave. Written from the specific failures that taught each lesson.

## Same affordance, same shape across roles

If a moderator and a director can both "jump to chapter X," the control they use must look and behave identically. Don't give one role a dropdown and the other a grid of tiles. The app's shape should not tell the user which role they're in - the data they see should.

R20 failed this. The moderator had a Chapters dropdown in the scoring hero; the director had a 9-tile grid (8 chapters + an ALL tile). Same intent, two shapes. Fix was to port the dropdown to the director and delete the ALL tile - not because tiles are wrong, but because *inconsistency between equivalent roles* is.

If you're adding a control to one role's view, grep the other role's component tree first. If the same affordance exists there, match the shape. If it doesn't exist there but should, add it in both places in the same change.

## One surface, one signal

A control should not both close itself and do something else on the same click. If a dropdown option routes the user to a new view, closing the dropdown is the only thing the click does - the view change is the consequence, not a second action. Sequencing looks like this:

1. User clicks item.
2. Local state flips: dropdown closes.
3. Parent state updates: selected chapter changes.
4. Parent re-renders: new view mounts.

The order matters. Closing the dropdown *after* the navigation causes a flicker where the dropdown briefly sits over the new view. Closing it *before* the state update is fine - the user doesn't care that the dropdown went first.

## Shell owns navigation, view owns content

The outer app shell (header, sidebar, role switcher) is the only place that routes between top-level surfaces. A content view can open overlays, toggle filters, expand sections - but it cannot tell the shell to unmount itself. If a view needs to exit, it calls a prop (`onClose`, `onBack`) and lets the shell decide.

This is why the director's Back button in the chapter view is `onClick={() => setExpandedChapter(null)}` - the parent owns `expandedChapter`, the child just signals.

## Dropdowns close on outside click *and* item select *and* Escape

All three, every time. The useEffect pattern for outside-click is:

```jsx
useEffect(() => {
  if (!open) return;
  const onDown = (e) => {
    if (ref.current && !ref.current.contains(e.target)) setOpen(false);
  };
  document.addEventListener('mousedown', onDown);
  return () => document.removeEventListener('mousedown', onDown);
}, [open]);
```

Guarding on `if (!open) return` matters - otherwise you're adding and removing a listener on every render of the parent, which is cheap but pointless.

## Terminal UI must close

Any UI surface the user opens must have a visible, obvious way to close. Dropdowns need a chevron that rotates, overlays need an X, modals need a backdrop tap target. "Click outside to close" is a backup, not the primary affordance - users who've been burned once by a modal that ate their input will never click outside again.

## Don't steal focus

Auto-focusing the first input on mount is tempting and almost always wrong. The user just clicked something to arrive at this view; they know where their attention is. The exception is a modal with a single obvious input (search, login) - those get focus. Forms with five fields do not.

## Loading states are states, not delays

If a value isn't ready, the slot should render the right size and shape with a skeleton or dashes - not an empty placeholder that jumps when the real content arrives. Layout shift at 180ms is more jarring than a skeleton that resolves in 1s.

For the readiness bar specifically: render the track immediately with a 0% fill, then animate the fill width once the number is known. The track's presence tells the user "this is a progress bar" before the number arrives.

## Write-through is a boundary, not a sprinkle

If the app has a persistence contract (e.g. sync-read state, async write-back), don't scatter `await` calls across components to "save as you go." Commit at named boundaries: on blur, on submit, on navigation, on visibility change. Scattered awaits turn into scattered bugs.

The CBAHI PHC pattern: every call site reads sync; the only async boundary is the boot bridge (`firebaseStateBridge.js`). Writes queue and flush. It's more code up front but it's the reason the app doesn't flicker on every keystroke.

## Sync over async whenever possible

The UI layer should not know about promises. If a component has to `await` something to render, that's a failure at the data layer - either the value should have been pre-fetched, or it should stream in via a subscription, or the component is reading too eagerly. The fastest interaction is the one that doesn't have to wait.
